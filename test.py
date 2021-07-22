import hashlib
        
import random

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
                  
            
    def change (self,transactions):
            self.transactions = transactions
            self.block_data = "-".join(transactions) + "-" +  self.pre_block_hash
            self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
chain = []        
first = blockchain("first",["1"])
chain.append(first)
for i in range (10000):
    n =str( random.random())
    second =blockchain(first.block_hash,[n])
    chain.append(second)
    first = second
    
for i in range (0,9999):
    temp = chain[i].block_hash
    flag = chain[i+1].validate(temp)
    if flag == False :
        break
if flag : 
    print("No problem")
else : 
    print("problem detected")

    

chain[776].change(["777"])
print("changin thee 777th block's data...")

problem_at= 0
for i in range (0,9999):
    temp = chain[i].block_hash
    flag = chain[i+1].validate(temp)
    if flag == False :
        problem_at= i
        break
if flag : 
    print("No problem")
else :
    # +1 is because of the start_index 0 in lists
    print("problem detected at {} block".format(problem_at+1))
    





    
        
        
    
    
    
    
