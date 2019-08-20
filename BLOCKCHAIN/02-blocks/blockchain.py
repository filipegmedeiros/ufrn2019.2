# -*- coding: utf-8 -*-
import hashlib
import json
import time



class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        

    def createGenesisBlock(self):
        self.createBlock()

    def createBlock(self, nonce=0, previousHash=0):
        # Implemente aqui o método para retornar um bloco (formato de dicionário)
        # Lembre que o hash do bloco anterior é o hash na verdade do CABEÇALHO do bloco anterior.
        if(len(self.chain)==0):
                    newBlock = dict(
                            index=0, 
                            timestamp=(int(time.time())), 
                            nonce=0, 
                            merkleRoot=0, 
                            previousHash= 0,
                            transactions= 0)

        else:
                    newBlock = dict(
                            index=(len(self.chain))+1, 
                            timestamp=(int(time.time())), 
                            nonce=0, 
                            merkleRoot=0, 
                            previousHash= self.generateHash(self.chain[-1]),
                            transactions=self.memPool)
            

        self.chain.append(newBlock)


    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    def printChain(self):
        for i in self.chain:
            print(json.dumps(i, sort_keys=True).encode())

        for i in self.chain:


# Teste
blockchain = Blockchain()
for x in range(0, 3): blockchain.createBlock()
blockchain.printChain()
