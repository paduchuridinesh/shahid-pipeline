# app.py
from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load and preprocess data
df = pd.read_csv("books.csv")
df = df.fillna("")
df['combined'] = df['title'] + ' ' + df['authors'] + ' ' + df['categories'] + ' ' + df['description']

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommend function
def recommend(title):
    idx = df[df['title'].str.lower() == title.lower()].index
    if len(idx) == 0:
        return []
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[book_indices].tolist()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    title = request.form['title']
    recs = recommend(title)
    return render_template('index.html', recommendations=recs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
