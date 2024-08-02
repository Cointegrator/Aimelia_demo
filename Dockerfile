FROM python:3.10-slim

# turns off writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ACCEPT_EULA=Y
ENV HOST 0.0.0.0
ENV PORT 8000

# Copying requirments.txt to the container
COPY ./requirements.txt /requirements.txt

# Installing the py dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

# Setting workdir
WORKDIR /aimelia

# Copying the source code to the container
COPY ./aimelia .

# Listing the files in the container
RUN ls -al

# Running the app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]
CMD exec uvicorn main:app --host ${HOST} --port ${PORT}
