#!/bin/bash

echo "=== Generando Dockerfile ==="
cat > Dockerfile << 'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt
COPY MusicForAll.py .
CMD ["python", "MusicForAll.py"]
EOF

echo "=== Construyendo imagen ==="
docker build -t musicforall .

echo "=== Eliminando contenedor anterior ==="
docker stop samplerunning 2>/dev/null
docker rm samplerunning 2>/dev/null

echo "=== Ejecutando contenedor ==="
docker run --name samplerunning -e LASTFM_API_KEY=$LASTFM_API_KEY musicforall
