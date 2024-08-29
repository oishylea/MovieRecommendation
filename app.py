<<<<<<< HEAD
=======

>>>>>>> c5864fe6e74ccc29ce3fa360880c35391a434a12
import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    API_KEY = "11a90ebcbb9b25e7e201c93163d109e8"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    if poster_path:
        full_path = "http://image.tmdb.org/t/p/w780/" + poster_path  # Change 'w500' to 'w780' to increase the poster width
    else:
        full_path = "https://via.placeholder.com/780x1170.png?text=No+Poster+Available"  # Change the placeholder size to 780x1170
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True, key = lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances [1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name,recommended_movies_poster

def set_background_color():
    html_template = f"""
    <style>
    .stApp {{
        background-color: #BAD6EB !important;
        color: black !important;
        font-family: monospace !important;
    }}
    .stButton button {{
        color: white !important;
    }}
    .stSelectbox {{
        color: black !important;
    }}
    </style>
    """
    st.markdown(html_template, unsafe_allow_html=True)

if __name__ == "__main__":
    set_background_color()
    st.markdown("<h1 style='color:black; text-align:center;'>Movies Recommendation System<br>Using Machine Learning</h1>", unsafe_allow_html=True)

    movies = pickle.load(open('artificats/movie_list.pkl','rb'))
    similarity = pickle.load(open('artificats/similary.pkl','rb'))

    movie_list = movies['title'].values

    st.markdown("<br><h5 style='color:black; text-align:center;'>Select Movie</h5>", unsafe_allow_html=True)

    selected_movie = st.selectbox(' ',
        movie_list
        )

    if st.button('Show recommendation'):
        recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
        col1,col2,col3,col4,col5= st.columns(5)
        with col1:
            st.text(recommended_movies_name[0])
            st.image(recommended_movies_poster[0])

        with col2:
            st.text(recommended_movies_name[1])
            st.image(recommended_movies_poster[1])        

        with col3:
            st.text(recommended_movies_name[2])
            st.image(recommended_movies_poster[2])

        with col4:
            st.text(recommended_movies_name[3])
            st.image(recommended_movies_poster[3])        

        with col5:
            st.text(recommended_movies_name[4])
            st.image(recommended_movies_poster[4])

