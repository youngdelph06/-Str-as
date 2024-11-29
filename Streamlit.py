import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration de Seaborn pour une meilleure esthétique
sns.set(style="whitegrid")

# Affichage de l'uploader dans l'application Streamlit
file = st.file_uploader("Importer vos données ici", type=["csv"])

# Vérification si un fichier a été téléchargé
if file is not None:
    # Traitement du fichier téléchargé
    df = pd.read_csv(file)
    
    # Affichage des 5 premières lignes du DataFrame
    st.write("Aperçu des données :")
    st.dataframe(df.head())
    
    # Analyse simple - Statistiques descriptives
    st.write("Statistiques descriptives :")
    st.write(df.describe())

    # Sélection d'une colonne pour la visualisation (assurez-vous que la colonne existe)
    column_to_plot = st.selectbox("Choisissez une colonne à visualiser :", df.columns)

    # Création d'un graphique
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column_to_plot], bins=30, kde=True)  # Histogramme avec estimation de densité
    plt.title(f'Histogramme de {column_to_plot}')
    plt.xlabel(column_to_plot)
    plt.ylabel('Fréquence')

    # Affichage du graphique dans Streamlit
    st.pyplot(plt)