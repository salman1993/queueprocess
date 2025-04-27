FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
WORKDIR /code
COPY . /code

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# Place executables in the environment at the front of the path
ENV PATH="/code/.venv/bin:$PATH"

# Command will be overridden by docker-compose.yml (uvicorn or worker)