FROM python:3.10

ENV ACCEPT_EULA=Y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY ./src/nodes/data/requirements.txt ./requirements.txt
COPY ./src /src

EXPOSE 8000

RUN pip install -r ./requirements.txt

CMD ["uvicorn", "nodes.data.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]