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
path_image = os.path.join('../../raw_data/Logo/basta.png')
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

path_page = os.path.join('../../raw_data/df_page.csv')
#'/Users/camillepettineo/code/sunc33/sexist_speech_recognition/sexist_speech_recognition/raw_data/TWITTER_Name_congress.csv'
df_page = load_csv(path_page)
# name_tuple = tupple(df_page)

#st.markdown("""### Quel subreddit voulez-vous analyser ?""")
st.markdown("<h1 style='text-align: center; color: black;'>Quel subreddit voulez-vous analyser ?</h1>", unsafe_allow_html=True)

option = st.selectbox(
     ' ',
     (df_page['sub_reddit'].unique()))

#st.write('Vous avez sélectionné :', option)

# ----------------------------------
#         HISTOGRAMME : répartition des postes par note moyenne sexisme
# ----------------------------------

path_post = os.path.join('../../raw_data/df_post.csv')
df_post = load_csv(path_post)


fig_post = px.histogram(df_post[df_post['sub_reddit']==option], x="pourcentage", labels={"pourcentage":"pourcentage sexisme","count":"nombre de poste"}, title="Pourcentage de commentaires sexistes par poste au sein de ce subreddit")
st.plotly_chart(fig_post)


# Message Insight qui s'affiche en regard du graph

nombre_poste_total=df_page[df_page['sub_reddit']==option].iat[0,-2]
nombre_poste_sexiste_sup_à_66=df_page[df_page['sub_reddit']==option].iat[0,-3]
moyenne_sexiste=df_page[df_page['sub_reddit']==option].iat[0,-1]

st.markdown(f"""Sur les {nombre_poste_total} commentaires total hebergés sur ce subreddit,
            {nombre_poste_sexiste_sup_à_66} ont une note moyenne de sexisme supérieur à 66%. """)

# ----------------------------------
#         DONUTS : repartition sexiste, pas sexiste commentaires d'un poste
# ----------------------------------
# note_moyenne_poste=
# titre_poste=
# nb_com_poste=
# part_com_sexiste=


#print(type(option))
# viz = df[df['title']==option][['sexist','pas_sexist','total_com']]
# print(viz)

path_image = os.path.join('../../raw_data/Logo/ligne.png')
image = Image.open(path_image)

st.image(image, width = None)

st.markdown("<h1 style='text-align: center; color: black;'>Quel post voulez vous analyser?</h1>", unsafe_allow_html=True)

# ----------------------------------
#         Donut : repartition commentaires sexist
# ----------------------------------

option2 = st.selectbox(
     ' ',
     df_post[df_post['sub_reddit']==option]['post_title'].unique())

path_comments= os.path.join('../../raw_data/df_comments.csv')
df_comments = pd.read_csv(path_comments)

df_comments_2 = df_comments[df_comments['post_title']==option2]

df_donut = pd.DataFrame(columns=['title','label','nombre'])

# sexist = pd.DataFrame(np.array([df_comments_2.iloc[0]['post_title'],'sexist', len(df_comments_2[df_comments_2['label']==1])  ]),columns=['title','label','nombre'])
# pas_sexist = pd.DataFrame(np.array([df_comments_2.iloc[0]['post_title'],'pas sexist', len(df_comments_2[df_comments_2['label']==0]) ]),columns=['title','label','nombre'])

df_donut.loc[0] = ( [df_comments_2.iloc[0]['post_title'], 'sexist', len(df_comments_2[df_comments_2['label']==1]) ] )
df_donut.loc[1] = ([df_comments_2.iloc[0]['post_title'], 'pas sexist', len(df_comments_2[df_comments_2['label']==0]) ])



fig_per_person = px.pie(df_donut, values='nombre', names='label',
            color_discrete_sequence=px.colors.sequential.Rainbow,
            opacity=0.7, hole=0.5, title="Proportion des commentaires sexistes sur ce post")
st.plotly_chart(fig_per_person)



pourcentage_sexist= df_post[df_post['post_title']==option2].iat[0,-1]

st.markdown(f"""{pourcentage_sexist}% des commentaires écrits sur ce post sont considérés comme sexist par notre modèle.""")

# st.markdown("""Avec une note moyenne de {note_moyenne_poste},
#             le poste nommé {titre_poste} est le moins bien noté de ce subreddit.
#             Pourquoi ? Sur les {nb_com_poste} commentaires de ce poste, {part_com_sexiste}""")

# ----------------------------------
#         TREEMAP : repartition user sexiste
# ----------------------------------

# st.markdown("""Des messages sexistes écris
#             par {nombre_user_sexiste} contributeurs différents.""")


# df = px.data.gapminder().query("year == 2007")
# fig_tree = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
#                   color='lifeExp', hover_data=['iso_alpha'],
#                   color_continuous_scale='RdBu',
#                   color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
# fig_tree.update_layout(margin = dict(t=50, l=25, r=25, b=25))

# st.plotly_chart(fig_tree)


# ----------------------------------
#         show a comment
# ----------------------------------
if st.checkbox('Show a random comment'):

    comment='show a comment'
    st.write(
        f' "{"if women want equality they should work heavy lifting manual labor jobs and let men hit them back"}" '
        )

# ----------------------------------
#        BARRE DE CREDIT & METHODO
# ----------------------------------
path_image = os.path.join('../../raw_data/Logo/ligne.png')
image = Image.open(path_image)

st.image(image, width = None)


# ----------------------------------
#         METHODO & LIEN VERS GITHUB
# ----------------------------------

# À ECRIRE

st.markdown("""**Réalisé par** : Camille Pettineo, Chen Sun, Liam Abramczyk & Anatole Soulié. """)

st.markdown("""**Méthodologie** :
""")
st.markdown("""Dans le cadre du projet "Basta" nous avons analysé 14,808 conversations
            du réseau social Reddit grâce à notre model NLP entraîné à reconnaître
            les textes sexistes.
            Par sexiste nous entendons : "Tout propos discriminant fondée
            sur le sexe et par extension sur le genre d'une personne." """)

st.markdown("""**Sources des datasets d'entraînement** : Leibniz-Institut für Sozialwissenschaften,
            National Institute of Technology Patna, North American Chapter of the Association for Computaitional Linguistics(NAACL)
""")
st.markdown("""**Sources des datasets d'analyse** : Reddit Social Media

""")






# ----------------------------------
#         CREDITS & LOGO LE WAGON
# ----------------------------------

if st.button('🎈🎈 Merci pour votre attention ! 🎈🎈'):
   st.balloons()

## LOGO LE WAGON
path_wagon = os.path.join('../../raw_data/Logo/wagon-executive.jpg')
image = Image.open(path_wagon)
st.image(image, caption='Le Wagon', use_column_width=False)

if __name__=='__main__':
    print('hello')
    #path = '/Users/camillepettineo/code/sunc33/sexist_speech_recognition/sexist_speech_recognition/raw_data/TWITTER_Name_congress.csv'
    #load_csv(path)
