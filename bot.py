import requests
import random
import time
from threading import Thread

# Сервер для реєстрації нод
server_url = 'http://127.0.0.1:5000/register'  # Замінили на правильний URL

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
        response = requests.post(server_url, json=node_data)
        if response.status_code == 201:
            print(f"Node created: {node_data}")
            created_nodes.append(node_data)
        else:
            print(f"Failed to create node: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to server: {str(e)}")


# Функція для симуляції транзакцій
def simulate_transactions():
    while True:
        sender = random.choice(created_nodes)
        recipient = random.choice(created_nodes)
        amount = random.randint(1, 100)

        # Якщо відправник і отримувач однакові, пропустимо
        if sender == recipient:
            continue

        transaction_data = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        # Надсилаємо транзакцію
        try:
            response = requests.post(f'http://{sender["ip"]}:{sender["port"]}/add_transaction', json=transaction_data)
            if response.status_code == 200:
                print(f"Transaction: {sender['ip']} -> {recipient['ip']} amount: {amount}")
            else:
                print(f"Failed to send transaction: {response.status_code}")
        except Exception as e:
            print(f"Error during transaction: {str(e)}")

        time.sleep(random.randint(1, 5))  # Затримка між транзакціями


# Функція для симуляції майнінгу блоків
def mine_blocks():
    while True:
        # Вибираємо випадкову ноду для майнінгу
        node = random.choice(created_nodes)

        try:
            response = requests.post(f'http://{node["ip"]}:{node["port"]}/mine_block')
            if response.status_code == 200:
                print(f"Node {node['ip']} mined a block.")
            else:
                print(f"Failed to mine block: {response.status_code}")
        except Exception as e:
            print(f"Error during mining: {str(e)}")

        time.sleep(random.randint(3, 7))  # Затримка між майнінгом блоків


# Функція для синхронізації блоків
def sync_blocks():
    while True:
        node = random.choice(created_nodes)
        try:
            response = requests.get(f'http://{node["ip"]}:{node["port"]}/sync_blocks')
            if response.status_code == 200:
                print(f"Node {node['ip']} synced its blocks.")
            else:
                print(f"Failed to sync blocks: {response.status_code}")
        except Exception as e:
            print(f"Error during block sync: {str(e)}")

        time.sleep(random.randint(5, 10))  # Затримка між синхронізаціями


# Створюємо кілька нод і запускаємо процеси
def start_bot():
    # Створюємо кілька нод
    for _ in range(5):  # Створюємо 5 нод
        create_node()

    # Запускаємо процеси для симуляції транзакцій, май
