# NewsAPI Integration Service

## Project Description
A FastAPI backend service that integrates with NewsAPI to fetch and manage news articles. Features include:
- OAuth2 client credentials authentication
- NewsAPI integration with 5 endpoints
- SQLite database support
- 80%+ test coverage with pytest
- Docker containerization
- Paginated responses
- Filtering by country/source

## Setup Instructions
Prerequisites
Python 3.8+ (You can use pyenv or a similar tool to manage Python versions).

Docker (For containerization).

NewsAPI API Key (Sign up at NewsAPI to get the free API key).
1. Clone repository:
```bash
git clone https://github.com/Milon34/fastapi-newsapp
cd FastAPI-NewsApp
```
Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt

```
##How to Run the Server
```
uvicorn app.main:app --reload
```
##How to run tests
```
pytest tests/test_news.py
pytest -v tests/test_news.py
pytest --cov=app tests/
```
## Test Coverage Report

The following is the current test coverage report:

| File                          | Statements | Missed | Coverage |
|-------------------------------|------------|--------|----------|
| `app/__init__.py`              | 3          | 0      | 100%     |
| `app/auth.py`                  | 21         | 3      | 86%      |
| `app/config.py`                | 11         | 0      | 100%     |
| `app/database.py`              | 13         | 0      | 100%     |
| `app/endpoints/news.py`        | 43         | 7      | 84%      |
| `app/main.py`                  | 11         | 3      | 73%      |
| `app/models.py`                | 9          | 0      | 100%     |
| `app/schemas.py`               | 13         | 0      | 100%     |
| `app/services/news_service.py` | 24         | 0      | 100%     |

**Total Coverage**: 91%

## 🐳 How to Use Docker

This project is fully containerized using **Docker** and **Docker Compose**.

### 🛠️ Prerequisites

If Docker is not installed on your system, please install:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

### 📁 Docker Files

- `Dockerfile`: Defines the application image.
- `docker-compose.yml`: Orchestrates the services (API, Database, etc.).

---

### 🚀 Build and Run the App

```bash
cd fastapi-newsapp
# Build the Docker containers
docker-compose build
# Run the containers
docker-compose up
#service check
docker-compose ps
```

##How to Generate Access Tokens and Use Secured Endpoints

You can generate access tokens by hitting the /tokens endpoint in your FastAPI application.

- Open the Swagger UI for your FastAPI application. It is usually available at http://localhost:8000/docs (or another port if you have configured it differently).

- In the Swagger UI, find the /tokens endpoint.

- Click on the POST method for /tokens.

- Provide the required credentials (such as client ID and client secret) in the input fields. These credentials will be used to generate the access token.

- Click on the Execute button to generate the token.

- The response will contain the access token which is needed for authenticated requests.

After generating the access token, you need to include it in the request headers to access any secured endpoints.

- In Swagger, you can use the Authorization header to pass the token for subsequent requests.

- For example, when calling the GET /news endpoint:

- Click on the GET method for /news.

- In the Authorization field, add the token in the following format:
```
Bearer <your_access_token>
```
- Alternatively, you can also manually include the token in the header (e.g., using curl, Postman, or in your code).

##API usage examples and descriptions for all 5 endpoints above

### 1. `GET /news`

**Description:**  
Fetch all news with pagination support.

**Query Parameters:**
- `page`: Page number (optional, default = 1)
- `page_size`: Number of articles per page (optional, default = 20)

**Example:**
```bash
curl -X GET "http://localhost:8000/news?page=1&page_size=5" -H "Authorization: Bearer <your_token>"
```
### 2. `POST /news/save-latest`

**Description:**  
Fetch the latest news from NewsAPI and save the top 3 articles into the database.

**Example:**
```bash
curl -X POST "http://localhost:8000/news/save-latest" -H "Authorization: Bearer <your_token>"
```
### 3. `GET /news/headlines/country/{country_code}`

**Description:**  
Fetch top headlines based on a specific country code.

**Path Parameters:**
- `country_code`: Two-letter country code (e.g., us, in, gb)

**Example:**
```bash
curl -X GET "http://localhost:8000/news/headlines/country/us" -H "Authorization: Bearer <your_token>"
```

### 4. `GET /news/headlines/source/{source_id}`

**Description:**  
Fetch top headlines from a specific news source.

**Path Parameters:**
- `source_id`: News source ID (e.g., bbc-news, cnn, abc-news)

**Example:**
```bash
curl -X GET "http://localhost:8000/news/headlines/source/bbc-news" -H "Authorization: Bearer <your_token>"
```
### 5. `GET /news/headlines/filter`

**Description:**  
Filter top headlines by country and source using query parameters.

**Path Parameters:**
- `country`: Country code
- `source`: Source ID

**Example:**
```bash
curl -X GET "http://localhost:8000/news/headlines/filter?country=us&source=cnn" -H "Authorization: Bearer <access_token>"
```