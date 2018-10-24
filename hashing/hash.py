import hashlib as hl
from pandas import json
import numpy as npy
from numpy import dtype, block
from datetime import datetime
from numpy.core.defchararray import index
from pandas._libs.sparse import BlockIndex



## trying to use blockchain

startTime = datetime.now()

class Transaction:
    
    def __init__(self,fromAddress,toAddress,amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount

class Blockchain:
    
    def __init__(self):
        self.difficulty = 2 
        self.chain = [self.createGenesisBlock()]
        self.pandingTransactions = []
        self.miningReward = 100
        
    def createGenesisBlock(self):
        gen = Block("Genesis Block")
        gen.previous = "0"
        gen.mineBlock(self.difficulty)
        return gen
    
    def updateBlock(self,blockindex,new_data):
        if(blockindex < 0 or blockindex >= self.index):
            AssertionError
        
        working_block = self.chain[blockindex]
        working_block.data = new_data
        working_block.hash = working_block.mineBlock(self.difficulty)
    
    
#    delete Blcok and re-Calculate all the other Blocks coming after
#     def deleteBlock(self,blockindex):
#         if(blockindex < 0 or blockindex >= len(self.chain)):
#             AssertionError
#          
#         self.chain.pop(blockindex)
# 
#         while(blockindex < len(self.chain)):
#             self.chain[blockindex].index -=1
#             if(blockindex == 0):
#                 self.chain[blockindex].previous = 0
#             else:
#                 self.chain[blockindex].previous =  self.chain[blockindex-1].hash
#                 
#             self.chain[blockindex].mineBlock(self.difficulty)
#     
    def getLatestBlock(self):
        return self.chain[-1]
    
    def minePandingTransactions(self,miningRewardAdress):
        block = Block(self.pandingTransactions)
        block.mineBlock(self.difficulty)
        self.chain.append(block)
        self.pandingTransactions = [Transaction(None,miningRewardAdress,self.miningReward)]
        
    def createTransaction(self,trnsaction):
        self.pandingTransactions.append(trnsaction )
        
    def getBalanceOfAddress(self,address):
        for()
#     def addBlock(self,newBlock):
#         newBlock.previous = self.getLatestBlock().hash
#         newBlock.hash = newBlock.mineBlock(self.difficulty)
#         self.chain.append(newBlock)
        
    def __str__(self):
        for b in self.chain:
            print b
        return '\n'


class Block(Blockchain):
    
    def __init__(self, transaction):
        self.timestamp = datetime.utcnow()
        self.transaction = transaction
        self.previous = Blockchain.getLatestBlock()
        self.nonce = 0
        self.hash = self.calculateHash()
        
    def calculateHash(self):
        self.timestamp = datetime.utcnow()
        cur_hash = hl.sha256();
        cur_hash.update(str(self.index)  + str(self.timestamp) + self.previous + str(self.data) + str(self.nonce))
        return cur_hash.hexdigest()
    
    def mineBlock(self, difficulty):
        
        start_mininig = datetime.now()
        print "Now Mining Block: #",self.index 
        diff_string = '0' * difficulty
        
        while(self.hash[0: difficulty] not in diff_string):
            self.nonce+= 1
            self.hash = self.calculateHash()
        print "Finished Mining Block: #",self.index, "time:", datetime.now() - start_mininig 

            
    def __str__(self):
        print "--------------------------------" 
        print "Block No.", self.index 
        print "Date: " ,self.timestamp 
        print "Data: " , self.data 
        print "P.Hash: " , self.previous 
        print "Hash: " , self.hash 
        print "Nonce: ",self.nonce
        return ' \n'
    

     
        
if __name__ == '__main__':
    bc = Blockchain()

    

    
    
    print bc
    print(datetime.now() - startTime)
    
    bc.deleteBlock(1)
    print bc
    
    