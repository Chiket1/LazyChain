from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

# Створюємо блокчейн
my_blockchain = Blockchain()
nodes = set()  # Список нод, зареєстрованих в мережі

@app.route('/blocks', methods=['GET'])
def get_blocks():
    """Отримати всі блоки з цієї ноди"""
    blocks = []
    for block in my_blockchain.chain:
        blocks.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'transactions': block.transactions,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        })
    return jsonify({'blocks': blocks})

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    """Додавання нової транзакції"""
    data = request.get_json()
    my_blockchain.add_transaction(data['sender'], data['recipient'], data['amount'])
    return jsonify({"message": "Транзакцію додано."})

@app.route('/mine', methods=['GET'])
def mine():
    """Майнінг нового блоку з Proof of Work"""
    new_block = my_blockchain.mine_block()
    return jsonify({
        "message": "Блок видобуто.",
        "block": {
            'index': new_block.index,
            'timestamp': new_block.timestamp,
            'transactions': new_block.transactions,
            'previous_hash': new_block.previous_hash,
            'hash': new_block.hash
        }
    })

@app.route('/register_node', methods=['POST'])
def register_node():
    """Реєстрація нової ноди в мережі"""
    data = request.get_json()
    node_address = data.get('node_address')
    if node_address:
        nodes.add(node_address)
        return jsonify({"message": f"Нода {node_address} зареєстрована."})
    return jsonify({"message": "Адреса ноди не надана."}), 400

@app.route('/validate_chain', methods=['GET'])
def validate_chain():
    """Перевірка валідності ланцюга"""
    is_valid = my_blockchain.is_valid()
    if is_valid:
        return jsonify({"message": "Ланцюг дійсний."})
    else:
        return jsonify({"message": "Ланцюг пошкоджено."}), 400

@app.route('/sync_chain', methods=['POST'])
def sync_chain():
    """Синхронізація ланцюга між вузлами"""
    data = request.get_json()
    node_chain = data.get('chain')

    if node_chain and len(node_chain) > len(my_blockchain.chain):
        my_blockchain.chain = node_chain
        return jsonify({"message": "Ланцюг синхронізовано."})
    return jsonify({"message": "Новий ланцюг не знайдений."}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
