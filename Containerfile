FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency files first for better build caching
COPY pyproject.toml uv.lock ./

# Install project dependencies
RUN uv sync --locked --no-dev

# Copy application code
COPY app.py ./
COPY data ./data
COPY src ./src

ENV PYTHONPATH=/app/src

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]