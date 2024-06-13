FROM python:3.10

ENV ACCEPT_EULA=Y

# turns off writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /inferenceNode
COPY ./requirements.txt ./requirements.txt
COPY ./multinode/inference .

EXPOSE 8001

RUN pip install -r requirements.txt

# Debug mode, reloads the server when a file changes
CMD ["uvicorn", "app:app", "--reload", "--port", "8001", "--host", "0.0.0.0"]

