#import block
from block import Block
from customer import Customer
from merchant import Merchant
from transaction import Transaction
import datetime
import hashlib

class Blockchain:
    chain: list

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        genesis = Block(0, "0", Transaction(0, 0, "0", 0))
        genesis.transaction.customer_signature = "0"
        genesis.transaction.merchant_signature = "0"
        genesis.miner_signature = "0"
        return genesis

    def create_new_block(self, transaction: Transaction) -> Block:
        return Block(len(self.chain), self.chain[-1].calculate_hash(), transaction)

    def add_block(self, block: Block):
        self.chain.append(block)

    def display(self):
        for block in self.chain:
            block.display()
        print(len(self.chain))

    def increment_fifteen(self):
        self.chain[16].transaction.amount = self.chain[16].transaction.amount + 10.0

    def is_chain_valid(self) -> bool:
        for index, block in enumerate(self.chain[1:]):
            previous_block = self.chain[index]

            if block.previous_hash != previous_block.calculate_hash():
                print("Previous Hash: " + str(block.previous_hash))
                print("Recaclulated Previous Hash: " + str(previous_block.calculate_hash()))
                return False

        return True

    def print_customer_three(self, customer: Customer):
        for block in self.chain:
            if block.transaction.customer_public_key == customer.public_key:
                block.display()

    def print_merchant_two(self, merchant: Merchant):
        for block in self.chain:
            if block.transaction.merchant_public_key == merchant.public_key:
                block.display()