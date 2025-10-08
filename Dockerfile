FROM python:3.13-slim

# Copy source
WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Ensure local package is discoverable
ENV PYTHONPATH=/app

# Set default transport environment variable
ENV TRANSPORT=stdio

# Expose port 8000 for streamable-http transport (FastMCP default)
EXPOSE 8000

CMD python qonto_mcp/server.py --transport $TRANSPORT
