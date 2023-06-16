FROM python:3.10.6-alpine

EXPOSE 8000

WORKDIR /code


RUN pip install --upgrade pip
RUN pip install poetry

COPY . /code

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without test

CMD ["poetry", "run", "uvicorn", "fastapi_project.main:app", "--host", "0.0.0.0", "--port", "8000 " ]