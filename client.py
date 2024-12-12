import requests

server_url = 'http://127.0.0.1:5000'

# Додавання транзакції
def add_transaction(sender, recipient, amount):
    transaction_data = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    try:
        response = requests.post(f'{server_url}/transactions/new', json=transaction_data)
        if response.status_code == 201:
            print(f"Transaction added: {sender} -> {recipient} amount: {amount}")
        else:
            print(f"Failed to add transaction: {response.status_code}")
    except Exception as e:
        print(f"Error adding transaction: {str(e)}")

# Майнінг блоку
def mine_block():
    try:
        response = requests.post(f'{server_url}/mine')
        if response.status_code == 200:
            print("Block mined successfully!")
        else:
            print(f"Failed to mine block: {response.status_code}")
    except Exception as e:
        print(f"Error mining block: {str(e)}")

# Отримання блоків
def get_blocks():
    try:
        response = requests.get(f'{server_url}/blocks')
        if response.status_code == 200:
            print(f"Blocks: {response.json()}")
        else:
            print(f"Failed to get blocks: {response.status_code}")
    except Exception as e:
        print(f"Error getting blocks: {str(e)}")

if __name__ == "__main__":
    # Приклад використання функцій
    add_transaction('Alice', 'Bob', 100)  # Додавання транзакції
    mine_block()  # Майнінг блоку
    get_blocks()  # Отримання блоків
