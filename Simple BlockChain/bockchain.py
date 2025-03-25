import hashlib
import time
import json
from flask import Flask, jsonify, request

class Block:
    def __init__(self, index, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "proof": self.proof
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0", 0)
        self.chain.append(genesis_block)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def proof_of_work(self, previous_proof):
        proof = 0
        while not self.valid_proof(previous_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(previous_proof, proof):
        guess = f'{previous_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Example difficulty

    def add_block(self):
        previous_block = self.chain[-1]
        proof = self.proof_of_work(previous_block.proof)
        new_block = Block(len(self.chain), self.transactions, previous_block.hash, proof)
        self.chain.append(new_block)
        self.transactions = []

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.previous_hash != previous_block.hash:
                return False
            if not self.valid_proof(previous_block.proof, current_block.proof):
                return False
        return True

    def get_chain(self):
        return [vars(block) for block in self.chain]

# Initialize Flask app
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    response = {
        "chain": blockchain.get_chain(),
        "length": len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    if not data or 'transaction' not in data:
        return jsonify({"message": "Invalid transaction data"}), 400
    blockchain.add_transaction(data['transaction'])
    return jsonify({"message": "Transaction added"}), 201

@app.route('/mine', methods=['GET'])
def mine_block():
    blockchain.add_block()
    return jsonify({"message": "Block mined successfully"}), 200

@app.route('/validate', methods=['GET'])
def validate_chain():
    valid = blockchain.is_chain_valid()
    return jsonify({"valid": valid}), 200

if __name__ == '__main__':
    app.run(debug=True)
