import requests
import random
import time
from threading import Thread

# Сервер для реєстрації нод
server_url = 'http://127.0.0.1:5000'

# Список для зберігання створених акаунтів
created_nodes = []

# Функція для створення акаунтів
def create_node():
    node_ip = f"192.168.0.{random.randint(100, 200)}"
    node_port = random.randint(5000, 6000)
    node_data = {
        'ip': node_ip,
        'port': node_port
    }

    try:
        response = requests.post(f"{server_url}/register", json=node_data)
        if response.status_code == 201:
            print(f"Node created: {node_data}")
            created_nodes.append(node_data)
        else:
            print(f"Failed to create node: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to server: {str(e)}")

# Майнімо блоки
def mine_blocks():
    while True:
        try:
            response = requests.post(f"{server_url}/mine")
            if response.status_code == 200:
                print("Block mined successfully!")
            else:
                print(f"Failed to mine block: {response.status_code}")
        except Exception as e:
            print(f"Error during mining: {str(e)}")

        time.sleep(random.randint(3, 7))  # Затримка між майнінгом блоків

def start_bot():
    # Створюємо 5 нод
    for _ in range(5):
        create_node()

    # Запускаємо майнінг у новому потоці
    Thread(target=mine_blocks).start()

if __name__ == "__main__":
    start_bot()
