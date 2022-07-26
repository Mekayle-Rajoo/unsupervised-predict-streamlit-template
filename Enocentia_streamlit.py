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
import joblib,os

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model


# Data Loading
movies = pd.read_csv('resources/data/movies.csv')
train_data = pd.read_csv('resources/data/ratings.csv')
unpickled_model = joblib.load(open("resources/models/SVD.pkl","rb"))


#To save the session state to enable nested buttons:
def callback():
    st.session_state.button_clicked = True


##########To set our background##############
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.ibb.co/Smvzshf/fall-movies-index-1628968089-01.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#############################################


# App declaration
def main():
    
    #Our background
    set_bg_hack_url()
    
    #Our Logo
    st.image("resources/logogif.gif")

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","FAQ", "Insights","Download our app", "Contact Us"]

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
        movie_1 = st.selectbox('Fisrt Option',movies["title"][14930:15200])
        movie_2 = st.selectbox('Second Option',movies["title"][25055:25255])
        movie_3 = st.selectbox('Third Option',movies["title"][21100:21200])
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
                
                with st.spinner('Crunching the numbers...'):
                    top_recommendations = collab_model(movie_list=fav_movies,
                                                       top_n=10)
                st.title("We think you'll like:")
                for i,j in enumerate(top_recommendations):
                    st.subheader(str(i+1)+'. '+j)
                

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    if page_selection == "Contact Us":
        st.title("Contact Us")
        st.write("Website:www.lumiere.com") 
        st.write("Address:123 Richard St., Sandton, 1683") 
        st.write("Tel: +27 32 944 8443") 
        st.write("Operating Hours")
        st.write("Monday - Friday, 8am - 5pm")
        st.write("Saturday, 8am - 1pm") 
        st.write("Sunday, 9am - 1pm")
    

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()