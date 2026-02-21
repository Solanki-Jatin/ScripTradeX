import sqlite3

def init_db():
    conn = sqlite3.connect('scriptradex.db')
    c = conn.cursor()

    # Create Users Table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY, username TEXT, role TEXT, balance REAL)''')
    
    # Create Pseudo-Government Scrip Registry (The "ICEGATE" Data)
    c.execute('''CREATE TABLE IF NOT EXISTS govt_registry (
                    scrip_id TEXT PRIMARY KEY, owner TEXT, value REAL, status TEXT)''')
    
    # Create Platform Marketplace Table
    c.execute('''CREATE TABLE IF NOT EXISTS marketplace (
                    id INTEGER KEY, scrip_id TEXT, seller TEXT, 
                    value REAL, discount REAL, price REAL, status TEXT)''')

    # ---- SEED DUMMY DATA ----
    # 1. Add Users (Seller has 0 cash to start, Buyer has 1,000,000 cash)
    c.execute("INSERT OR IGNORE INTO users (id, username, role, balance) VALUES (1, 'Alpha Exports', 'seller', 0.0)")
    c.execute("INSERT OR IGNORE INTO users (id, username, role, balance) VALUES (2, 'Global Imports', 'buyer', 1000000.0)")

    # 2. Add Dummy Scrips to Government Registry
    c.execute("INSERT OR IGNORE INTO govt_registry (scrip_id, owner, value, status) VALUES ('RODTEP101', 'Alpha Exports', 500000.0, 'Active')")
    c.execute("INSERT OR IGNORE INTO govt_registry (scrip_id, owner, value, status) VALUES ('ROSCTL202', 'Alpha Exports', 120000.0, 'Active')")

    conn.commit()
    conn.close()
    print("Database Initialized with Pseudo-Govt Data!")

if __name__ == '__main__':
    init_db()
