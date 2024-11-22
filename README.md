# DEVCOMMERCE

## Requirements
- Python: 3.12
- Django: 5.x
- Docker
- Docker Compose
- Stripe

## Steps to follow for installation
1. Clone the repository:
```sh
git clone git@github.com:Waislam/devcommerce.git
cd devcommerce
```
2. Create `.env`
```sh
cp .env.example .env
```
3. Build and start the container
```sh
docker compose up --build
```
4. Accessing Application
```sh
http://localhost:8000/api/
```