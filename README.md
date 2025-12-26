# Scalable Document Tagging with Elasticsearch on AWS

## Overview

This project implements a scalable document tagging and search system using **Flask**, **TF-IDF based NLP**, **Elasticsearch**, and **Docker**.

Users can upload unstructured text documents, automatically generate topic tags, index them in Elasticsearch, and perform fast full-text search across documents.

The application is containerized using Docker and orchestrated with Docker Compose, making it easy to run locally or deploy on AWS EC2.

---

## Features

- REST API built using Flask  
- Automatic document tagging using TF-IDF  
- Fast indexing and search using Elasticsearch 8.x  
- Full-text search across title, content, and tags  
- Dockerized services with Docker Compose  
- Robust error handling and service health checks  

---

## Tech Stack

- Python  
- Flask  
- scikit-learn (TF-IDF)  
- Elasticsearch 8.x  
- Docker  
- Docker Compose  
- AWS EC2  

---

## API Endpoints

### Upload Document
Uploads a document, generates tags using TF-IDF, and indexes it in Elasticsearch.

```http
POST /upload
```

#### Request Body
```json
{
  "title": "Test Doc",
  "content": "This is a test document for tagging."
}
```

#### Response
```json
{
  "message": "Document indexed successfully",
  "tags": ["document", "tagging", "test"]
}
```

---

### Search Documents
Searches documents based on query across title, content, and tags.

```http
GET /search?query=test
```

#### Response
```json
[
  {
    "title": "Test Doc",
    "content": "This is a test document for tagging.",
    "tags": ["document", "tagging", "test"]
  }
]
```

---

## Running Locally

### Prerequisites
- Docker
- Docker Compose

### Steps
```bash
docker-compose up --build
```

### Access Services
- Flask API: http://localhost:5000
- Elasticsearch: http://localhost:9200

---

## Deployment on AWS EC2

### EC2 Configuration
- Instance Type: `t3.micro`
- OS: Ubuntu 22.04+
- Open inbound ports:
  - `22` → SSH
  - `5000` → Flask API
  - `9200` → Elasticsearch

### Deployment Steps
```bash
sudo apt update
sudo apt install docker docker-compose -y
git clone <your-repo-url>
cd scalable-doc-tagging
docker-compose up -d
```

---

## Screenshots Included
- Docker containers running
- Elasticsearch service health
- Document upload API response
- Search API response
- AWS EC2 instance deployment

---

## Notes
- Elasticsearch runs in single-node mode.
- TF-IDF is used for lightweight topic extraction.
- Can be extended to LDA or transformer-based models.

---

## Author
**Rohit Kumar**  
AI Engineer – Technical Task Submission
