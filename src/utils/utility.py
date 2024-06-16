import inspect
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from config import configs


def log(message: str) -> None:
    stack = inspect.stack()

    the_class = stack[1][0].f_locals["self"].__class__.__name__
    the_method = stack[1][0].f_code.co_name

    print(f"[{the_class}].[{the_method}] {message}")


def get_custom_openapi(node: str, app: FastAPI):
    openapi_schema = get_openapi(
        title=f"Aimelia - {node.capitalize()} Node",
        version=configs.VERSION,
        summary=f"PredX x Aimelia Proof of Concept :: {node.capitalize()} Node",
        description=configs.OPENAPI_DESC,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://whitepaper.aimelia.network/~gitbook/image?url=https%3A%2F%2F516989656-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCCzRRAwggtrnfKBiYaGq%252Fuploads%252FW8fpToe2OpxJbE7zdXps%252FScreenshot%25202024-05-04%2520at%252012.22.55%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Deb2af258-d015-4c7f-9981-03a89f3e1027&width=1248&dpr=1&quality=100&sign=e164f643a8f454f59abc1b647429411faf0866c4af5b5c30452bd098d67da177"
    }
    # app.openapi_schema = openapi_schema
    # return app.openapi_schema
    return openapi_schema
