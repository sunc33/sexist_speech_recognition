import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from PIL import Image

# ----------------------------------
#         GESTION FONT
# ----------------------------------
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Ubuntu', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

# ----------------------------------
#         HEADER TITRE ET IMAGE
# ----------------------------------
path_image = '../raw_data/Logo/basta.png'
image = Image.open(path_image)

st.image(image, width = None)

# ----------------------------------
#         MENU DE SELECTION
# ----------------------------------

def load_csv(path):
    """
        Import the Reddit DataFrame
        """
    df = pd.read_csv(path)
    print(df)
    return df

#TODO: A supprimer
def tupple(df):
    """
        Function to convert df into a list and then a tuple for the
        implementation in selectbox
        """
    member = [member for member in df['title']]
    name_tuple = tuple(member)
    return name_tuple

## PATH A CHANGER POUR LINKER VERS le csv conversations

path = os.path.join('../raw_data/COM.csv')
#'/Users/camillepettineo/code/sunc33/sexist_speech_recognition/sexist_speech_recognition/raw_data/TWITTER_Name_congress.csv'
df = load_csv(path)
# name_tuple = tupple(df)

#st.markdown("""### Quel subreddit voulez-vous analyser ?""")
st.markdown("<h1 style='text-align: center; color: black;'>Quel subreddit voulez-vous analyser ?</h1>", unsafe_allow_html=True)

option = st.selectbox(
     ' ',
     (df['title'].unique()))

#st.write('Vous avez sélectionné :', option)

# ----------------------------------
#         HISTOGRAMME : répartition des postes par note moyenne sexisme
# ----------------------------------

fig_post = px.histogram(df[df['title']==option], x="label")
st.plotly_chart(fig_post)

# Message Insight qui s'affiche en regard du graph
st.markdown("""Sur les {nombre_poste_total} postes total hebergés sur ce subreddit,
            {nombre_poste_sexiste_sup_à_70} ont une note moyenne de sexisme supérieur à 70% | {moyenne_sexiste}. """)

# ----------------------------------
#         DONUTS : repartition sexiste, pas sexiste commentaires d'un poste
# ----------------------------------

st.markdown("""Avec une note moyenne de {note_moyenne_poste},
            le poste nommé {titre_poste} est le moins bien noté de ce subreddit.
            Pourquoi ? Sur les {nb_com_poste} commentaires de ce poste, {part_com_sexiste}""")

#print(type(option))
# viz = df[df['title']==option][['sexist','pas_sexist','total_com']]
# print(viz)

fig_per_person = px.pie(df[df['title']==option], values='sexist', names='label',
            color_discrete_sequence=px.colors.sequential.RdBu,
            opacity=0.7, hole=0.5)
st.plotly_chart(fig_per_person)

# ----------------------------------
#         TREEMAP : repartition user sexiste
# ----------------------------------

st.markdown("""Des messages sexistes écris
            par {nombre_user_sexiste} contributeurs différents.""")


df = px.data.gapminder().query("year == 2007")
fig_tree = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig_tree.update_layout(margin = dict(t=50, l=25, r=25, b=25))

st.plotly_chart(fig_tree)

# ----------------------------------
#        BARRE DE CREDIT & METHODO
# ----------------------------------
path_image = os.path.join('../raw_data/Logo/ligne.png')
image = Image.open(path_image)

st.image(image, width = None)

# ----------------------------------
#         METHODO & LIEN VERS GITHUB
# ----------------------------------

# À ECRIRE

st.markdown("""**Réalisé par** : Camille Pettineo, Chen Sun, Liam Abramczyk & Anatole Soulié. """)

st.markdown("""**Méthodologie** :
""")
st.markdown("""Dans le cadre du projet “Basta” nous avons analysé XXXXX conversations
            du réseau social Reddit grâce à notre model NLP entraîné à reconnaître
            les textes sexistes.
            Par sexiste nous entendons : “Tout propos discriminant fondée
            sur le sexe et par extension sur le genre d'une personne.” """)

st.markdown("""**Sources** : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""")

# ----------------------------------
#         CREDITS & LOGO LE WAGON
# ----------------------------------

if st.button('🎈🎈 Merci pour votre attention ! 🎈🎈'):
   st.balloons()

## LOGO LE WAGON
path_wagon = os.path.join('../raw_data/Logo/wagon-executive.jpg')
image = Image.open(path_wagon)
st.image(image, caption='Le Wagon', use_column_width=False)

if __name__=='__main__':
    print('hello')
    #path = '/Users/camillepettineo/code/sunc33/sexist_speech_recognition/sexist_speech_recognition/raw_data/TWITTER_Name_congress.csv'
    #load_csv(path)
