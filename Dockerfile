FROM python:3.10

ENV ACCEPT_EULA=Y

# turns off writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /aimelia
COPY ./requirements.txt /requirements.txt
COPY ./src /src

EXPOSE 8000

RUN pip install -r requirements.txt

# Debug mode, reloads the server when a file changes
CMD ["uvicorn", "src.main:app", "--reload"]
