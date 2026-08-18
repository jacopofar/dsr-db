FROM python:3.14

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app

RUN uv sync 

CMD ["uv", "run", "flask", "--app", "hello", "run", "-h", "0.0.0.0"]
