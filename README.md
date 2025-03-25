# Simple Blockchain Simulation with API

## 📌 Overview
This project is a **simple blockchain simulation** implemented in Python with Flask. It allows users to interact with the blockchain via a REST API, including:
- Adding transactions
- Mining blocks
- Retrieving the blockchain
- Validating the blockchain

## ✨ Features
✅ **Blockchain Structure**: Blocks contain an index, timestamp, transactions, previous hash, proof, and hash.  
✅ **Hashing Mechanism**: SHA-256 is used to ensure data integrity.  
✅ **Proof-of-Work**: Implements computational effort for block validation.  
✅ **Blockchain Validation**: Ensures integrity and detects tampering.  
✅ **REST API Integration**: Easily interact with the blockchain using HTTP requests.

## 🛠️ Prerequisites
Ensure you have Python installed along with Flask:
```sh
pip install flask
```

## 🚀 Installation & Setup
1️⃣ **Clone this repository:**
```sh
git clone https://github.com/your-username/blockchain-simulation.git
cd blockchain-simulation
```
2️⃣ **Install dependencies:**
```sh
pip install -r requirements.txt
```
3️⃣ **Run the application:**
```sh
python blockchain.py
```

## 🔗 API Endpoints
| Endpoint        | Method | Description |
|---------------|--------|-------------|
| `/chain` | GET | Retrieve the blockchain |
| `/transaction` | POST | Add a transaction (JSON: `{ "transaction": "Alice pays Bob 10 BTC" }`) |
| `/mine` | GET | Mine a new block |
| `/validate` | GET | Validate the blockchain |

## 🖥️ Usage Examples
### 1️⃣ Start the server
```sh
python blockchain.py
```
### 2️⃣ Get Blockchain Data
```sh
curl http://127.0.0.1:5000/chain
```
### 3️⃣ Add a Transaction
```sh
curl -X POST -H "Content-Type: application/json" -d '{"transaction": "Alice pays Bob 10 BTC"}' http://127.0.0.1:5000/transaction
```
### 4️⃣ Mine a Block
```sh
curl http://127.0.0.1:5000/mine
```
### 5️⃣ Validate the Blockchain
```sh
curl http://127.0.0.1:5000/validate
```

## 🐳 Docker Setup (Optional)
You can run this blockchain simulation inside a **Docker container**.
### 1️⃣ Build the Docker Image
```sh
docker build -t blockchain-simulation .
```
### 2️⃣ Run the Container
```sh
docker run -p 5000:5000 blockchain-simulation
```

## 📌 Future Enhancements
- 🔗 Implement a **peer-to-peer network** for decentralized validation.
- 🎨 Add a **web-based user interface**.
- 🔑 Implement **cryptographic signatures** for transactions.

## 📜 License
This project is open-source and available under the **MIT License**.

---
🔗 **Follow & Star** ⭐ the repo if you like it!  
📧 **Contact:** your-email@example.com  
🚀 **Contributions Welcome!**

