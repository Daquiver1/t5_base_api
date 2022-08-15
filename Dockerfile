FROM python:3.9.0-slim 

# System dependenices
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /app/

RUN poetry export --output requirements.txt --without-hashes
RUN pip install -r requirements.txt

# Creating folders and files for project
#COPY ./model/ /app/model
COPY ./api /app/api
COPY ./core /app/core
COPY ./schemes /app/schemes
COPY ./main.py /app

# Exposing port
EXPOSE 8080

# Running project
CMD ["uvicorn", "main:app", "--port", "8080"]
