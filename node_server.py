from flask import Flask, jsonify, request
from node import Node  # Імпортуємо клас Node з існуючого node.py
from blockchain import Blockchain  # Імпортуємо ваш клас Blockchain

# Ініціалізація блокчейну та ноди
blockchain = Blockchain()
node_address = "localhost:5000"  # Встановіть адресу вашої ноди
node = Node(node_address, blockchain)

app = Flask(__name__)

@app.route('/blocks', methods=['GET'])
def get_blocks():
    """Отримати всі блоки в блокчейні."""
    return jsonify({'blocks': blockchain.chain}), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Додати нову транзакцію."""
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    blockchain.add_transaction(values['sender'], values['recipient'], values['amount'])
    return 'Transaction added', 201

@app.route('/mine', methods=['GET'])
def mine():
    """Майнінг нового блоку."""
    if blockchain.add_block():
        return 'Block mined and added to the chain', 201
    return 'Mining failed', 500

@app.route('/nodes/register', methods=['POST'])
def register_node():
    """Реєстрація нової ноди."""
    values = request.get_json()
    node_address = values.get('node_address')
    if node_address is None:
        return "Error: Please supply a valid node address", 400

    node.register_node(node_address)
    return f"Node {node_address} registered successfully", 201

@app.route('/nodes/sync', methods=['GET'])
def sync_blocks():
    """Синхронізація блоків з іншими нодами."""
    node.sync_blocks()
    return "Blockchain synchronized with other nodes", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
