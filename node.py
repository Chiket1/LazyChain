import requests

# Регістрація ноди на сервері
def register_node():
    server_url = 'http://your-server-url.com/register'  # Заміни на реальний URL сервера
    node_data = {
        'ip': '127.0.0.1',  # IP-адреса ноди
        'port': 5000        # Порт, на якому працює нода
    }

    try:
        response = requests.post(server_url, json=node_data)
        if response.status_code == 201:
            print("Node successfully registered:", response.json())
        else:
            print("Failed to register node:", response.status_code, response.text)
    except Exception as e:
        print("Error connecting to the server:", str(e))

# Майнімо блок на ноді
def mine_block():
    server_url = 'http://your-server-url.com/mine'  # Заміни на реальний URL
    try:
        response = requests.post(server_url)
        if response.status_code == 200:
            print("Block mined successfully!")
        else:
            print("Failed to mine block:", response.status_code, response.text)
    except Exception as e:
        print("Error connecting to the server:", str(e))

# Синхронізація блоків з іншими нодами
def sync_blocks(nodes):
    for node in nodes:
        try:
            response = requests.get(f'http://{node}/blocks')
            if response.status_code == 200:
                # Якщо є нові блоки, синхронізуємо з поточною нодою
                new_blocks = response.json()['blocks']
                print(f"Synced blocks from {node}.")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to {node}: {e}")

if __name__ == "__main__":
    register_node()
    mine_block()
