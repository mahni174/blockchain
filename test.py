import hashlib
        
import random
class blockchain:
    
    def __init__(self, pre_block_hash, transactions):
        # records the previous blocks
        self.pre_block_hash = pre_block_hash
        self.transactions = transactions
        
        self.block_data = "-".join(transactions) + "-" +  pre_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
   #def validate(self):
        
first = blockchain("first","1")
for i in range (1,10000):
    n =str( random.random())
    second =blockchain(first.block_hash,[n])
    first = second
    
    
    
