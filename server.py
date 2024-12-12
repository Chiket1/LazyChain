from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Список для зберігання нод
nodes = []

# Список для блоків (тут простий приклад, на реальному блоці буде складніше)
blocks = []

# Реєстрація ноди
@app.route('/register', methods=['POST'])
def register_node():
    node_info = request.get_json()
    nodes.append(node_info)
    return jsonify({"message": "Node registered successfully", "nodes": nodes}), 201

# Отримання списку всіх нод
@app.route('/nodes', methods=['GET'])
def get_nodes():
    return jsonify({"nodes": nodes}), 200

# Винагорода ноди
@app.route('/reward', methods=['POST'])
def reward_node():
    node_id = request.get_json().get('node_id')
    reward_amount = 10  # Приклад винагороди
    return jsonify({"message": f"Node {node_id} rewarded with {reward_amount} tokens"}), 200

# Майнімо блок
@app.route('/mine', methods=['POST'])
def mine_block():
    new_block = {
        'index': len(blocks) + 1,
        'timestamp': time.time(),
        'transactions': [],
        'proof': 100,
        'previous_hash': '1'
    }
    blocks.append(new_block)
    return jsonify({"message": "Block mined successfully", "block": new_block}), 200

# Отримати блоки
@app.route('/blocks', methods=['GET'])
def get_blocks():
    return jsonify({"blocks": blocks}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
