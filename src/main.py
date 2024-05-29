from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.api import router as api_router


app = FastAPI()

description = """
To have a complete pipeline of Aimelia.network, we need to have four different nodes connected, namely

* **Task node**
* **Inference node**
* **Validation node**
* **Data node**

They serve creators, players, and validators. Each node can be a centralized server or a decentralized AI blockchain that provides a specific type of service. 

To let the nodes communicate,  a tailored communication protocol is neccessary to support messaging and resource scheduling between nodes. The content encoded in the communication protocol might be different due to the source and target nodes, however, needs to mark down the stage of the system as well as the expected outcome in the payload. 

Due to the advance of a large language model and high-performance blockchain, messaging passing cross-chain is possible to be written in plain language with proper implementation (considering the maximum transmission unit of each chain) and highly explainable to humans and AI agents. 
"""

app.include_router(api_router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="PredX x Aimelia",
        version="0.0.1",
        summary="PredX x Aimelia Proof of Concept",
        # description="**Aimelia** is a decentralized AI platform that enables users to create, share, and monetize AI models. PredX is a prediction market platform that allows users to create, share, and monetize prediction markets. This project is a proof of concept that combines the two platforms to create a decentralized prediction market platform that leverages AI models to make better predictions.",
        description=description,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://whitepaper.aimelia.network/~gitbook/image?url=https%3A%2F%2F516989656-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCCzRRAwggtrnfKBiYaGq%252Fuploads%252FW8fpToe2OpxJbE7zdXps%252FScreenshot%25202024-05-04%2520at%252012.22.55%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Deb2af258-d015-4c7f-9981-03a89f3e1027&width=1248&dpr=1&quality=100&sign=e164f643a8f454f59abc1b647429411faf0866c4af5b5c30452bd098d67da177"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi