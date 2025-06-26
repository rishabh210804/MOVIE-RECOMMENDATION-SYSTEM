# MOVIE RECOMMENATION SYSTEM

COMPANY: CODECH TECHNOLOGIES

NAME: RISHABH CHOUHAN

DOMAIN: ARTIFICIAL INTELLIGENCE INTERN

DURATION - 1 MONTH

# PROJECT - MOVIE RECOMMENDATION SYSTEM

# Objective

The primary objective of this project titled “Movie Recommendation System” is to develop a functional and user-friendly system that recommends movies to users based on their interests. Movie recommendation systems are a core application of machine learning and data science that are widely used in platforms like Netflix, Amazon Prime, YouTube, and Spotify to personalize user experiences. This project introduces the foundational concepts and techniques used to build a basic movie recommender using content-based filtering.

Recommender systems solve the problem of information overload by automatically suggesting items (in this case, movies) that are most relevant to the user’s preferences. They aim to improve user satisfaction and engagement by narrowing down the options to what the user is most likely to enjoy. There are two popular types of recommendation systems: collaborative filtering, which uses user behavior and preferences, and content-based filtering, which relies on attributes of the items themselves. In this project, we implement a content-based filtering system.

The dataset used in this project consists of a small collection of movies with their respective genres. Each movie is described using a single text field that includes genre-related keywords (e.g., “Action,” “Romance,” “Drama,” “Sci-Fi”). These genres are used to calculate similarities between different movies using natural language processing techniques.

The project uses the following approach:
	1.	Data Preparation: A dataset of movies is created with fields such as movie title and genre. Although the sample dataset used is small for demonstration purposes, the method can be scaled to include hundreds or thousands of movies.
	2.	Text Vectorization: To allow the system to mathematically compare genres, we use a CountVectorizer to convert genre descriptions into numerical vectors. This transformation creates a matrix that represents the frequency of each keyword in the genre descriptions.
	3.	Similarity Measurement: We use cosine similarity to measure the angle between the vector representations of movies. This helps identify how closely related two movies are based on their genres. If two movies have similar genre vectors, they are considered similar.
	4.	Recommendation Engine: When a user inputs a movie title, the system identifies similar movies by looking at the cosine similarity scores. The top 5 most similar movies are returned as recommendations.
	5.	Testing and Output: The recommender is tested with multiple movie inputs, and the system returns relevant recommendations that match the genre profile of the selected movie.

The key advantage of a content-based system is that it doesn’t depend on user data or ratings. It works purely on the item features (in this case, genres), making it suitable even when user history is unavailable (cold start problem). This makes content-based filtering a good starting point for beginners in machine learning and recommendation systems.

Through this project, learners gain hands-on experience in:
	•	Building a simple but effective recommendation algorithm
	•	Working with text-based data and applying vectorization techniques
	•	Understanding how similarity metrics like cosine similarity work
	•	Developing real-world applications using basic machine learning tools

In conclusion, the Movie Recommendation System project serves as a practical introduction to one of the most popular real-life applications of AI and machine learning. While this is a simple implementation, it lays the foundation for more complex systems that include user preferences, ratings, viewing history, and advanced algorithms like collaborative filtering, matrix factorization, and deep learning-based recommenders.

# OUTPUT
<img width="1792" alt="Image" src="https://github.com/user-attachments/assets/5da51594-cce8-423f-97bf-5e00d45d8f65" />
