FROM python:3.13-slim

# Copy source
WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Ensure local package is discoverable
ENV PYTHONPATH=/app

CMD ["python", "qonto_mcp/server.py"]
