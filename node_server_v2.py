from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

# Створення нового блокчейну
my_blockchain = Blockchain()
nodes = set()

# API для майнінгу
@app.route('/mine_new', methods=['GET'])
def mine_new():
    """Майнінг нового блоку з Proof of Work"""
    new_block = my_blockchain.mine_block()
    return jsonify({
        "message": "Новый блок найден.",
        "block": {
            'index': new_block.index,
            'timestamp': new_block.timestamp,
            'transactions': new_block.transactions,
            'previous_hash': new_block.previous_hash,
            'hash': new_block.hash
        }
    })

# Запуск серверу
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Запуск на іншому порту
