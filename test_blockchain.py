from blockchain import Blockchain, Block

# Створюємо блокчейн
blockchain = Blockchain()

# Додаємо нову транзакцію
blockchain.add_transaction("user1", "user2", 100)

# Створюємо новий блок і додаємо його в ланцюг
new_block = Block(1, blockchain.get_last_block().hash, blockchain.transactions)
blockchain.add_block(new_block)

# Перевіряємо новий блок
for block in blockchain.chain:
    print(f"Block #{block.index} Hash: {block.hash}")
