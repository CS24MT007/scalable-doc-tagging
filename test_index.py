# test_index.py

from model import DocumentTagger
from elastic import create_index, index_document

text = """
Deep learning models are widely used in healthcare for disease detection,
medical imaging, and diagnosis support systems.
"""

title = "AI in Healthcare"

tagger = DocumentTagger()
tags = tagger.generate_tags(text)

print("Generated Tags:", tags)

create_index()
index_document(title, text, tags)
