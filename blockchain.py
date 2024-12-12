import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f'{self.index}{self.previous_hash}{self.transactions}{self.timestamp}'
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.transactions = []

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        self.transactions.append({"sender": sender, "recipient": recipient, "amount": amount})

    def mine_block(self):
        last_block = self.get_last_block()
        new_block = Block(len(self.chain), last_block.hash, self.transactions)
        self.chain.append(new_block)
        self.transactions = []
        return new_block
