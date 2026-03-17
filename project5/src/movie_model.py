import pandas as pd
import pickle

# Load dataset
movies = pd.read_csv("data/tmdb.csv")

# Select columns (adjust if needed)
movies = movies[['title', 'overview', 'genre']]

# Drop missing
movies.dropna(inplace=True)

# Clean genre (IMPORTANT - your dataset fix)
movies['genre'] = movies['genre'].apply(lambda x: x.replace(",", " "))

# Create tags
movies['tags'] = movies['overview'] + " " + movies['genre']

# Lowercase
movies['tags'] = movies['tags'].apply(lambda x: x.lower())

# Vectorization
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

import pickle
import os

os.makedirs("models", exist_ok=True)

# Save files
pickle.dump(movies, open('models/movies.pkl', 'wb'))
pickle.dump(similarity, open('models/similarity.pkl', 'wb'))

print("✅ Files saved successfully!")