from configs.config import VERSION, OPENAPI_DESC
from fastapi import FastAPI
from api import router as api_router
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware


def get_custom_openapi(app: FastAPI):
    openapi_schema = get_openapi(
        title=f"Aimelia",
        version=VERSION,
        summary=f"PredX x Aimelia Proof of Concept",
        description=OPENAPI_DESC,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://whitepaper.aimelia.network/~gitbook/image?url=https%3A%2F%2F516989656-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCCzRRAwggtrnfKBiYaGq%252Fuploads%252FW8fpToe2OpxJbE7zdXps%252FScreenshot%25202024-05-04%2520at%252012.22.55%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Deb2af258-d015-4c7f-9981-03a89f3e1027&width=1248&dpr=1&quality=100&sign=e164f643a8f454f59abc1b647429411faf0866c4af5b5c30452bd098d67da177"
    }
    return openapi_schema


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.openapi_schema = get_custom_openapi(app)
