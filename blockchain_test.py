import requests

BASE_URL = "http://127.0.0.1:5000"

def test_add_transaction():
    transaction_data = {
        "sender": "user1",
        "recipient": "user2",
        "amount": 50
    }
    response = requests.post(f"{BASE_URL}/add_transaction", json=transaction_data)
    assert response.status_code == 200, f"Failed to add transaction: {response.text}"
    print("Transaction added successfully:", response.json())

def test_mine_block():
    response = requests.get(f"{BASE_URL}/mine")
    assert response.status_code == 200, f"Failed to mine block: {response.text}"
    print("Block mined successfully:", response.json())

def test_get_blocks():
    response = requests.get(f"{BASE_URL}/blocks")
    assert response.status_code == 200, f"Failed to get blocks: {response.text}"
    print("Blockchain:", response.json())

def run_tests():
    print("Running tests...")
    test_add_transaction()
    test_mine_block()
    test_get_blocks()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
