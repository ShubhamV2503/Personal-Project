from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)


rc = load(r'C:\Users\JoyBoy\Desktop\Code\Learnbay\Code\ML\Project\Recommendation System\recommendation.joblib')

movie_set = load(r'C:\Users\JoyBoy\Desktop\Code\Learnbay\Code\ML\Project\Recommendation System\movie_dataset.joblib')

def key_sort(item):
    return item[1]

def recommendation(movie_name):
    movie_name = movie_name.lower()
    index =  movie_set[movie_set['title']==movie_name].index[0]
    
    dist = []
    counter = 0
    movie = []
    for i in range(len(rc)):
        dist.append((i,rc[index][i]))  ## this will give tuple
        distance = sorted(dist , reverse=True , key=key_sort)
    
    while counter!=5:
        movie.append(movie_set.title[distance[counter][0]])
        counter = counter + 1
    return movie[1:]

# # Assume you have a function recommend_movies(movie_name) that returns a list of recommended movies
# def recommend_movies(movie_name):
#     # Replace this with your actual movie recommendation logic
#     # For demonstration purposes, we'll just return a static list of movies
#     recommended_movies = ["Movie A", "Movie B", "Movie C", "Movie D"]
#     return recommended_movies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']
    recommended_movies = recommendation(movie_name)
    return render_template('index.html', movie_name=movie_name, recommended_movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
