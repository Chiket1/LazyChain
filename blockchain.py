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
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.transactions = []
        self.difficulty = difficulty  # Proof of Work difficulty (leading zeros in the hash)

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        self.transactions.append({"sender": sender, "recipient": recipient, "amount": amount})

    def mine_block(self):
        last_block = self.get_last_block()
        new_block = Block(len(self.chain), last_block.hash, self.transactions)

        # Perform Proof of Work
        new_block.hash = self.proof_of_work(new_block)

        self.chain.append(new_block)
        self.transactions = []  # Clear the transaction list
        return new_block

    def proof_of_work(self, block):
        """Proof of Work algorithm"""
        block.hash = block.calculate_hash()
        while not block.hash.startswith('0' * self.difficulty):  # Difficulty level, e.g., 4 leading zeros
            block.timestamp = time.time()  # update timestamp
            block.hash = block.calculate_hash()  # Recalculate hash until it meets the difficulty
        return block.hash

    def is_valid(self):
        """Check the validity of the blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash matches the expected hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous block's hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        """Display the blockchain"""
        for block in self.chain:
            print(f"Index: {block.index}, Hash: {block.hash}, Prev Hash: {block.previous_hash}, Transactions: {block.transactions}")
