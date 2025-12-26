Scalable Document Tagging with Elasticsearch on AWS
Overview

This project implements a scalable document tagging and search system using Flask, TF-IDF based NLP, Elasticsearch, and Docker.
It allows users to upload unstructured text documents, automatically generate topic tags, index them in Elasticsearch, and perform fast full-text search.

The application is containerized using Docker and orchestrated with Docker Compose, making it easy to deploy locally or on cloud platforms like AWS EC2.

Features

REST API built using Flask

Automatic document tagging using TF-IDF

Fast indexing and search using Elasticsearch 8.x

Full-text search across title, content, and tags

Dockerized services with Docker Compose

Robust error handling and service health checks

Tech Stack

Python

Flask

scikit-learn (TF-IDF)

Elasticsearch 8.x

Docker & Docker Compose

Project Structure
scalable-doc-tagging/
│
├── app.py                 # Flask application
├── elastic.py             # Elasticsearch index setup
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image for Flask app
├── docker-compose.yml     # Service orchestration
└── README.md              # Project documentation

API Endpoints
1. Upload Document

POST /upload

Request Body (JSON):

{
  "title": "AI in Healthcare",
  "content": "Deep learning models are widely used in healthcare."
}


Response:

{
  "message": "Document indexed successfully",
  "tags": ["learning", "healthcare", "models", "deep", "used"]
}

2. Search Documents

GET /search?query=<keyword>

Example:

/search?query=healthcare


Response:

[
  {
    "title": "AI in Healthcare",
    "content": "Deep learning models are widely used in healthcare.",
    "tags": ["learning", "healthcare", "models", "deep", "used"]
  }
]

How It Works

User uploads a document via the /upload endpoint.

TF-IDF is used to extract the most relevant keywords as tags.

The document and tags are indexed into Elasticsearch.

Search requests use Elasticsearch Query DSL for reliable full-text search.

Running the Project Locally
Prerequisites

Docker

Docker Compose

Steps to Run

Clone the repository:

git clone <repository-url>
cd scalable-doc-tagging


Build and start the services:

docker-compose up --build


Wait for Elasticsearch and Flask services to start.

Testing the API (Windows PowerShell)
Upload a document
Invoke-RestMethod -Uri http://127.0.0.1:5000/upload `
-Method POST `
-ContentType "application/json" `
-Body '{"title":"Test Doc","content":"Elasticsearch works well with Docker."}'

Search documents
Invoke-RestMethod -Uri "http://127.0.0.1:5000/search?query=Elasticsearch" `
-Method GET

Docker & Deployment Notes

Flask communicates with Elasticsearch using Docker service names (elasticsearch:9200)

Elasticsearch runs in single-node mode

Flask debug mode and reloader are disabled for container stability

Services are connected using Docker Compose networking

Future Enhancements

Replace TF-IDF with LDA or transformer-based topic modeling

Add authentication and role-based access

Deploy on AWS EC2 with persistent storage

Add pagination and advanced filtering

Author

Rohit Kumar
AI / Data Engineering Enthusiast

Conclusion

This project demonstrates practical skills in API development, NLP, Elasticsearch, Docker, and system integration, aligned with real-world AI engineering requirements.