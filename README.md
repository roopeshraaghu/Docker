# Docker Flask Application

A simple Flask application containerized using Docker and Docker Compose.

## Technologies Used

- Python Flask
- Docker
- Docker Compose
- Redis
---

## Run Locally

### Clone Repository

```bash
git clone https://github.com/yourusername/docker-flask-app.git

cd docker-flask-app
```

### Build Docker Image

```bash
docker build -t flask-docker-app .
```

### Run Container

```bash
docker run -d -p 5000:5000 flask-docker-app
```

Open:

http://localhost:5000

---

## Docker Compose

### Start Services

```bash
docker compose up -d
```

### Stop Services

```bash
docker compose down
```

---

## Docker Hub

### Pull Image

```bash
docker pull yourdockerhubusername/flask-docker-app:v1
```
## Application Architecture

The application consists of:

- Flask Web Application
- Redis Cache
- PostgreSQL Database

Docker Compose manages all services together.

### Services

| Service | Purpose |
|---|---|
| web | Flask application |
| redis | Visitor counter cache |
| db | PostgreSQL database |

---

## Start Application

```bash
docker compose up -d
```

---

## Stop Application

```bash
docker compose down
```

---

## Access PostgreSQL

```bash
docker exec -it postgres-db psql -U postgres -d flaskdb
