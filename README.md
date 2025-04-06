# NPI

Une API REST pour évaluer des expressions en **notation polonaise inverse (NPI)**, stocker les résultats dans une base de données PostgreSQL, et exporter les données en CSV. Le tout conteneurisé avec Docker.


## Fonctionnalités

- Calculatrice NPI (notation polonaise inverse)
- API REST avec FastAPI
- Base de données PostgreSQL avec SQLAlchemy
- Export CSV des opérations
- Conteneurisation avec Docker & Docker Compose
- Tests unitaires

## Stack technique

- **Python**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Docker / Docker Compose**
- **Pytest** (tests)

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/housseinnajahi/NPI.git
cd NPI
```

### 2. Lancer avec Docker

```bash
docker-compose up --build
```
- **API disponible sur** `http://localhost:8001`
- **Swagger UI** `http://localhost:8001/calculator/docs`


## Exemple d'utilisation

### POST `/api/v1/expressions/calculate/`
```
{
  "expression": ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
}
```

### Réponse

```
{
  "expression": ["5", "1", "2", "+", "4", "*", "+", "3", "-"],
  "result": 14.0
}
```

### Get `/api/v1/expressions/export/`
Télécharge un fichier CSV contenant toutes les opérations.


## Lancer les tests

```
docker exec -it fastapi_app pytest
```
