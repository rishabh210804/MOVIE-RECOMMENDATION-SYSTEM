import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
movies = {
    'title': [
        'The Matrix', 'John Wick', 'The Notebook', 'Avengers: Endgame',
        'Titanic', 'Gladiator', 'The Godfather', 'La La Land',
        'The Dark Knight', 'Inception'
    ],
    'genre': [
        'Action Sci-Fi', 'Action Thriller', 'Romance Drama', 'Action Sci-Fi Superhero',
        'Romance Drama', 'Action Drama', 'Crime Drama', 'Romance Musical',
        'Action Crime', 'Action Sci-Fi Thriller'
    ]
}

# Step 1: Load data into DataFrame
df = pd.DataFrame(movies)

# Step 2: Convert genre text to vector
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['genre'])

# Step 3: Calculate similarity
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Step 4: Function to recommend movies
def recommend(movie_title, df=df, similarity=cosine_sim):
    if movie_title not in df['title'].values:
        return "❌ Movie not found in database."

    index = df[df['title'] == movie_title].index[0]
    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5
    recommended_movies = [df['title'][i[0]] for i in sorted_scores]
    return recommended_movies

# Test the recommender
movie_to_search = 'Inception'
print(f"\n🎬 Because you liked '{movie_to_search}', you may also like:")
for rec in recommend(movie_to_search):
    print("👉", rec)
