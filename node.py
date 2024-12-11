import requests
from blockchain import Blockchain


class Node:
    def __init__(self, address, blockchain):
        self.address = address  # Адреса ноди (можна використовувати IP:PORT)
        self.blockchain = blockchain  # Підключення до блокчейну
        self.nodes = set()  # Список інших нод у мережі

    def register_node(self, node_address):
        """Реєстрація іншої ноди в мережі"""
        self.nodes.add(node_address)
        print(f"Нода {node_address} зареєстрована у мережі.")

    def sync_blocks(self):
        """Синхронізація блоків з іншими нодами"""
        for node in self.nodes:
            try:
                response = requests.get(f'http://{node}/blocks')
                if response.status_code == 200:
                    # Якщо є нові блоки, синхронізуємо з поточною нодою
                    new_blocks = response.json()['blocks']
                    self.blockchain.chain = new_blocks
                    print(f"Синхронізовано блоки з нодою {node}.")
            except requests.exceptions.RequestException as e:
                print(f"Помилка при підключенні до {node}: {e}")

    def add_transaction(self, sender, recipient, amount):
        """Додавання транзакції через API"""
        self.blockchain.add_transaction(sender, recipient, amount)

    def mine_block(self):
        """Майнінг блоку на цій ноді"""
        if self.blockchain.add_block():
            print("Блок успішно додано.")
        else:
            print("Не вдалося додати блок.")

