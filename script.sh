#!/bin/bash
set -e
set -u

echo "Starting deployment script..."

cd /home/devxhub || { echo "Directory not found"; exit 1; }

echo "Stopping and removing existing containers..."
docker compose down

echo "Building and starting containers..."
docker compose up -d --build

echo "Checking container status..."
docker compose ps

echo "Deployment script finished successfully."
