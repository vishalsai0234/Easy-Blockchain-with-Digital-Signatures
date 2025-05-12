# Easy Blockchain

This project is a simple implementation of a blockchain in Python. It demonstrates the basic concepts of blockchain technology, including blocks, hashing, and chain integrity.

## Features

- Creation of a blockchain with a genesis block
- Adding new blocks to the chain
- Calculation of SHA-256 hashes for each block
- Validation of the blockchain's integrity
- Simple demonstration of chain tampering detection

## Requirements

- Python 3.6+

No additional libraries are required as this project only uses Python's standard libraries (`hashlib` and `time`).

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/simonedimeglio/easy-blockchain.git
   ```
2. Navigate to the project directory:
   ```
   cd easy-blockchain
   ```

## Usage

Run the script using Python:

```
python simple_blockchain.py
```

This will create a blockchain, add some sample blocks, print the blockchain, and demonstrate the validation process.

## Understanding the Code

### Block Class

The `Block` class represents a single block in the blockchain. Each block contains:

- `index`: A unique identifier for the block's position in the chain
- `previous_hash`: The hash of the previous block, creating the chain link
- `data`: The data stored in the block (e.g., transaction details)
- `timestamp`: The time when the block was created
- `hash`: A SHA-256 hash of the block's contents

### Blockchain Class

The `Blockchain` class manages the entire chain of blocks. It includes methods to:

- Create the genesis block (the first block in the chain)
- Add new blocks to the chain
- Validate the integrity of the entire chain

### Key Concepts Demonstrated

1. **Hashing**: Each block's hash is created from its contents, ensuring data integrity.
2. **Chaining**: Each block references the previous block's hash, creating a tamper-evident chain.
3. **Validation**: The `is_chain_valid()` method checks the integrity of the entire blockchain.

## Extending the Project

This simple implementation can be extended in several ways:

1. Implement a proof-of-work system
2. Add digital signatures for transactions
3. Create a decentralized network of nodes
4. Implement a consensus mechanism

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

Simone Di Meglio

- GitHub: [@simonedimeglio](https://github.com/simonedimeglio)
