FROM python:3.13-slim-bookworm AS base

# install pdm dependencies
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

FROM base AS build
WORKDIR /app
COPY . /app
RUN uv sync
RUN uv build

FROM python:3.13-alpine AS deployment

# Install build dependencies temporarily
RUN apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    python3-dev \
    curl

RUN addgroup -S nonroot \
    && adduser -S nonroot -G nonroot
WORKDIR /app
COPY --from=build /app/dist/*.whl .
RUN mkdir -p /app/logs && \
    chown -R nonroot:nonroot /app
RUN chown -R nonroot /app/*whl
USER nonroot
RUN pip install *.whl --no-cache-dir --prefer-binary
ENV PATH="/home/nonroot/.local/bin:$PATH"
WORKDIR /home/nonroot/.local/lib/python3.13/site-packages/

COPY src/manage.py .
RUN pip install granian
EXPOSE 8000 50051
CMD ["python", "-m", "granian", "--host", "0.0.0.0", "--interface", "wsgi", "greeting_services.wsgi:application"]
