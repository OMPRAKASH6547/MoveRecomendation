import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=47d8169c4187685be533ca316057ccea&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recomended_moves_posters = []
    for i in movies_list:
        movie_id_x = movies.iloc[i[0]].movie_id_x
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recomended_moves_posters.append(fetch_poster(movie_id_x))
    return recommended_movies, recomended_moves_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Move Recommender System')
st.subheader("Select the movie name")
selected_movie_name = st.selectbox(
    'Select  the movies name',
    movies['title'].values
)
if st.button('Recommend'):
    name, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col1:
        st.text(name[1])
        st.image(posters[1])
    with col1:
        st.text(name[2])
        st.image(posters[2])
    with col1:
        st.text(name[3])
        st.image(posters[3])
    with col1:
        st.text(name[4])
        st.image(posters[4])
