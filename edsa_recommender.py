"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.api import fetch_poster, fetch_runtime ,fetch_imdbrating, fetch_plot, fetch_genre
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model 
import sweetviz as sv

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
movies = pd.read_csv('resources/data/movies.csv')
links = pd.read_csv('resources/data/movies_link.csv')

# App declaration
def main():

 
    st.sidebar.image("resources/imgs/logo.webp")
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Recommender System","Recommend with Poster","EDA","Business Solutions","Meet the Team"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    
    if page_selection == "Home":
        st.write("# MovieMate")
        st.write("### Find Your Perfect Flick ")
        st.image("resources/imgs/APP.webp", use_column_width=True)
        
    if page_selection == "Recommend with Poster":
        
        # Header contents
        st.image('resources/imgs/header.jpeg')
        st.markdown("# MOVIE RECOMMENDER")
        #st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):

                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    with st.container():
                        for i,j in enumerate(top_recommendations):
                            col1, col2, = st.columns(2)
                            with col1:
                                temp_id = links.loc[links['title'] == j].movieId.values[0]
                                id = str(links.loc[links['movieId']== temp_id].imdbId.values[0])                                
                                st.image(fetch_poster('tt'+id.zfill(7)))
                            with col2:
                                st.subheader(str(i+1)+'. '+j)
                                id = str(links.loc[links['movieId']== temp_id].imdbId.values[0])
                                st.write('Plot: ' + fetch_plot('tt'+id.zfill(7)))
                                st.write('Genre: ' + fetch_genre('tt'+id.zfill(7)))
                                st.write('Rating: ' + fetch_imdbrating('tt'+id.zfill(7) )+ '/10')
                                st.write('Runtime: ' + fetch_runtime('tt'+id.zfill(7)))
                            
                            
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
                        
        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    with st.container():
                        for i,j in enumerate(top_recommendations):
                            col1, col2, = st.columns(2)
                            with col1:
                                temp_id = links.loc[links['title'] == j].movieId.values[0]
                                id = str(links.loc[links['movieId']== temp_id].imdbId.values[0])                                
                                st.image(fetch_poster('tt'+id.zfill(7)))
                            with col2:
                                st.subheader(str(i+1)+'. '+j)
                                id = str(links.loc[links['movieId']== temp_id].imdbId.values[0])
                                st.write('Plot: ' + fetch_plot('tt'+id.zfill(7)))
                                st.write('Genre: ' + fetch_genre('tt'+id.zfill(7)))
                                st.write('Rating: ' + fetch_imdbrating('tt'+id.zfill(7) )+ '/10')
                                st.write('Runtime: ' + fetch_runtime('tt'+id.zfill(7)))
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
            
    if page_selection == "EDA":
        
        st.markdown("# Exploratory Data Analysis")
        st.markdown("Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.")
        #if st.checkbox('Why show Eda??'):
            #st.subheader('r/dataisbeautiful subscriber rank per year')
            #st.image('resources/imgs/reddit.png',use_column_width=True)
            
        eda_select = st.selectbox('Select a Visual to inspect ',('Rating Distribution','Most Common Genres'))
        if eda_select == "Rating Distribution":
            st.image("resources/imgs/Pie_chart.png",use_column_width=True)
            st.write("")

        #Count of the most common genres
        if eda_select == "Most Common Genres":
                st.image("resources/imgs/Common_genres.png",use_column_width=True)
                st.markdown(" ")
               
            
        pass
    
    
    if page_selection == "Business Solutions":
        st.markdown("# Business Solutions")
        st.markdown("The internet is a go-to space for businesses seeking to access the global marketplace. Nowadays, there is a preference among shoppers to make purchases online from the comfort of their own homes.Now more than ever it really pays to know your customer, and thanks to Recommender Systems now you can")
        st.markdown("Recommender Systems can assess multiple parameters to create solutions unique to the business needs. It's an effective system when expanding your business (35% of all sales on Amazon are attributed to the recommender). It ensures businesses are better equiped to provide their customers with their desired products and services, boosting business and income")
        
        
        st.markdown("## Content Based Filtering")
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.image('resources/imgs/contentbased.png',use_column_width=True)
        with col2:
            st.write('')
            st.markdown("Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.Content-based filtering makes recommendations by using keywords and attributes assigned to objects in a database (e.g., items in an online marketplace) and matching them to a user profile creating some form of feature matrix. The user profile is created based on data derived from a user’s actions, such as purchases, ratings (likes and dislikes), downloads, items searched for on a website and/or placed in a cart, and clicks on product links. An example of a feature matrix:")
            
        st.markdown("## Collaborative Filtering")
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.image('resources/imgs/collab.webp',use_column_width=True)
        with col2:
            st.markdown("Collaborative filtering uses algorithms to filter data from user reviews to make personalized recommendations for users with similar preferences. This is the hallmark for Recommender Systems, Giving greater insights into what users/customers are interested")

                    
                    
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
