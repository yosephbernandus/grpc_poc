FROM python:3.13-slim-bookworm AS base

# install uv dependencies
# RUN python -m pip install uv --no-cache-dir
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

FROM base AS build
WORKDIR /app
COPY . /app
RUN uv sync
RUN uv build

FROM python:3.13-alpine AS deployment
RUN addgroup -S nonroot \
    && adduser -S nonroot -G nonroot
WORKDIR /app
COPY --from=build /app/dist/*.whl .
RUN chown -R nonroot /app/*whl
USER nonroot
RUN pip install *.whl --no-cache-dir --prefer-binary

ENV PATH="/home/nonroot/.local/bin:$PATH"
WORKDIR /home/nonroot/.local/lib/python3.13/site-packages/
COPY src/app .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

