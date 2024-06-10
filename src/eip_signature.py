import os
import time
from typing import Optional

from eth_account import Account
from eth_account.messages import encode_structured_data
from dotenv import load_dotenv


load_dotenv()


def get_l1_header(verbose: Optional[bool] = False):
    # Replace with your actual Polygon private key
    private_key = os.getenv("PK")

    account = Account.from_key(private_key)

    # Replace with your actual data
    POLY_NONCE = 0  # Example nonce, increment as needed
    POLY_TIMESTAMP = int(time.time())

    # Define the EIP-712 domain
    domain = {
        "name": "Polymarket",
        "version": "1",
        "chainId": 137,  # Polygon chain ID
    }

    # Define the EIP-712 types
    types = {
        "EIP712Domain": [
            {"name": "name", "type": "string"},
            {"name": "version", "type": "string"},
            {"name": "chainId", "type": "uint256"},
        ],
        "Auth": [
            {"name": "address", "type": "address"},
            {"name": "nonce", "type": "uint256"},
            {"name": "timestamp", "type": "uint256"},
        ],
    }

    # Define the message
    message = {
        "address": account.address,
        "nonce": POLY_NONCE,
        "timestamp": POLY_TIMESTAMP,
    }

    # Encode the structured data
    data = {"domain": domain, "types": types, "primaryType": "Auth", "message": message}
    encoded_data = encode_structured_data(data)

    # Sign the message
    signed_message = account.sign_message(encoded_data)
    signature = signed_message.signature.hex()

    if verbose:
        print("POLY_ADDRESS:", account.address)
        print("POLY_SIGNATURE:", signature)
        print("POLY_TIMESTAMP:", POLY_TIMESTAMP)
        print("POLY_NONCE:", POLY_NONCE)

    return {
        "POLY_ADDRESS": account.address,
        "POLY_SIGNATURE": signature,
        "POLY_TIMESTAMP": POLY_TIMESTAMP,
        "POLY_NONCE": POLY_NONCE,
    }


if __name__ == "__main__":
    get_l1_header(verbose=True)
else:
    pass
