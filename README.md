# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System that suggests similar movies based on user selection using content-based filtering.

---

## 🚀 Project Overview

This project recommends movies by analyzing their **overview and genres**. It uses **Natural Language Processing** (NLP) and similarity algorithms to find movies that are most similar to a selected movie.

---

## 🧠 How It Works

*  Load movie dataset (`tmdb.csv`)
*  Clean and preprocess data
*  Combine features (overview + genre)
*  Convert text into numerical vectors using CountVectorizer
*  Compute similarity using cosine similarity
*  Recommend top 5 similar movies

---

## 📂 Project Structure

```
movie_project/
│
├── data/
│   └── tmdb.csv
│
├── src/
│   └── movie_model.py
│
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── app.py
└── README.md
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/JARIYA123/movie-recommender.git
cd movie-recommender
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Step 1: Generate Model Files

```
python src/movie_model.py
```

This will create:

* `models/movies.pkl`
* `models/similarity.pkl`

---

### Step 2: Run Streamlit App

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🎯 Features

* Select a movie from dropdown
* Get top 5 similar movie recommendations
* Fast and interactive UI using Streamlit

---

## 📸 Future Improvements

* Add movie posters using TMDB API
* Improve UI (Netflix-style layout)
* Add search functionality
* Deploy on cloud (Streamlit Cloud / Render)

---

## 📊 Example Output

Input:

```
Avatar
```

Output:

```
Guardians of the Galaxy  
Interstellar  
Star Trek  
John Carter  
The Fifth Element  
```

---

## 🧠 Concepts Used

* Natural Language Processing (NLP)
* CountVectorizer
* Cosine Similarity
* Content-Based Filtering

---

## 🌍 Deployment

You can deploy this project using:

* Streamlit Cloud
* Render
* Hugging Face Spaces

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📧 Contact

If you have any questions or suggestions, feel free to connect.

---

⭐ If you like this project, give it a star!
