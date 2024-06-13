# Create API Key
from dotenv import load_dotenv
import os

from py_clob_client.client import ClobClient, ApiCreds
from py_clob_client.constants import POLYGON, AMOY

load_dotenv()


def get_api_key() -> ApiCreds:
    host = "https://clob-staging.polymarket.com/"
    key = os.getenv("PK")
    chain_id = AMOY
    client = ClobClient(host, key=key, chain_id=chain_id)
    creds = None
    try:
        creds = client.create_api_key()
    except Exception:
        creds = client.derive_api_key()
    return creds


def main():
    creds = get_api_key()
    print(creds)


if __name__ == "__main__":
    main()
else:
    pass
