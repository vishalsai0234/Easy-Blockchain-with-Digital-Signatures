import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        """
        Initialize a new Block in the blockchain.
        
        :param index: Unique identifier of the block in the chain
        :param previous_hash: Hash of the previous block in the chain
        :param data: Data stored in the block (could be transactions, messages, etc.)
        :param timestamp: Time when the block was created (default: current time)
        """
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block using SHA-256.
        
        The hash is created using the block's index, previous hash, data, and timestamp.
        This ensures that any change in these values will result in a different hash.
        
        :return: A string representing the hexadecimal digest of the hash
        """
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (genesis block).
        
        :return: A Block object representing the genesis block
        """
        return Block(0, "0", "Genesis Block", time.time())

    def get_latest_block(self):
        """
        Get the most recent block in the blockchain.
        
        :return: The last Block object in the chain
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the blockchain.
        
        This method sets the previous_hash of the new block to the hash of the latest block,
        recalculates the new block's hash, and appends it to the chain.
        
        :param new_block: The Block object to be added to the chain
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the integrity of the blockchain.
        
        This method checks if each block's previous_hash matches the hash of the actual previous block,
        and if each block's hash is correctly calculated.
        
        :return: Boolean indicating whether the chain is valid
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if the current block's hash is correctly calculated
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {i} has an invalid hash")
                return False
            
            # Check if the current block's previous_hash matches the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {i} has an invalid previous hash")
                return False
        
        return True

# Test the blockchain
if __name__ == "__main__":
    # Create a new blockchain
    my_blockchain = Blockchain()

    # Add some blocks to the chain
    my_blockchain.add_block(Block(1, "", "First Transaction: Alice sends 1 BTC to Bob"))
    my_blockchain.add_block(Block(2, "", "Second Transaction: Bob sends 0.5 BTC to Charlie"))
    my_blockchain.add_block(Block(3, "", "Third Transaction: Charlie sends 0.2 BTC to David"))

    # Print out the blockchain
    for block in my_blockchain.chain:
        print(f"Block #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print("--------------")

    # Validate the blockchain
    print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")

    # Try to tamper with the blockchain
    my_blockchain.chain[1].data = "Tampered Transaction: Alice sends 100 BTC to Eve"
    print(f"Is blockchain valid after tampering? {my_blockchain.is_chain_valid()}")