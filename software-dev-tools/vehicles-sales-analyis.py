import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

from data_wrangling import Limpiador

def main():
    datos_raw = pd.read_csv('.datasets/movie_metadata.csv')
    
    limpiador = Limpiador('limpiador de peliculas', datos_raw)

    print(datos_raw.isna().sum())

    datos_clean = limpiador.clean()

    print(datos_clean.isna().sum())

    print(datos_clean.info())

    boton_histograma = st.button('Click aqui para dibujar el histograma')

    if boton_histograma:

        print(datos_clean.info())

        fig = px.histogram(datos_clean, 'movie_facebook_likes')

        st.plotly_chart(fig)


if __name__ == '__main__':
    main()