FROM python:3.10

ENV ACCEPT_EULA=Y

# turns off writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update pip
RUN pip install --upgrade pip

# WORKDIR /aimelia
COPY ./docs/requirements.doc.txt ./requirements.txt
COPY ./docs /docs
COPY mkdocs.yml /mkdocs.yml

EXPOSE 3000

RUN pip install -r ./requirements.txt

CMD ["mkdocs", "serve", "-a", "0.0.0.0:3000"]
