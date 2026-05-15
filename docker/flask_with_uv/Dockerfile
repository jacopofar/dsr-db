FROM python:3.14

COPY . /app/

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN uv sync

CMD ["uv","run", "flask", "--app", "main", "run", "--host", "0.0.0.0"]




