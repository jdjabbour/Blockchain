#####################################################################################################
# This is a very simple blockchain application that takes the hash from the previous block
# and rehashes it to create a chain
# You can see this coded live via: https://www.youtube.com/watch?v=p4lw8CuQtq8
# While in JS, this article helps explain Blockchain a little further: 
# https://dev.to/damcosset/blockchain-what-is-in-a-block-48jo
####################################################################################################

import hashlib
import datetime

class Block:
    def __init__(self, previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()
    
    
    @staticmethod  # Decorators  w00w
    def create_genesis_block():
        '''
        This creates the "seed" for the chain.  As we can see the initial hash is two zeros and the date
        '''
        return Block("0", "0", datetime.datetime.now())

    def get_hash(self):
        '''
        This is called once the chain has been started.  It takes the previous hash and adds to it to create a new hash.
        From here you can create the inner has and outerhash since eash hash runs through twice.
        The outer hash is what is returned and collected in the next block of the chain.
        '''
        header_bin = (str(self.previous_block_hash) + str(self.data) + str(self.timestamp)).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash