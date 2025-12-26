from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class DocumentTagger:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=50
        )

    def generate_tags(self, text, top_n=5):
        tfidf_matrix = self.vectorizer.fit_transform([text])
        feature_names = self.vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]

        top_indices = np.argsort(scores)[::-1][:top_n]
        tags = [feature_names[i] for i in top_indices if scores[i] > 0]

        return tags
