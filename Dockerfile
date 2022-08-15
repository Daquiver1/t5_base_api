FROM python:3.9.0-slim 

RUN pip install poetry

COPY pyproject.toml /app/

RUN poetry install

COPY ./api /app/api
COPY ./core /app/core
COPY ./schemes /app/schemes
COPY ./main.py /app
COPY ./model/ /app/model

EXPOSE 8080

CMD ["uvicorn", "main:app", "--port", "8080"]
