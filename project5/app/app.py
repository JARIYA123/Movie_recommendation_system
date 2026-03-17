import streamlit as st
import pickle
import pandas as pd

# Load saved data
movies = pickle.load(open('../models/movies.pkl', 'rb'))
similarity = pickle.load(open('../models/similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    results = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for movie in results:
        st.write("👉", movie)