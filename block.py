#####################################################################################################
# This is a very simple blockchain application that takes the hash from the previous block
# and rehashes it to create a new hash in a chain
# You can see this coded live via: https://www.youtube.com/watch?v=p4lw8CuQtq8
####################################################################################################

from bc_app import Block
import datetime

# This imports the creation of the Genesis hash which is the seed that starts the chain

block_chain = [Block.create_genesis_block()]
print("The genesis block has been created!")
print("Hash: {}".format(block_chain[-1].hash))

num_blocks_to_add = 10  # This sets the amount of blocks within the chain


for i in range(1, num_blocks_to_add + 1):  # Starts at 1 and goes for the range of num_blocks plus 1 to make it 10
    block_chain.append(Block(block_chain[-1].hash, "DATA", datetime.datetime.now()))  # Adds to the block_chain list

    print("Block {} has been created.".format(i))
    print("Block {} hash: {}".format(i, block_chain[i].hash))
