# -*- coding: utf-8 -*-
import hashlib
import json
import time


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = [ ]

        self.hashs = []        
        self.createGenesisBlock()


    def createGenesisBlock(self):
        self.createBlock()

    def createBlock(self, nonce=0, previousHash=0):
        # Lembre que o hash do bloco anterior é o hash na verdade do CABEÇALHO do bloco anterior.

        
        if(len(self.chain)==0):

            #pool = self.memPool.copy()
            #self.memPool.clear()

            Block = dict(
            index=0,
            timestamp=(int(time.time())),
            nonce=0,
            merkleRoot=0,
            previousHash=0,
            transactions=self.memPool)
        else:
            header = self.chain[-1].copy()
            header.pop("transactions")
            previousHash2 = dict(index=(len(self.chain)-1), hash = self.generateHash(header))
            previousHash = self.generateHash(header)
            self.hashs.append(previousHash2)

            pool = self.memPool.copy()
            self.memPool.clear()

            Block = dict(
            index=(len(self.chain)),
            timestamp=(int(time.time())),
            nonce=0,
            merkleRoot=0,
            previousHash= previousHash,
            transactions=pool)

        self.chain.append(Block)



    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    def printChain(self):
        for i in self.hashs:
            print(json.dumps(i,indent = 4, sort_keys=True ))            
        for i in self.chain:
            print(json.dumps(i,indent = 4, sort_keys=True ))



blockchain = Blockchain()



for x in range(1, 6):
    blockchain.createBlock()
blockchain.printChain()