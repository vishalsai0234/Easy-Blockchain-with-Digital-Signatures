from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import json

# Load private key
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Transaction data
transaction = {
    "sender": "Alice",
    "recipient": "Bob",
    "amount": 50
}
message = json.dumps(transaction, sort_keys=True).encode()

# Sign the message
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Include the signature
transaction["signature"] = signature.hex()

# Save to file
with open("signed_transaction.json", "w") as f:
    json.dump(transaction, f, indent=2)

print(json.dumps(transaction, indent=2))
