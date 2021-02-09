from transaction import Transaction

import hashlib

class Block:
    block_seq_number: int
    previous_hash: str
    miner_signature: bytes
    
    transaction: Transaction

    def __init__(self, seq_number: int, previous_hash: str, transaction: Transaction):
        self.block_seq_number = seq_number
        self.previous_hash = previous_hash

        self.transaction = transaction

    def miner_signature_bytes(self) -> bytes:
        return (str(self.transaction.merchant_signature) + str(self.block_seq_number) + str(self.previous_hash)).encode('utf-8')

    def calculate_hash(self) -> bytes:
        if self.block_seq_number == 0:
            return hashlib.sha256("0000000".encode('utf-8')).digest()
        else:
            return hashlib.sha256((str(self.transaction.customer_public_key) + str(self.transaction.merchant_public_key) + str(self.transaction.date) + str(self.transaction.amount) + str(self.transaction.customer_signature) + str(self.transaction.merchant_signature) + str(self.block_seq_number)).encode('utf-8')).digest()


    def display(self):
        print("---------------------------")
        print("Customer Public Key: " + str(self.transaction.customer_public_key))
        print("Merchant Public Key: " + str(self.transaction.merchant_public_key))
        print("Date: " + str(self.transaction.date))
        print("Amount: " + str(self.transaction.amount))
        print("---------------------------")