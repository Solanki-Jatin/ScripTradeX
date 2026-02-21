from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'hackathon_secret_key'

def get_db():
    conn = sqlite3.connect('scriptradex.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    if user:
        session['username'] = user['username']
        session['role'] = user['role']
        return redirect('/dashboard')
    return "User not found. Use 'Alpha Exports' or 'Global Imports'."

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/')
    
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE username=?", (session['username'],)).fetchone()
    
    # Fetch active market listings
    listings = db.execute("SELECT * FROM marketplace WHERE status='Listed'").fetchall()
    
    # Fetch Seller's specific listings
    my_listings = db.execute("SELECT * FROM marketplace WHERE seller=?", (session['username'],)).fetchall()
    
    return render_template('dashboard.html', user=user, listings=listings, my_listings=my_listings)

# --- THE TECHNICAL APIs ---

@app.route('/api/verify_and_list', methods=['POST'])
def verify_and_list():
    """Step 1: Pings Govt API, verifies, and lists on marketplace"""
    scrip_id = request.form['scrip_id']
    discount = float(request.form['discount'])
    seller = session['username']
    
    db = get_db()
    # 1. API Verification (Ping Pseudo-Govt Server)
    govt_data = db.execute("SELECT * FROM govt_registry WHERE scrip_id=? AND owner=? AND status='Active'", (scrip_id, seller)).fetchone()
    
    if not govt_data:
        return jsonify({"success": False, "message": "Verification Failed: Scrip Invalid or Not Owned by you."})
    
    # 2. Calculate Price & List
    value = govt_data['value']
    price = value - (value * (discount / 100))
    
    db.execute("INSERT INTO marketplace (scrip_id, seller, value, discount, price, status) VALUES (?, ?, ?, ?, ?, 'Listed')",
               (scrip_id, seller, value, discount, price))
    db.commit()
    return redirect('/dashboard')

@app.route('/api/buy', methods=['POST'])
def buy():
    """Step 2 & 3: Escrow Hold and Settlement logic"""
    market_id = request.form['market_id']
    buyer = session['username']
    
    db = get_db()
    listing = db.execute("SELECT * FROM marketplace WHERE id=?", (market_id,)).fetchone()
    buyer_data = db.execute("SELECT * FROM users WHERE username=?", (buyer,)).fetchone()
    seller_data = db.execute("SELECT * FROM users WHERE username=?", (listing['seller'],)).fetchone()
    
    price = listing['price']
    
    # Check if Buyer has enough funds
    if buyer_data['balance'] < price:
        return "Insufficient Funds!"
        
    # --- ESCROW LOGIC & SETTLEMENT ---
    # 1. Deduct from buyer
    new_buyer_balance = buyer_data['balance'] - price
    db.execute("UPDATE users SET balance=? WHERE username=?", (new_buyer_balance, buyer))
    
    # 2. Calculate 1% Platform Commission and pay seller
    commission = price * 0.01
    seller_payout = price - commission
    new_seller_balance = seller_data['balance'] + seller_payout
    db.execute("UPDATE users SET balance=? WHERE username=?", (new_seller_balance, listing['seller']))
    
    # 3. Transfer Ownership in Pseudo-Govt Registry
    db.execute("UPDATE govt_registry SET owner=? WHERE scrip_id=?", (buyer, listing['scrip_id']))
    
    # 4. Update Marketplace Status
    db.execute("UPDATE marketplace SET status='Completed' WHERE id=?", (market_id,))
    
    db.commit()
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
