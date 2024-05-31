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
