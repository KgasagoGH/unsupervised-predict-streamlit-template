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
    page_options = ["Home",'About Us',"Recommender System","EDA","Business Solutions",'App Feedback']

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
    
    if page_selection == "About Us":
        st.title("About Us")

    # Company Profile
        st.header("Company Profile")
        st.write("Step into the world of our Movie Recommender System, where personalized movie recommendations await to elevate your entertainment experience. Our mission is to enrich your cinematic journey, making each movie-watching moment not just enjoyable but truly thrilling. Join us as we guide you through a curated selection of films tailored to your unique preferences, ensuring every viewing is a captivating and memorable experience.")

    # Team Member Profiles
        st.header("Meet The Team")
        with st.container():
            col1, col2, col3 = st.columns(3)

            with col1:
                st.image('resources/imgs/IMG_20240126_102843_362.jpg', width= 200)
                st.subheader("Iloh Fransisca")
                st.caption("Web Developer")

            with col2:
                st.image('resources/imgs/mashoto.webp', width= 200)
                st.subheader("Mashoto Kgasago")
                st.caption("Data Engineer")
                    
            with col3:
                st.image('resources/imgs/IMG_4552.jpg', width= 200)
                st.subheader("Mkhosi Myeni")
                st.caption("Project Manager")

        with st.container():
            col4, col5, col6 = st.columns(3)

            with col4:
                st.image('resources/imgs/WhatsApp_Image_2023-11-15_at_15.41.44_2706cb67.jpg', width= 200)
                st.subheader("Jonathan Thomson")
                st.caption("Data Scientist")

            with col5:
                st.image('resources/imgs/IMG_20240126_102843_362.jpg', width= 200)
                st.subheader("Justice Mashako")
                st.caption("Data Scientist")
                    
            with col6:
                st.image('resources/imgs/FHULU.jpeg', width= 200)
                st.subheader("Faith Fhulufhelo")
                st.caption("Data Engineer")


    
        #team_members = [
         #   {"name": "Iloh Fransisca", "role": "Web Developer",
          #   "bio": "Fransisca is a highly skilled web developer with a passion for creating engaging and user-friendly web applications. With a keen eye for design and a strong understanding of user experience, she brings creativity and innovation to our development team. Fransisca enjoys tackling complex challenges and turning them into elegant solutions.",
           #  "image": "resources\imgs\IMG_20240126_102843_362.jpg"},
            #{"name": "Mashoto Kgasago", "role": "Data Engineer",
            # "bio": "Mashoto is a seasoned data scientist and the team lead for our movie recommendation project. With a background in machine learning and data analysis, Mashoto leverages advanced algorithms to provide accurate and personalized movie recommendations. His commitment to delivering data-driven insights contributes to the success of our recommendation system.",
            # "image": "resources\imgs\mashoto.webp"},
            #{"name": "Mkhosi Myeni", "role": "Project Manager",
             #"bio": "Mkhosi is a results-oriented project manager with a proven track record of successfully leading and delivering complex projects. With strong leadership and communication skills, Mkhosi ensures seamless coordination among team members, stakeholders, and project goals. His strategic approach and attention to detail drive the project towards success.",
             #"image": "resources\imgs\IMG_4552.jpg"},
        
            #{"name": "Jonathan Thomson", "role": "Data Scientist",
            # "bio": "Jonathan is a meticulous data analyst with a passion for transforming raw data into meaningful insights. His analytical skills and attention to detail help uncover valuable patterns and trends, contributing to informed decision-making. Jonathan's commitment to data accuracy and efficiency enhances our data analysis capabilities.",
             #"image": "resources\imgs\WhatsApp_Image_2023-11-15_at_15.41.44_2706cb67.jpg"},
        
            #{"name": "Justice Mashako", "role": "Data Scientist",
             #"bio": "Justice is a dedicated data scientist with expertise in developing and implementing machine learning models. His analytical mindset and problem-solving abilities contribute to the continuous improvement of our recommendation algorithms. Justice is passionate about leveraging data science to enhance user experiences in the realm of movie recommendations.",
             #"image": "resources\imgs\IMG_20240126_102843_362.jpg"},
        
            #{"name": "Faith Fhulufhelo", "role": "Data Engineer",
            # "bio": "Faith is a skilled machine learning specialist specializing in building advanced recommendation models. Her proficiency in machine learning algorithms and model optimization ensures that our recommendation system stays at the forefront of technology. Faith's commitment to pushing the boundaries of machine learning elevates our system's performance.",
             #"image": "resources\imgs\IMG_20240126_102843_362.jpg"},
        
    #]

       # for member in team_members:
        #    st.subheader(f"{member['name']} - {member['role']}")
        
        # Using st.columns to create a layout with two columns
           # col1, col2 = st.columns([1, 3])
        
        # Display the image in the first column
            #with col1:
             #   st.image(member['image'], caption=f"{member['name']}", use_column_width=True)
        
        # Display the bio in the second column
            #with col2:
             #   st.write(member['bio'])
        
        # Separator between team members
            #st.write("---")  

    # Company Contact
        st.header("Contact Us")
        st.write("Feel free to reach out to us if you have any questions, suggestions, or inquiries.")

        company_contact = {
            "email": "info@cinematrix.com",
            "phone": "+1 (123) 452-7658",
            "address": "548 Movie Street, Entertainment City"
        }

        st.write(f"Email: {company_contact['email']}")
        st.write(f"Phone: {company_contact['phone']}")
        st.write(f"Address: {company_contact['address']}")

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

    import datetime
    import logging
    

    if page_selection == "App Feedback":
        st.title("App Feedback")
        st.write("We appreciate your valuable feedback on our app! Your insights and suggestions are crucial in helping us improve and provide you with an exceptional user experience. Please take a few moments to share your thoughts by completing this feedback form. Your input will assist us in understanding what aspects of the app are working well and where we can make enhancements or address any issues you may have encountered.")
    
        with st.form("feedback_form"):
            c_feedback = st.container()

            with c_feedback:
                col_feedback_1, col_feedback_2 = st.columns(2)
                with col_feedback_1:
                    feedback_name = st.text_input(
                        "Name",
                        placeholder='Enter',
                    )
                with col_feedback_2:
                    feedback_email = st.text_input(
                        "Email",
                        placeholder='Enter',
                    )
                col_feedback_3, col_feedback_4 = st.columns(2)
                with col_feedback_3:
                    feedback_type = st.selectbox(
                        'Category',
                        ('Defect', 'Bug', 'Feature'))
                with col_feedback_4:
                    feedback_subject = st.text_input(
                        "Subject",
                        placeholder='Enter',
                    )
                col_feedback_5, col_feedback_6 = st.columns(2)
                with col_feedback_5:
                    feedback_description = st.text_area('Description', '''''', height=400)
                with col_feedback_6:
                    tab_low, tab_medium, tab_high = st.tabs(["Low", "Medium", "High"])
                    with tab_low:
                        feedback_priority = 0
                    with tab_medium:
                        feedback_priority = 1
                    with tab_high:
                        feedback_priority = 2

                    feedback_satisfaction = st.radio(
                        "Satisfaction",
                        ('Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied'))

                    st.write('Additional Features')
                    feedback_additional_1 = st.checkbox('UI/UX')
                    feedback_additional_2 = st.checkbox('Performance')
                    feedback_additional_3 = st.checkbox('Functionality')
                    feedback_additional_4 = st.checkbox('Other')

            submit_feedback = st.form_submit_button("Submit Feedback")
        
            if submit_feedback:
                st.success("Feedback submitted successfully! Thank you for your input.")
                st.balloons()
                
    
    
    if page_selection == "EDA":
        
        st.markdown("# Exploratory Data Analysis")
        st.markdown("Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.")

            
        eda_select = st.selectbox('Select a Visual to inspect ',('Rating Distribution','Most Common Genres','Top Cast Members','Top Movie Directors'))
        if eda_select == "Rating Distribution":
            st.image("resources/imgs/Pie_chart.png",use_column_width=True)
            st.write("A significant majority of ratings within the viewer's dataset predominantly lean towards a 4-star rating, encompassing the largest share at 26.5%. Following closely, the next highly favored rating is 5 stars, constituting 14.5% of the entire rating distribution. Conversely, the least frequent rating is 0.5 stars, making up a relatively minor portion at 1.6%.Interestingly, approximately 12.9% of ratings fall within the range of 2 to 0.5 stars, providing insight into the distribution of viewer preferences across different rating levels. This diversity in ratings adds depth to the dataset, capturing a range of viewer sentiments and contributing to the overall nuanced landscape of audience feedback.")

        #Count of the most common genres
        if eda_select == "Most Common Genres":
            st.image("resources/imgs/Common_genres.png",use_column_width=True)
            st.write("Drama stands out as the predominant genre within the database, reflecting the highest frequency. Notably, there are around 5000 films that currently lack genre information. To address this gap, leveraging the IMDB and TMDB IDs through APIs can provide an effective strategy to complete and enhance the genre details for these films. Additionally, it's worth noting that the term 'IMAX' in this context doesn't represent a genre but rather refers to a proprietary system designed for large-scale cinematic presentations. As we refine and augment the genre information in the database, ensuring accuracy and clarity will be a key focus.")
 
         #Count of top cast members
        if eda_select == "Top Cast Members":
            st.image("resources/imgs/top_cast_members.png",use_column_width=True)
            st.write("In the cinematic realm, Samuel L. Jackson stands as an iconic figure with a prolific career, leaving an indelible mark on audiences through his charismatic and versatile performances. Bruce Willis, celebrated for his diverse roles and on-screen presence, has garnered widespread recognition, showcasing his acting prowess in a variety of genres. Steve Buscemi, known for his ability to add depth and authenticity to films, distinguishes himself with unique characters and memorable portrayals, making significant contributions to the cinematic landscape. Exploring our extensive movie database reveals the pivotal role these outstanding cast members play, enhancing the overall viewing experience with their exceptional talents.") 
        #Count of top movie directors
        if eda_select == "Top Movie Directors":
            st.image("resources/imgs/top_directors.png",use_column_width=True)
            st.write("Prominent directors in the dataset include Luc Besson, Woody Allen, Stephen King, and Ki-duk Kim. However, it's essential to note that William Shakespeare and Stephen King are recognized as writers, not directors. This distinction is crucial to consider during the modeling process, emphasizing the need for accuracy in attributing roles to individuals within the film industry. Understanding and respecting the distinct contributions of writers and directors will enhance the precision and reliability of our modeling endeavors.")           
        
              
        pass
    
    
    if page_selection == "Business Solutions":
        st.markdown("# Business Solutions")
        st.markdown("In today's digital era, the online landscape has become a primary hub for businesses aiming to tap into the vast global marketplace. The modern consumer trend leans towards the convenience of making purchases from the comfort of their homes, marking a significant shift in shopping preferences. Now, more than ever, understanding your customers is a valuable asset, and with Recommender Systems, this insight becomes accessible.")
        st.markdown("These systems go beyond conventional approaches by evaluating numerous parameters to craft tailored solutions that cater to the unique needs of your business. When considering business expansion, the impact of Recommender Systems cannot be overstated. A striking example is evident in Amazon, where a noteworthy 35% of all sales are attributed to the effectiveness of the recommender. This sophisticated tool equips businesses to not only meet but exceed customer expectations, delivering the products and services that resonate with their desires. The result? A substantial boost in business activity and income, paving the way for sustained success in the dynamic online marketplace.")
        
        
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
