FROM python:3.10-slim

# turns off writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copying requirments.txt to the container
COPY ./requirements.txt /requirements.txt

# Installing the py dependencies
RUN pip install -r requirements.txt
# Documentation dependencies
RUN pip install mkdocs mkdocs-material

# Setting workdir
WORKDIR /aimelia

# Copying the source code to the container
COPY ./aimelia .

# Listing the files in the container
RUN ls -al

# Running the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--log-level", "debug"]