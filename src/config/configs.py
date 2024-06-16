DEBUG: bool = True

BASE: str = "https://clob.polymarket.com"
AUTH_BASE: str = "https://clob-staging.polymarket.com/"
CACHE: bool = True  # Local file based cache

AUTO_BUY: bool = True


VERSION = "0.0.1"
OPENAPI_TITLE = "PredX x AImelia"
OPENAPI_SUMMARY = "PredX x Aimelia Proof of Concept"
OPENAPI_DESC = """
To have a complete pipeline of Aimelia.network, we need to have
four different nodes connected, namely

- **Task node**
- **Inference node**
- **Validation node**
- **Data node**

They serve **creators**, **players**, and **validators**. Each node can be
a centralized server or a decentralized AI blockchain that provides
a specific type of service.

To let the nodes communicate,  a tailored communication protocol
is neccessary to support messaging and resource
scheduling between nodes. The content encoded in the
communication protocol might be different due to the
source and target nodes, however, needs to mark down the
stage of the system as well as the expected outcome in the payload.

Due to the advance of a large language model and high-performance
blockchain, messaging passing cross-chain is possible to be
written in plain language with proper implementation (considering
the maximum transmission unit of each chain) and highly
explainable to humans and AI agents.
"""
