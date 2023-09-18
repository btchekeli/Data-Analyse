# Import necessary libraries
import os
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar
from wordcloud import WordCloud
import plotly.express as px
from PIL import Image


    
icon_path = os.path.join(os.path.dirname(__file__), "./img/logo_principal_HB.png")
icon = Image.open(icon_path)
st.set_page_config(
    page_title="PacificDatavizChallenge",
    page_icon = icon,
    # page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto",
    )

# Sidebar for navigation
with st.sidebar:
    choice = option_menu(
            menu_title = "Menu",
            options=["Accueil", "Exploration des données", "Analyses et dataviz", "Ressources"],
            icons=['house', "database-fill-gear",'bar-chart-line-fill', 'gear', "list-task", "book"], # bootstrap icons
            menu_icon="list", default_index=0 ) #, orientation="horizontal")
     
    st.write("Présenté par: ")
    st.success("**Brunel TCHEKELI**")
    st.divider()
    col1, col2 = st.columns(2)
    
    # Première colonne
    with col1:
        import os
        image_path = os.path.join(os.path.dirname(__file__), "img", "linkedin_icon.png")
        img = Image.open(image_path)
        st.image(img, width=50)
        st.write("[LinkedIn](https://www.linkedin.com/in/brunel-tchekeli/)")

  # Deuxième colonne
    with col2:
        
        image_path = os.path.join(os.path.dirname(__file__), "img","github_logo.png")
        img = Image.open(image_path)
        st.image(img, width=30)
        st.write("[GitHub](https://github.com/btchekeli)")
        
        
    
def display_header_info():
    
    st.image("https://data.gouv.nc/assets/theme_image/PACIFIC_DATAVIZ_CHALLENGE_COVER.jpg", width=800, use_column_width=False)
    
    # Three columns
    col1, col2, col3 = st.columns([1,2,1])
   
   # Display the logo in the middle column
    with col2:
       st.image("https://btchekeli.github.io/src/My_logos/logo_principal_HB.png", use_column_width=True)
      
    
    # Display the quote
    st.markdown("<center><h6>La donnée est l’actif stratégique de la révolution numérique</h6></center>", unsafe_allow_html=True)
    
    # Display the title
    st.markdown("<hr style='border-width:2px;border-color:#75DFC1'><center><h4><strong>PacificDatavizChallenge 2023 :</strong></h4></center><hr style='border-width:2px;border-color:#75DFC1'>", unsafe_allow_html=True)
    
    
# Load the data
@st.cache_data
def load_data():
    data_path = os.path.join(os.path.dirname(__file__), 'pacificdatavizchallenge_fruit_cleaned_data.csv')
    data = pd.read_csv(data_path)
    data['mois'] = data['mois'].apply(lambda x: calendar.month_name[x])    
    return data
   
def load_data_prix():
    data_path = os.path.join(os.path.dirname(__file__), 'echantillon_prix_produits_pacific_all_years1.csv')
    data_prix = pd.read_csv(data_path)
    data_prix.drop("Unnamed: 0", axis=1, inplace=True)
    return data_prix

data = load_data()
df = load_data_prix()


# Products most frequently surveyed using 'regroupement1' column
most_frequent_products = data['regroupement1'].value_counts().head(20)

# Products with the highest average values using 'regroupement1' column
average_values = data.groupby('regroupement1')['valeur_moy'].mean().sort_values(ascending=False).head(20)

# Theme for the plots
sns.set_theme()

if choice == "Accueil":
    display_header_info()
    st.write("Bienvenue sur la page d'accueil.")
    
    # Chargement et affichage de l'image
    # Créez trois colonnes : une colonne vide à gauche, une colonne centrale pour l'image, et une colonne vide à droite
    col1, col2, col3 = st.columns([1,1,1])
    
    # Affichez l'image dans la colonne centrale
    with col2:
        st.image("https://btchekeli.github.io/src/My_logos/profil_linkedin.jpg", use_column_width=False, width=250)

    
    st.info("""
    👋 **Bonjour, Chers Passionnés de la Data!**

    Je suis **Brunel TCHEKELI**, un passionné du numérique et du monde infini des données. Mon parcours académique riche et diversifié m'a permis de me forger une expertise solide dans le domaine de la data. Je suis titulaire d'un Master 2 en Humanités Numériques, spécialité Data Mining de l'Université Lumière Lyon 2, d'un second Master en Data Analyse de l'école des mines ParisTech, co-certifié par Datascientest, sans oublier une maîtrise en Veille Technologique et Innovation. 

    💫 **Une Opportunité Saisie** - Lorsque j'ai découvert le PacificDatavizChallenge 2023, j'ai immédiatement su que c'était le moment de montrer ce que je peux accomplir. En plein recherche de travail, je suis prêt à mettre mes compétences approfondies à votre service, maîtrisant des outils tels que Power BI, Qlik, Looker, Streamlit, ainsi que les fondamentaux d'Azure et de Google Cloud Platform, Python, R, XML et HTML.

    📜 **Ma Philosophie** - mon poème préféré, "Invictus", je suis le maître de mon destin, le capitaine de mon âme... ; Ma citation préférée ? "La donnée est l’actif stratégique de la révolution numérique", cette citation résonne profondément en moi, guidant chaque projet sur lequel je travaille. 

    🤝 **Partenariat et Collaboration** - Je vous invite à me rejoindre dans cette aventure exaltante, où ensemble, nous pouvons façonner l'avenir de la visualisation de données. Je suis non seulement là pour participer, mais pour connecter, collaborer et innover.

    🌐 **Rendez-vous dans les pages suivantes !** - Suivez mon parcours, où je transformerai des données brutes en récits visuels percutants et captivants. À très bientôt dans ce terrain fertile de créativité et d'innovation!

    🔗 *Restez à l'écoute pour des mises à jour, des aperçus et bien plus encore! Au plaisir de vous retrouver au PacificDatavizChallenge 2024!*
    """)
    
    st.divider()

    st.info("""
    **Plongée dans la Nouvelle-Calédonie : Un Défi de Dataviz Interactive**
    
     Plus qu'un simple challenge, c'était une occasion d'explorer et de présenter des données d'une manière qui pourrait raconter une histoire, offrir des perspectives, et surtout, être interactive. Et c'est exactement ce que j'ai décidé de faire en m'inscrivant dans la catégorie "Dataviz interactive".
    
    **Python & Streamlit : Un Duo Puissant**
    
    Ma décision de me baser sur le langage de programmation Python pour ce challenge était assez naturelle. Python, avec sa versatilité et ses bibliothèques robustes, offre une pléthore d'outils pour travailler avec des données. Mais le véritable atout dans mon arsenal a été la bibliothèque Streamlit. Streamlit a transformé ma capacité à créer des applications de visualisation de données interactives avec une facilité déconcertante.
    
    **Exploration des Données : Deux Perspectives Uniques**
    
    J'ai choisi de travailler avec deux jeux de données distincts mais intrinsèquement liés à la Nouvelle-Calédonie : **"Prix des produits alimentaires en Nouvelle-Calédonie"** et **"Marché des fruits et légumes en Nouvelle-Calédonie"**. Ces datasets offrent un aperçu fascinant de l'économie et des tendances alimentaires de la région.
    
    Sur ma plateforme, vous remarquerez que les sections **"exploration des données"** et **"analyse et dataviz"** sont soigneusement structurées avec deux onglets distincts. Selon votre intérêt, vous pouvez choisir entre les deux jeux de données. Si vous êtes curieux de connaître les tendances du marché des fruits et légumes, cliquez simplement sur l'onglet 'Marché des fruits et légumes'. Pour une analyse approfondie des prix des produits alimentaires, dirigez-vous vers 'Prix des produits alimentaires'.
    
    **L'Art de la Visualisation avec Python**
    
    La beauté d'une visualisation réside dans sa capacité à transmettre des informations complexes d'une manière simple et esthétiquement plaisante. J'ai utilisé une combinaison de bibliothèques Python pour atteindre cet équilibre. Matplotlib et Seaborn ont été mes alliés de confiance pour les graphiques traditionnels, tandis que Plotly m'a permis d'ajouter une dimension interactive à mes visualisations. Et pour ajouter une touche artistique, j'ai incorporé des nuages de mots via la bibliothèque WordCloud, offrant une perspective différente et engageante sur les données.
    
    
    D'une manière générale, ce challenge a été une expérience d'apprentissage et de découverte. En fusionnant la puissance de Python avec la magie de la visualisation interactive, j'espère offrir aux visiteurs une perspective unique sur la Nouvelle-Calédonie et ses tendances alimentaires. Je vous invite à explorer, interagir et plonger dans le monde fascinant de la dataviz !
    """)
    
    st.divider()
    st.header("Mon poème préféré **Invictus** ")
    st.success("""
     
    Dans les ténèbres qui m’enserrent,  
    Noires comme un puits où l’on se noie,  
    Je rends grâce aux dieux quels qu’ils soient,  
    Pour mon âme invincible et fière,  

    Dans de cruelles circonstances,  
    Je n’ai ni gémi ni pleuré,  
    Meurtri par cette existence,  
    Je suis debout bien que blessé,  

    En ce lieu de colère et de pleurs,  
    Se profile l’ombre de la mort,  
    Et je ne sais ce que me réserve le sort,  
    Mais je suis et je resterai sans peur,  

    Aussi étroit soit le chemin,  
    Nombreux les châtiments infâmes,  
    Je suis le maître de mon destin,  
    Je suis le capitaine de mon âme.  
    *William Ernest Henley*
    """)
    
    st.divider()
    st.subheader("Le PacificDatavizChallenge 2023 est Organisé par : ")
    col1, col2 = st.columns(2)
    with col1: 
        credit_text = "Crédit : [Communauté du Pacifique](https://spc.int)"
        
        image_path = os.path.join(os.path.dirname(__file__), "img", "SPC-CPS-logo_27_stars-2023.png")
        img = Image.open(image_path)
        st.image(img)
        st.markdown(credit_text, unsafe_allow_html=True)
    with col2:
        credit_text = "Crédit : [Gouvernement de la Nouvelle Calédonie](https://gouv.nc)"
        image_path = os.path.join(os.path.dirname(__file__), "img", "gouv-nc-color.png")
        img = Image.open(image_path)
        st.image(img)
        st.markdown(credit_text, unsafe_allow_html=True)

    st.markdown("""  """, unsafe_allow_html=True )
elif choice == "Exploration des données":
    
    display_header_info()
    st.info("Choisissez un onglet pour afficher les analyses concernant ce jeu de données : Pour les données concernant le marché des fruits et légumes choisissez 'Marché des fruits et légumes',  pour les données concernant le prix des produits alimentaires cliquez sur 'Prix des produits alimentaires'")
    tab1, tab2, tab3 = st.tabs(["**Prix des produits alimentaires**","D-----------------------------------------------------------C","**Marché des fruits et légumes**"])
    with tab1:
        st.header(" Prix des produits alimentaires en Nouvelle-Calédonie")
        st.divider()
        st.markdown("""
                    L'étape d'exploration pour ce jeux de données consistait simplement à néttoyer le jeux de données de facon à avoir un dataset de qualité. 
                    
                    Tout d'abord, il faut faire remarquer que ce jeux de données est très très lourd et pèse dans les 2 Go, une fois le fichier de 840 Mo dézipé. Il est donc impossible de charger le jeu de données en mémoire et de travailler avec, bien que ceci pourrait être fait avec dask (Une librairie qui permet de charger des jeux de données volumineux sans utiliser la mémoire de l'appareil).
                    
                    j'ai donc décidé de prendre un échantillon (0.01%) du jeux de données "Prix des produits alimentaires en Nouvelle-Calédonie de 2012 à 2023". l'échantillon retenue contenait cependant plus de 5000 lignes choisi au hasard par la fonction "skiprows"
                    
                    """)
        code = """
        import random
        
        # Définir la probabilité de sauter une ligne
        probability_of_skip = 1 - (5300/52290713)
        
        def skip_function(i):
            if i == 0:  # Assurez-vous de ne pas sauter l'en-tête
                return False
            return random.random() < probability_of_skip
        
        # Charger les données en utilisant la fonction skip_function
        sample_data_with_skiprows = pd.read_csv("extraction_filtre_sous_secteurs.csv", skiprows=skip_function)
        
        # Vérifier le nombre de lignes obtenues
        sample_data_with_skiprows.to_csv("echantillon_prix_produits_pacific_all_years.csv")
        
        
        """        
        st.code(code, language='python')
        st.markdown(""" 
                    Ainsi, l'échantillon est sauvegardé puis chargé directement pour les besoins de la visualisation.
                    
                    En ce qui concerne les doublons et les données manquantes, elles ont été tout simplement supprimés
                    
                    
                    """)
        st.write("- **Voyons à quoi ressemble le jeu de données chargé :**", df)
        st.write("- **Notre jeu de données chargé contient :**", df.shape[0], "**lignes et**", df.shape[1], "**colonnes**")
        st.write("- **Liste des colonnes**",df.columns.to_list())
        st.write("- **Description du jeu de données avec describe() :**", df.describe().T)
        st.warning("**J'aurai pu développer et enrichir cette partie exploration par certains graphique de visualisation mais j'ai préféré tout afficher dans la partie 'Analyse et dataviz'**.")

    with tab2:       
        st.warning("Il n'y a rien ici. Veuillez choisir entre 'Prix des produits alimentaires' et 'Marché des fruits et légumes en Nouvelle-Calédonie' ")
        st.info("Cet onglet (tab) est la à titre de séparateur entre les deux autres")
    
    with tab3:
        st.header("Marché des fruits et légumes en Nouvelle-Calédonie")
        st.divider()
        st.markdown("""
                    En ce qui concerne l'étape d'exploration pour le jeux de données "Marché des fruits et légumes en Nouvelle-Calédonie" consistait simplement à néttoyer le jeux de données de facon à avoir un dataset de qualité. 
                    
                    Contrairement au dataset "prix", ce jeux de données est utilisé tel quel sans besoin de constituer un échantillon.
                    
                   Pour plus de 5000 lignes, le dataset contenait entre 12 et 300 lignes de données manquantes pour les collonnes qui m'intéressent pour la visualisation. Ces lignes sont tout simplement supprimées.
                   """)
        
        
        st.write("- **Voyons à quoi ressemble le jeu de données chargé :**", data)
        st.write("- **Notre jeu de données chargé contient :**", data.shape[0], "**lignes et**", data.shape[1], "**colonnes**")
        st.write("- **Liste des colonnes**",data.columns.to_list())
        st.write("- **Description du jeu de données avec describe() :**", data.describe().T)
        st.warning("**J'aurai pu développer et enrichir cette partie exploration par certains graphique de visualisation mais j'ai préféré tout afficher dans la partie 'Analyse et dataviz'**.")
       
elif choice == "Analyses et dataviz":
    display_header_info()
    st.write("Visualisations des données.")
        
    
    st.info("Choisissez un onglet pour afficher les analyses concernant ce jeu de données : Pour les données concernant le marché des fruits et légumes choisissez 'Marché des fruits et légumes',  pour les données concernant le prix des produits alimentaires cliquez sur 'Prix des produits alimentaires'")
    tab1, tab2, tab3 = st.tabs(["**Prix des produits alimentaires**","D-----------------------------------------------------------C","**Marché des fruits et légumes**"])
    with tab1:
        st.header(" Prix des produits alimentaires en Nouvelle-Calédonie")
        plot_choice = st.selectbox("Choisissez le type de visualisation:", ['Carte des Prix', "Boxplots","Wordclouds",
                                    "Histogramme des prix",  "Top Marques les Plus Courantes", 
                                    "Répartition des Produits par Catégorie", "Variabilité de Prix", "Top Points de Vente", 
                                    "Correlation entre les variables", "Répartition des produits en Promotion",
                                    "Evolution annuelle prix des produits courants", "Prix Moyens au Fil du Temps"])
        
        if plot_choice == 'Carte des Prix':
            # Créer une carte interactive avec Plotly pour visualiser les points de vente
            fig = px.scatter_mapbox(df, 
                                    lat="LATITUDE", 
                                    lon="LONGITUDE", 
                                    hover_name="RAISON_SOCIALE", 
                                    hover_data=["PRIX_RELEVE", "NOM"],
                                    color_discrete_sequence=["blue"],
                                    zoom=7, 
                                    height=700)
            
            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(title="Carte des Points de Vente (Géolocalisation)")
            st.plotly_chart(fig)
        
        elif plot_choice == "Boxplots":
            boxplot_to_plot = st.selectbox("Choisissez le Boxplot à afficher:", ["Distribution des Prix par Sous-Secteur de Consommation", "Prix relevé par département", 
                                             "Distribution des Prix par Promotion", "Distribution produits les Plus Courants"])
            
            if boxplot_to_plot == "Distribution des Prix par Sous-Secteur de Consommation" :
                fig = plt.figure(figsize=(10, 12))
                sns.boxplot(x='PRIX_RELEVE', y='SOUS_SECTEUR_CONSO', data=df, palette='pastel')
                plt.title('Distribution des Prix par Sous-Secteur de Consommation')
                plt.xlabel('Prix')
                plt.ylabel('Sous-Secteur de Consommation')
                plt.xlim(0, 4500)  # Limit the x-axis for better visualization
                plt.tight_layout()
                st.pyplot(fig)
                            
            elif boxplot_to_plot == "Prix relevé par département" :
                # Créer un graphique à boîtes pour comparer la distribution des prix entre les départements
                fig = plt.figure(figsize=(12, 7))
                sns.boxplot(x='DEPARTEMENT', y='PRIX_RELEVE', data=df, palette='pastel')
                plt.title('Distribution des Prix par Département')
                plt.xlabel('Département')
                plt.ylabel('Prix Relevé')
                plt.tight_layout()
                st.pyplot(fig)
                
            elif boxplot_to_plot == "Distribution des Prix par Promotion":
                fig = plt.figure(figsize=(12, 8))
                sns.boxplot(x='PROMOTION', y='PRIX_RELEVE', data=df)
                plt.title('Distribution des Prix par Promotion')
                plt.xlabel('Promotion')
                plt.ylabel('Prix Relevé')
                plt.xticks([0, 1], ['Non', 'Oui'])
                plt.tight_layout()
                st.pyplot(fig)
            elif boxplot_to_plot == "Distribution produits les Plus Courants":
                # Sélectionner les 10 produits les plus courants
                top_products = df['NOM'].value_counts().nlargest(10).index
                
                # Filtrer le dataframe pour ne garder que ces produits
                filtered_df_for_top_products = df[df['NOM'].isin(top_products)]
                
                # Visualiser la distribution des prix pour ces produits
                fig = plt.figure(figsize=(10, 8))
                sns.boxplot(x='PRIX_RELEVE', y='NOM', data=filtered_df_for_top_products, palette='pastel')
                plt.title('Distribution des Prix pour les 10 Produits les Plus Courants')
                plt.xlabel('Produit')
                plt.ylabel('Prix Relevé')
                plt.xticks(rotation=0)
                plt.tight_layout()
                st.pyplot(fig)


        elif plot_choice == "Wordclouds" :
            columns_for_wordcloud = ['NOM', 'MARQUE', 'FAMILLE_PRODUIT', 'SOUS_FAMILLE', 'SOUS_SECTEUR_CONSO', 'RAISON_SOCIALE']

            # Menu déroulant pour choisir la colonne pour le word cloud
            selected_column = st.selectbox(
                'Sélectionnez la colonne pour le Word Cloud',
                columns_for_wordcloud
            )
            
            # Générer et afficher le word cloud pour la colonne sélectionnée
            text = ' '.join(df[selected_column].dropna())
            wordcloud = WordCloud(background_color='white', width=800, height=400).generate(text)
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
        
        elif plot_choice == "Histogramme des prix" : 
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df['PRIX_RELEVE'], bins=50, kde=True, color='blue')
            plt.title('Distribution des Prix des Produits')
            plt.xlabel('Prix Relevé')
            plt.ylabel('Nombre de Produits')
            st.pyplot(fig)
          
        elif plot_choice == "Prix Moyens au Fil du Temps" :
            # Convertir la colonne DATE_RELEVE en format datetime
            df['DATE_RELEVE'] = pd.to_datetime(df['DATE_RELEVE'])
            
            # Calculer le prix moyen par mois
            avg_price_per_month = df.groupby(df['DATE_RELEVE'].dt.to_period("M")).mean()['PRIX_RELEVE']
            
            # Visualiser l'évolution des prix moyens au fil du temps
            fig = plt.figure(figsize=(14, 8))
            avg_price_per_month.plot(color='red')
            plt.title('Évolution des Prix Moyens au Fil des années')
            plt.xlabel('Date')
            plt.ylabel('Prix Moyen')
            plt.grid(True, which='both', linestyle='--', linewidth=0.5)
            plt.tight_layout()
            st.pyplot(fig)

        elif plot_choice == "Top Marques les Plus Courantes" :
            # Compter le nombre de produits par marque
            top_slider = st.slider("Selectionner un top 10 ou 15 etc :", 10, 30, 10)
            top_brands = df['MARQUE'].value_counts().head(top_slider)
            
            # Créer un graphique à barres pour les marques les plus courantes
            fig = plt.figure(figsize=(12, 7))
            sns.barplot(x=top_brands.values, y=top_brands.index, palette='viridis')
            plt.title(f"Top {top_slider} des Marques les Plus Courantes")
            plt.xlabel('Nombre de Produits')
            plt.ylabel('Marque')
            plt.tight_layout()
            st.pyplot(fig)
            
        elif plot_choice == "Répartition des Produits par Catégorie" :
            # Compter le nombre de produits par catégorie
            product_categories = df['SECTEUR_CONSO'].value_counts()
            
            # Créer un diagramme en secteur pour la répartition des produits par catégorie
            fig = plt.figure(figsize=(12, 7))
            explode = [0.1,0,0,0,0.1,0.2,0.2, 0.2, 0.2, 0.01] 
            product_categories.plot.pie(autopct='%1.1f%%', startangle=140, explode=explode, colors=sns.color_palette('pastel', len(product_categories)))
            plt.title('Répartition des Produits par Catégorie')
            plt.ylabel('')  # Pour enlever le nom de la colonne en tant que label y
            plt.tight_layout()
            st.pyplot(fig)
            
           
        elif plot_choice == "Répartition des produits en Promotion" :            
            fig = plt.figure(figsize=(8, 6))
            explode = [0, 0.2]
            labels = ["Pas en promotion (0)", "En promotion (1)"]
            df['PROMOTION'].value_counts().plot.pie(labels=labels, autopct='%1.1f%%', startangle=140, explode = explode, colors=sns.color_palette('pastel', 2))
            plt.title('Proportion de Produits en Promotion')
            plt.ylabel('')  # Pour enlever le nom de la colonne en tant que label y
            
            plt.tight_layout()
            st.pyplot(fig)
            
        elif plot_choice == "Variabilité de Prix":
            
            # Calculer le prix moyen et l'écart type pour chaque marque
            brand_price_stats = df.groupby('MARQUE')['PRIX_RELEVE'].agg(['mean', 'std']).reset_index()
            
            # Sélectionner les 10 marques ayant la plus grande variabilité de prix
            top_slider = st.slider("Selectionner un top 10 ou 15 etc :", 10, 30, 10)
            top_variable_brands = brand_price_stats.sort_values('std', ascending=False).head(top_slider)
            
            # Visualiser la variabilité des prix pour les marques sélectionnées
            fig= plt.figure(figsize=(14, 8))
            sns.barplot(x='MARQUE', y='std', data=top_variable_brands, palette='pastel')
            plt.title(f"Top {top_slider} Marques avec la Plus Grande Variabilité de Prix")
            plt.xlabel('Marque')
            plt.ylabel('Écart Type du Prix')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)

        elif plot_choice == "Top Points de Vente" :
            # Compter le nombre de produits par point de vente
            store_product_counts = df['RAISON_SOCIALE'].value_counts().head(10)
            
            # Calculer le prix moyen pour chaque point de vente
            top_slider = st.slider("Selectionner un top 10 ou 15 etc :", 10, 30, 10)
            store_avg_price = df.groupby('RAISON_SOCIALE')['PRIX_RELEVE'].mean().sort_values(ascending=False).head(top_slider)
            
            # Visualiser les points de vente avec le plus grand nombre de produits
            fig, ax = plt.subplots(2, 1, figsize=(12, 15))
            
            sns.barplot(x=store_product_counts.values, y=store_product_counts.index, palette='viridis', ax=ax[0])
            ax[0].set_title(f'Top {top_slider} Points de Vente avec le Plus Grand Nombre de Produits')
            ax[0].set_xlabel('Point de Vente')
            ax[0].set_ylabel('Nombre de Produits')
            ax[0].tick_params(axis='x', rotation=0)
            
            # Visualiser les points de vente avec le prix moyen le plus élevé
            sns.barplot(x=store_avg_price.values, y=store_avg_price.index, palette='viridis', ax=ax[1])
            ax[1].set_title(f'Top {top_slider} Points de Vente avec le Prix Moyen le Plus Élevé')
            ax[1].set_xlabel('Point de Vente')
            ax[1].set_ylabel('Prix Moyen')
            ax[1].tick_params(axis='x', rotation=0)
            
            plt.tight_layout()
            st.pyplot(fig)
                
        elif  plot_choice == "Correlation entre les variables": 
            # Calculer la matrice de corrélation
            correlation_matrix = df.corr()
            
            # Visualiser la matrice de corrélation avec une heatmap
            fig= plt.figure(figsize=(12, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
            plt.title('Matrice de Corrélation')
            plt.tight_layout()
            st.pyplot(fig)
            
        elif plot_choice == "Evolution annuelle prix des produits courants":
            # Convertir la colonne DATE_RELEVE en type datetime
            df['DATE_RELEVE'] = pd.to_datetime(df['DATE_RELEVE'])
        
            # Extraire l'année et créer une nouvelle colonne 'YEAR'
            df['YEAR'] = df['DATE_RELEVE'].dt.year
        
            # Sélectionner les 5 produits les plus courants
            top_slider = st.slider("Selectionner un top 10 ou 15 etc :", 10, 30, 5)
            top_products = df['NOM'].value_counts().nlargest(top_slider).index
        
            # Filtrer le dataframe pour ne garder que ces produits
            filtered_df_for_top_products = df[df['NOM'].isin(top_products)]
        
            # Calculer le prix moyen pour chaque année et chaque produit
            avg_price_per_year = filtered_df_for_top_products.groupby(['YEAR', 'NOM'])['PRIX_RELEVE'].mean().reset_index()
        
            # Visualiser l'évolution des prix pour ces produits au fil des années
            fig = plt.figure(figsize=(14, 8))
            sns.lineplot(x='YEAR', y='PRIX_RELEVE', hue='NOM', data=avg_price_per_year, marker='o', palette='pastel')
            plt.title(f'Évolution des Prix Moyens par Année pour les {top_slider} Produits les Plus Courants')
            plt.xlabel('Année')
            plt.ylabel('Prix Moyen')
            plt.legend(title='Produit')
            plt.tight_layout()
            st.pyplot(fig)

         
    with tab2:       
        st.warning("Il n'y a rien ici. Veuillez choisir entre 'Prix des produits alimentaires' et 'Marché des fruits et légumes en Nouvelle-Calédonie' ")
        st.info("Cet onglet (tab) est la à titre de séparateur entre les deux autres")
    with tab3:
        st.header("Marché des fruits et légumes en Nouvelle-Calédonie")
        # Dropdown for user to select the type of visualization
        plot_choice = st.selectbox("Choisissez le type de visualisation:", 
                                   ["Tendances temporelles", "graphique à barres empilées" , "Histogrammes", "Boxplots",
                                    "Heatmap des valeurs moyennes", "Corrélation entre les variables",
                                    "Produits les plus enquêtés", "Produits à valeur moyenne élevée", 
                                    "Répartition des produits", "Comparaison des tendances",
                                    "Distribution des valeurs moyennes", "Word cloud"])
    
        if plot_choice == "Tendances temporelles":
            
            # Convert the 'mois' column to a categorical type with proper order
            month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                           'August', 'September', 'October', 'November', 'December']
            data['mois'] = pd.Categorical(data['mois'], categories=month_order, ordered=True)
        
            # Letting the user select products for which they want to see the temporal trends
            # Get unique products and remove "AIL"
            unique_products = list(data['regroupement1'].unique())
            if "AIL" in unique_products:
                unique_products.remove("AIL")
            
            products_to_view = st.multiselect("Sélectionnez les produits à visualiser:", 
                                     sorted(unique_products),
                                     default=unique_products[:5])
    
        
            # If no product is selected, show trends for all products; else, filter by selected products
            if products_to_view:
                filtered_data_by_product = data[data['regroupement1'].isin(products_to_view)]
            else:
                filtered_data_by_product = data
        
            # Allow user to select one or multiple years
            selected_years = st.multiselect("Choisissez une ou plusieurs années:", 
                                            sorted(data['annee'].unique()), 
                                            default=[sorted(data['annee'].unique())[0]])
            
            if not selected_years:
                st.warning("Veuillez sélectionner au moins une année.")
            else:
                filtered_data = filtered_data_by_product[filtered_data_by_product['annee'].isin(selected_years)]
                filtered_data = filtered_data.groupby(['annee', 'mois', 'regroupement1'])[["valeur_moy", 'poids_enquete_kg', 'poids_mg_kg', 'valeur_tot_mg_fr']].sum().reset_index()
                
                # Sorting by month to ensure correct order
                filtered_data = filtered_data.sort_values(by=['annee', 'mois'])
        
                column_to_plot = st.selectbox("Choisissez la colonne à visualiser:", 
                                              ["valeur_moy", "poids_enquete_kg", "poids_mg_kg", "valeur_tot_mg_fr"])
                
                st.write(f"Tendance temporelle pour {column_to_plot} pour les années {', '.join(map(str, selected_years))}")
                fig, ax = plt.subplots(figsize=(14, 7))
                sns.lineplot(data=filtered_data, x='mois', y=column_to_plot, hue='regroupement1', ax=ax, palette="coolwarm", ci=None)
                st.pyplot(fig)
    
        
        elif plot_choice == "Produits les plus enquêtés":
            st.write("Produits les plus fréquemment enquêtés (top_20)")
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.countplot(y=data['regroupement1'], order=most_frequent_products.index, palette="viridis", ax=ax)
            st.pyplot(fig)
    
        elif plot_choice == "Produits à valeur moyenne élevée":
            st.write("Produits avec les valeurs moyennes les plus élevées (top_20)")
            fig, ax = plt.subplots(figsize=(14, 7))
            sns.barplot(y=average_values.index, x=average_values.values, palette="coolwarm", ax=ax)
            st.pyplot(fig)
        
    
        elif plot_choice == "Répartition des produits":
            pie_data = data.groupby('regroupement1')[['poids_enquete_kg', 'poids_mg_kg']].sum().sum(axis=1)
            top_pie_data = pie_data.sort_values(ascending=False).head(10)
            fig, ax = plt.subplots(figsize=(10, 7))
            top_pie_data.plot(kind='pie', explode=[0.1,0.1,0.1,0,0,0,0,0,0,0], autopct='%1.1f%%', ax=ax)
            st.write("Top 10")
            st.pyplot(fig)
    
        elif plot_choice == "Comparaison des tendances":
            available_products = data['regroupement1'].unique().tolist()
            default_products = [prod for prod in ['ANANAS', 'MELON', 'BANANE DESSERT'] if prod in available_products]
            products_to_compare = st.multiselect('Sélectionnez les produits à comparer', available_products, default=default_products)
            filtered_data = data[data['regroupement1'].isin(products_to_compare)]
            fig, ax = plt.subplots(figsize=(12, 7))
            sns.lineplot(data=filtered_data, x='annee', y='valeur_moy', hue='regroupement1', ci=None, ax=ax)
            
            show_confidence_interval = st.checkbox("Afficher l'intervalle de confiance", value=False)
    
            if show_confidence_interval:
                sns.lineplot(data=filtered_data, x='annee', y='valeur_moy')
                    
            st.pyplot(fig)
    
    
        elif plot_choice == "Distribution des valeurs moyennes":
            top_products_for_violin = data['regroupement1'].value_counts().head(20).index.tolist()
            filtered_data = data[data['regroupement1'].isin(top_products_for_violin)]
            fig, ax = plt.subplots(figsize=(14, 8))
            sns.violinplot(data=filtered_data, x='regroupement1', y='valeur_moy', palette="coolwarm", ax=ax)
            st.pyplot(fig)
            
            
        elif plot_choice == "Word cloud":
            wordcloud = WordCloud(background_color='white', colormap='viridis', max_words=50).generate_from_frequencies(data['regroupement1'].value_counts())
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
    
    
        elif plot_choice ==  "graphique à barres empilées" :
            
            import plotly.express as px

            # Letting the user select the metric to base the graph on
            metric_to_view = st.selectbox("Choisissez la métrique à visualiser:", ["valeur_moy", "poids_mg_kg", "poids_enquete_kg"])
            
            # Convert the 'mois' column to a categorical type with proper order
            month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                           'August', 'September', 'October', 'November', 'December']
            data['mois'] = pd.Categorical(data['mois'], categories=month_order, ordered=True)
            
            # Selecting top common products
            top_slider = st.slider("Selectionner un top 10 ou 15 etc :", 10, 30, 10)
            top_products = data['regroupement1'].value_counts().head(top_slider).index.tolist()
            
            # Filtering data for the top products
            stacked_data = data[data['regroupement1'].isin(top_products)]
            
            # Creating a pivot table for the stacked bar chart based on user's metric choice
            pivot_data = stacked_data.pivot_table(index='mois', columns='regroupement1', values=metric_to_view, aggfunc='sum').fillna(0).reset_index()
            
            # Plotting using Plotly Express
            fig = px.bar(pivot_data, x='mois', y=[col for col in pivot_data.columns if col != 'mois'],
                         title=f'Répartition de {metric_to_view} des produits par mois (Top {top_slider})',
                         labels={'value': metric_to_view, 'mois': 'Mois'},
                         height=500, width=900)
            
            fig.update_layout(barmode='stack', xaxis={'categoryorder':'array', 'categoryarray': month_order})
            
            st.plotly_chart(fig)


        elif plot_choice == "Histogrammes":
            column_to_plot = st.selectbox("Choisissez la colonne à visualiser:", 
                                       ["valeur_moy", "poids_enquete_kg", "poids_mg_kg", "valeur_tot_mg_fr"])
            bins_slider = st.slider("Nombre d'intervalle:", 10, 100, 30)
            st.write(f"Histogramme pour {column_to_plot}")
            fig, ax = plt.subplots()
            sns.histplot(data[column_to_plot], bins=bins_slider, kde=True, ax=ax, color=sns.color_palette("viridis", 10)[4])
            st.pyplot(fig)
         
        elif plot_choice == "Boxplots":
            column_to_plot = st.selectbox("Choisissez la colonne à visualiser:", 
                                       ["poids_enquete_kg", "poids_mg_kg", "valeur_tot_mg_fr", "valeur_moy"])
            st.write(f"Boxplot pour {column_to_plot}")
            fig, ax = plt.subplots()
            sns.boxplot(x=data[column_to_plot], ax=ax, color=sns.color_palette("muted", 1)[0])
            st.pyplot(fig)    
     
        elif plot_choice == "Corrélation entre les variables":
            correlation_data = data[['poids_enquete_kg', 'poids_mg_kg', 'valeur_tot_mg_fr', 'valeur_moy']].corr()
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(correlation_data, cmap="coolwarm", annot=True, ax=ax)
            st.pyplot(fig)
    
        elif plot_choice == "Heatmap des valeurs moyennes":
         
             # Convert the 'mois' column to a categorical type with proper order
            month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                        'August', 'September', 'October', 'November', 'December']
            data['mois'] = pd.Categorical(data['mois'], categories=month_order, ordered=True)
         
            heatmap_data = data.pivot_table(index="mois", columns="annee", values="valeur_moy", aggfunc="mean")
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".2f", linewidths=.5, ax=ax)
            st.pyplot(fig)

 
elif choice == "Ressources":
        image_path = os.path.join(os.path.dirname(__file__), "img", "ressources.jpg")
        img = Image.open(image_path)
        st.image(img)
        credit_text = "Crédit : [Les echos](https://www.lesechos.fr/2015/08/le-stock-mondial-de-ressources-renouvelables-samenuise-269495)"
        st.markdown(credit_text, unsafe_allow_html=True)
        st.subheader(" - En savoir plus sur le Pacific Dataviz Challenge 2023 : ")
        st.markdown('''- https://dataviz.pacificdata.org/fr/''', unsafe_allow_html=True)
        st.markdown(''' - https://www.spc.int/fr/a-l-agenda/the-pacific-dataviz-challenge-2023</a>''', unsafe_allow_html=True)
        st.markdown(''' - https://unc.nc/pacific-dataviz-challenge-2023-donnez-vie-aux-donnees/''', unsafe_allow_html=True)
        
        st.subheader(" Sources des jeux de données utilisés :")   
        st.markdown('''- <a target="blank" href="https://data.gouv.nc/explore/?flg=fr&amp;disjunctive.theme&amp;disjunctive.publisher&amp;disjunctive.keyword&amp;disjunctive.attributions&amp;disjunctive.license&amp;sort=explore.popularity_score&amp;refine.keyword=PacificDatavizChallenge2023&amp;refine.attributions=+Direction+des+Affaires+V%C3%A9t%C3%A9rinaires,+Alimentaires+et+Rurales+(DAVAR)">Marché des fruits et légumes en Nouvelle-Calédonie</a>''', unsafe_allow_html=True)
        st.markdown('''- <a target="_blank" href="https://data.gouv.nc/explore/?flg=fr&amp;disjunctive.theme&amp;disjunctive.publisher&amp;disjunctive.keyword&amp;disjunctive.attributions&amp;disjunctive.license&amp;sort=explore.popularity_score&amp;refine.attributions=Direction%20des%20Affaires%20%C3%89conomiques%20(DAE)&amp;refine.keyword=PacificDatavizChallenge2023">Prix des produits alimentaires en Nouvelle-Calédonie</a>''', unsafe_allow_html=True)

        st.subheader(" Code streamlit et notebook :")
        st.info("L'ensemble des codes, données et notebooks utilisés pour la création de ce site est disponible dans mon Github à l'adresse suivante : https://github.com/btchekeli/Data-Analyse/tree/main/PacificDatavizChallenges")
        
        st.subheader("Organisateurs : ")
        col1, col2 = st.columns(2)
        with col1: 
            credit_text = "Crédit : [Communauté du Pacifique](https://spc.int)"
            image_path = os.path.join(os.path.dirname(__file__), "img", "SPC-CPS-logo_27_stars-2023.png")
            img = Image.open(image_path)
            st.image(img)
            st.markdown(credit_text, unsafe_allow_html=True)
        with col2:
            credit_text = "Crédit : [Gouvernement de la Nouvelle Calédonie](https://gouv.nc)"
            image_path = os.path.join(os.path.dirname(__file__), "img", "gouv-nc-color.png")
            img = Image.open(image_path)
            st.image(img)
            st.markdown(credit_text, unsafe_allow_html=True)


# Note: 
#""" Pour sauvegarder les requirement.txt sur windows,  utilisez la commande suivante :
#    pip freeze | findstr /R "streamlit pandas seaborn matplotlib calendar wordcloud plotly" > requirements.txt
#"""
