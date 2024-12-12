import requests

# URL сервера
server_url = 'http://127.0.0.1:5000'

# Регістрація ноди на сервері
def register_node():
    node_data = {
        'ip': '127.0.0.1',
        'port': 5001
    }
    try:
        response = requests.post(f"{server_url}/register", json=node_data)
        if response.status_code == 201:
            print("Node successfully registered:", response.json())
        else:
            print("Failed to register node:", response.status_code, response.text)
    except Exception as e:
        print("Error connecting to the server:", str(e))

# Майнімо блок
def mine_block():
    try:
        response = requests.post(f"{server_url}/mine")
        if response.status_code == 200:
            print("Block mined successfully!")
            print(response.json())
        else:
            print("Failed to mine block:", response.status_code, response.text)
    except Exception as e:
        print("Error connecting to the server:", str(e))

if __name__ == "__main__":
    register_node()
    mine_block()
