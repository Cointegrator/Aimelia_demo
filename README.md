<img src="https://whitepaper.aimelia.network/~gitbook/image?url=https%3A%2F%2F516989656-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCCzRRAwggtrnfKBiYaGq%252Fuploads%252FW8fpToe2OpxJbE7zdXps%252FScreenshot%25202024-05-04%2520at%252012.22.55%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Deb2af258-d015-4c7f-9981-03a89f3e1027&width=1248&dpr=1&quality=100&sign=e164f643a8f454f59abc1b647429411faf0866c4af5b5c30452bd098d67da177" width="200" height="200" />

# PredX x Aimelia POC

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A truly RESTful service showcasing the true capability of Aimelia

## Usage

This project utilizes Docker to the fullest, so getting started with the project is as simple as

**Docker**

```bash
docker-compose up --build
```

**Manually**

If we're running the project locally we'd have to install the required dependencies first

```bash
# Installing the dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Starting the FastAPI server in development mode**

```bash
uvicorn src.main:app --reload
```

**Starting the server in Production mode**

```bash
gunicorn -w 1 --threads 4 --worker_class uvicorn.worker.UvicornWorker --bind :8000
```

## Testing the project

This project uses `pytest` and `pytest-cov` for unit testing various component of the project, you can run the tests locally using the following commands

```bash
# Installing the dependencies
python -m venv dev_venv
source venv/bin/activate
pip install -r requirements.dev.txt
```

**Running the tests**

```bash
pytest -v --cov
```

## Contribution

## Change log
