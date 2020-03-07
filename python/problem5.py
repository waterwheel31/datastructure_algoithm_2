

import hashlib
import datetime as dt


class Block:

    def __init__(self, index, timestamp, data, previous_hash, block_hash):
      self.index = index
      self.timestamp = str(timestamp)
      self.data = str(data)
      self.previous_hash = str(previous_hash)
      self.hash = block_hash
    
    def calc_hash(self, raw_data):
      sha = hashlib.sha256()

      hash_str = raw_data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()



class BlockChain:
    
    def __init__(self):
        
        data = None
        prev_hash = None
        
        gen_hash = self.calc_hash( str(dt.datetime.now()) + str(data) + str(prev_hash))
        self.gen_block = Block(0, dt.datetime.now(), data, prev_hash , gen_hash )
        self.block_length = 1
        self.last_block = self.gen_block
        self.block_map = dict()
        self.block_map[gen_hash] = self.gen_block
        
        
    def add_block(self, data):
        
        block_hash = self.calc_hash(str(dt.datetime.now()) + str(data) + str(self.last_block.hash))
        new_block = Block(self.block_length, dt.datetime.now(), data, self.last_block.hash, block_hash )
        
        self.last_block = new_block
        self.block_map[block_hash] = new_block
        
        self.block_length += 1
    
    def retrive_by_index(self, index):
         
        if index not in range(self.block_length):
            return 'index {} is out of range'.format(index)
        
        else:    
            block = self.last_block
            i = self.block_length
            while(i>0):
                if block.index == index:
                    
                    data = {'index': block.index, 'timestamp': block.timestamp, 'data': block.data, 'block hash' : block.hash, 'previous hash': block.previous_hash}
                    
                    return data
                
                else:
                    block = self.retrive_by_hash(block.previous_hash)
   
                i -= 1
    
    def retrive_by_hash(self, block_hash):
        
        block = self.block_map[block_hash]
        
        return block
        
    def calc_hash(self, raw_data):
        sha = hashlib.sha256()
        hash_str = raw_data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


bc = BlockChain()

bc.add_block('block1')
bc.add_block('block2')
bc.add_block('block3')

print(bc.retrive_by_index(4))
print(bc.retrive_by_index(1))
print(bc.retrive_by_index(0))