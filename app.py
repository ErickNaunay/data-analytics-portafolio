import streamlit as st
import pandas as pd
import sidetable as stb
import plotly.express as px

st.title("_DA Portafolio_ de :blue[Erick Naunay] :sunglasses:")
st.write('Analisis exploratorio inicial:')

raw_data = pd.read_csv('datasets/movie_metadata.csv')

st.write('Revisar primeras filas:')
st.dataframe(raw_data.head())

st.write('Revisar primeras valores ausentes:')
st.dataframe(raw_data.stb.missing(style=True))

boton_barras = st.button('Crear grafico de barras sobre puntaje de imdb', type='primary')

if boton_barras:
    st.bar_chart(raw_data['imdb_score'])

boton_histograma= st.button('Crear grafico de histograma sobre puntaje de imdb')

if boton_histograma:
    fig = px.histogram(raw_data, x='imdb_score')

    st.plotly_chart(fig)

