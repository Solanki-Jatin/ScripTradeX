<div align="center">
  
  # 🚀 ScripTradeX
  **The Verified Exchange for EXIM Duty Credits**

  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)](#)
  [![Flask](https://img.shields.io/badge/Flask-3.0.1-black.svg?logo=flask&logoColor=white)](#)
  [![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg?logo=sqlite&logoColor=white)](#)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

  > Moving the $2 Trillion export economy from "Who you know" to a secure, centralized digital floor.

</div>

---

## 🛑 The Problem: "Frozen Capital"
Indian exporters lose up to **10% of their script value** due to a fragmented, opaque, and manual secondary market for Duty Credit Scrips. 
* 📉 **No Centralized Hub:** Trading relies on WhatsApp groups and offline brokers.
* 💸 **High Fees:** Brokers charge 3-5% commissions.
* ⚠️ **Security Risks:** High chance of "double-selling" and script fraud.

## 💡 Our Solution
**ScripTradeX** is a secure B2B digital exchange. We replace manual brokers with a centralized matching engine and an automated escrow system.
* 🔐 **API Verification:** Pings government portals (Pseudo-ICEGATE) to verify script validity *before* listing.
* ⚡ **Instant Matching:** Buyers and sellers are matched instantly based on required credit amounts and discount rates.
* 🛡️ **Digital Escrow:** Payment is held securely until delivery is verified, ensuring zero fraud.
* 💰 **Cost Efficiency:** A flat **1% transaction fee**, maximizing savings.

---

## ⚙️ How It Works (Workflow)



| 🧑‍💼 Exporter (Seller) Flow | 🏢 Importer (Buyer) Flow |
| :--- | :--- |
| **1. Verify:** Enters Scrip ID (e.g., RoDTEP). | **1. Discover:** Browses verified matches on the marketplace. |
| **2. List:** System validates via Govt API and lists the offer. | **2. Lock:** Clicks "Buy", moving funds into the secure Escrow. |
| **3. Transfer:** Transfers credit on Govt Portal. | **3. Verify:** System performs a re-check of validity. |
| **4. Settle:** Receives instant payout. | **4. Receive:** Gains the credit for duty relaxation. |

---

## 🛠️ Tech Stack
This MVP is built for rapid deployment and robust logic demonstration:
* **Backend:** Python / Flask
* **Database:** SQLite (Relational DB for Escrow & State tracking)
* **Frontend:** HTML5, Bootstrap 5 (Responsive UI)
* **Integrations:** Mock Government Registry API (Local JSON/SQL logic)

---

## 📂 Project Structure

```text
ScripTradeX_MVP/
│
├── app.py              # Main Flask Backend (API & Escrow Logic)
├── init_db.py          # Database Setup (Pseudo-Govt Registry)
├── scriptradex.db      # SQLite Database (Created after init)
├── requirements.txt    # Project Dependencies
│
└── templates/          # Frontend UI (Bootstrap 5)
    ├── login.html      # Authentication Page
    └── dashboard.html  # Seller & Buyer Dashboards
```
---

## 🚀 Getting Started (Run Locally)

Follow these steps to run the ScripTradeX MVP on your local machine:

### 1. Clone the repository
```bash
git clone [https://github.com/yourusername/ScripTradeX.git](https://github.com/yourusername/ScripTradeX.git)
cd ScripTradeX
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize the Pseudo-Govt Database
```bash
python init_db.py
```

### 4. Run the Engine
```bash
python app.py
```

---

## 🧪 Demo Credentials

To test the application, use the dropdown on the login screen with these pre-configured accounts:

### 🟢 Seller Account (Alpha Exports)
* **Role**: Exporter looking to sell surplus credits.
* **Valid Demo Scrips to test**: 
  * `RODTEP101` (Face Value: ₹5,00,000)
  * `ROSCTL202` (Face Value: ₹1,20,000)
* **Tip**: Try typing a fake ID like `XYZ999` to see the **API Verification** reject the listing.

### 🔵 Buyer Account (Global Imports)
* **Role**: Importer looking to buy credits at a discount.
* **Starting Balance**: ₹1,00,00,000
* **Action**: Browse the marketplace and click **"Buy & Lock Escrow"** on a listed scrip to trigger the secure settlement logic.

---

<div align="center">
  <i>Built with 💻 and ☕ for the Hackathon</i>
</div>
