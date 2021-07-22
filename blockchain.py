import hashlib

class blockchain:
    
    def __init__(self, pre_block_hash, transactions):
        # records the previous blocks
        self.pre_block_hash = pre_block_hash
        self.transactions = transactions
        
        self.block_data = "-".join(transactions) + "-" +  pre_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
    def validate(self,pre_hash):
        new = "-".join(self.transactions) + "-" + pre_hash
        new_hash =  hashlib.sha256(new.encode()).hexdigest()
        if new_hash == self.block_hash:
            return True
        else:
            return False
      
   
 """      
t1 = "A sends 2 to B"
t2 = "B sends 3.1 to C"      
t3 = "B sends 3 to C"     
       
first= blockchain("first",[t1,t2])
print(first.block_data)
print(first.block_hash)
second =blockchain(first.block_hash,[t3])
print(second.block_data)
print()
print(second.pre_block_hash)
print(second.block_hash)
x = second.validate(first.block_hash)
print(x)"""


    
