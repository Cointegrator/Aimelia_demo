FROM python:3.10

ENV ACCEPT_EULA=Y

# turns off writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /dataNode
COPY ./requirements.txt ./requirements.txt
COPY ./multinode/data .

EXPOSE 8000

RUN pip install -r requirements.txt

# Debug mode, reloads the server when a file changes
CMD ["uvicorn", "app:app", "--reload", "--port", "8000", "--host", "0.0.0.0"]

