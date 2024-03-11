import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances= sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        movie_id = df.iloc[i[0]].movie_id
        recommended_movie_names.append(df.iloc[i[0]].title)

    return recommended_movie_names



st.header('Movie Recommender System')

movie_dict=pickle.load(open('movies_dict.pkl','rb'))
df=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


movie_list = df['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names= recommend(selected_movie)
    st.text(recommended_movie_names[0])
    st.text(recommended_movie_names[1])
    st.text(recommended_movie_names[2])
    st.text(recommended_movie_names[3])
    st.text(recommended_movie_names[4])


