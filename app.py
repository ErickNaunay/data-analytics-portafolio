import streamlit as st
import pandas as pd
import sidetable as stb
import plotly.express as px

st.title("_DA Portafolio_ de :blue[Erick Naunay] :sunglasses:")
st.header('Analisis exploratorio inicial:')

raw_data = pd.read_csv('datasets/movie_metadata.csv')

st.subheader('Total de filas en el dataframe:')
st.write(len(raw_data))

st.subheader('Tipos de datos de las columnas:')
st.dataframe(raw_data.dtypes.rename('datatype'))

st.subheader('Revisar primeras filas:')
st.dataframe(raw_data.head())

st.subheader('Revisar ultimas filas:')
st.dataframe(raw_data.tail())

st.subheader('Revisar valores ausentes:')
st.dataframe(raw_data.stb.missing(style=True))

st.subheader('Revisar filas duplicados:')
st.write('El numero de filas duplicadas es: {}'.format(raw_data.duplicated().sum()))

st.subheader('Estadisticas descriptivas de los datos numericos:')
st.dataframe(raw_data.describe())

st.header('Limpieza y curacion de los datos')

with st.echo():

    clean_data = raw_data.drop_duplicates()

    clean_data['gross'].interpolate(method='polynomial', order=5, inplace=True)

    clean_data.dropna(inplace=True)

    clean_data.drop('color', axis=1, inplace=True)

    clean_data.reset_index(drop=False, inplace=True)

st.subheader('Total de filas en el dataframe:')
st.write(len(clean_data))

st.subheader('Revisar valores ausentes:')
st.dataframe(clean_data.stb.missing(style=True))

st.subheader('Revisar filas duplicados:')
st.write('El numero de filas duplicadas es: {}'.format(clean_data.duplicated().sum()))

st.header('Analisis Exploratorio')

dimension_selection = st.selectbox(
    'Selecciona la dimension a comparar con el GROSS',
    ('cast_total_facebook_likes', 'imdb_score', 'movie_facebook_likes')
)

#st.write('El usurio selecciono: {}'.format(dimension_selection))

st.scatter_chart(clean_data, x='gross', y=dimension_selection)

ventas_por_categoria = {}

for index, fila in clean_data.iterrows():
    
    for genero in fila['genres'].split('|'):
        
        genero_limpio = genero.strip()

        if genero_limpio not in ventas_por_categoria:
            ventas_por_categoria[genero_limpio] = 0
        
        ventas_por_categoria[genero_limpio] += fila['gross']

ventas_por_categoria_df = pd.DataFrame(list(ventas_por_categoria.items()), columns=['genero', 'gross'])

st.dataframe(ventas_por_categoria_df)


