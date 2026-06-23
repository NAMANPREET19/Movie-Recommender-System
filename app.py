import streamlit as st
import pickle
import requests



similarity=pickle.load(open('similarity.pkl','rb'))
movies=pickle.load(open('movies.pkl','rb'))
movieslist=movies['title'].values
poster_data=pickle.load(open('poster.pkl','rb'))



def recommend(movie):
    poster=[]
    movie_name=[]
    movie_index=movies[movies['title']==movie].index[0]
    distance= similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)), reverse=True,key=lambda x:x[1])[1:6]

    for i in movie_list:
        poster.append(poster_data.iloc[i[0]].poster_url)
        movie_name.append(movies.iloc[i[0]].title)

    return movie_name,poster




st.title('Movie Recommender System')

selected_movie=st.selectbox('SELECT Movie Name',movieslist)
# extras
movie_index=movies[movies['title']==selected_movie].index[0]
if st.button('Recommend'):
    recommended_movie,recommended_poster=recommend(selected_movie)
    # extras
    st.header(f'Your selected movie is {selected_movie}')
    st.image(poster_data.iloc[movie_index].poster_url,width=100)

    st.header('HERE ARE SOME RECOMMENDATIONS:')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_poster[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_poster[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_poster[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_poster[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_poster[4])

