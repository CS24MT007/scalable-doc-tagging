from flask import Flask, request, jsonify
import requests
import os
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# -----------------------
# Configuration
# -----------------------
ES_URL = os.environ.get("ES_URL", "http://elasticsearch:9200")
INDEX_NAME = "documents"

# -----------------------
# Simple TF-IDF tagger
# -----------------------
def generate_tags(text, top_k=5):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf.toarray()[0]
    tags = sorted(
        zip(feature_names, scores),
        key=lambda x: x[1],
        reverse=True
    )
    return [tag for tag, score in tags[:top_k]]

# -----------------------
# Upload Endpoint
# -----------------------
@app.route("/upload", methods=["POST"])
def upload_document():
    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    tags = generate_tags(content)

    doc = {
        "title": title,
        "content": content,
        "tags": tags
    }

    try:
        response = requests.post(
            f"{ES_URL}/{INDEX_NAME}/_doc",
            json=doc,
            timeout=5
        )

        if response.status_code not in [200, 201]:
            return jsonify({"error": "Failed to index document"}), 500

        return jsonify({
            "message": "Document indexed successfully",
            "tags": tags
        })

    except requests.exceptions.RequestException:
        return jsonify({"error": "Elasticsearch not reachable"}), 500


# -----------------------
# Search Endpoint (Query DSL)
# -----------------------
@app.route("/search", methods=["GET"])
def search_documents():
    query = request.args.get("query")

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    payload = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "content", "tags"]
            }
        }
    }

    try:
        response = requests.post(
            f"{ES_URL}/{INDEX_NAME}/_search",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=5
        )

        if response.status_code != 200:
            return jsonify({"error": "Elasticsearch query failed"}), 500

        hits = response.json().get("hits", {}).get("hits", [])
        results = [hit["_source"] for hit in hits]

        return jsonify(results)

    except requests.exceptions.RequestException:
        return jsonify({"error": "Search service unavailable"}), 500


# -----------------------
# Run App (Docker-safe)
# -----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
