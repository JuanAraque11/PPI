# Librerías de terceros
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial as spt
import streamlit as st
import geopandas as gpd
import plotly.express as px
import plotly.graph_objs as go


url = "https://raw.githubusercontent.com/JuanAraque11/ppi_dai_ECHAVARRIAjj/main/Un_mundo_en_tu_plato/Datos/restaurantes.csv"

# Cargar el dataset a partir de la ruta establecida
datos = gpd.read_file(url, sep=",")

# Convertir las columnas de latitud y longitud a tipo numérico
datos['Latitude'] = pd.to_numeric(datos['Latitude'])
datos['Longitude'] = pd.to_numeric(datos['Longitude'])
datos['Price range'] = pd.to_numeric(datos['Price range'])
datos['Aggregate rating'] = pd.to_numeric(datos['Aggregate rating'])
datos['Votes'] = pd.to_numeric(datos['Votes'])
datos['Restaurant Name'] = datos['Restaurant Name'].astype('string')
datos['Address'] = datos['Address'].astype('string')

# Eliminar las columnas de latitud y longitud con valores nulos
datos = datos[(datos['Longitude'] != 0) | (datos['Latitude'] != 0)]

Noida = datos[datos['City'] == 'Noida']
Noida = Noida[Noida['Longitude'] != 0.0]

NewDelhi = datos[datos['City'] == 'New Delhi']
NewDelhi = NewDelhi[NewDelhi['Longitude'] != 34.0]

Gurgaon = datos[datos['City'] == 'Gurgaon']
Faridabad = datos[datos['City'] == 'Faridabad']
Ghaziabad = datos[datos['City'] == 'Ghaziabad']



def triangulacion(df):
    """ Muestra la triangulación de Delaunay de un dataframe.

    Args: df: DataFrame

    Returns: None
    """

    st.write("Triangulación de Delaunay")
    points = df[['Longitude', 'Latitude']].to_numpy()

    # Aplicar la triangulación de Delaunay
    triangulation = spt.Delaunay(points)

    # Graficar la triangulación de Delaunay
    plt.triplot(points[:, 0], points[:, 1], triangulation.simplices)

    # Mostrar los vertices
    plt.plot(points[:, 0], points[:,1], '*')

    plt.xlabel('Longitud')
    plt.ylabel('Latitude')
    plt.title('Triangulación de Delaunay')
    st.pyplot(plt)

    # Limpiar la figura para evitar problemas con gráficos futuros
    plt.clf()


def casco(df):
    """ Muestra el casco convexo de los puntos de un dataframe.

    Args: df: DataFrame

    Returns: None
    """

    st.write("Casco Convexo")
    points = df[['Longitude', 'Latitude']].to_numpy()
    # Calcular el casco convexo
    casco = spt.ConvexHull(points)
    puntos_casco = casco.simplices

    # Graficar el casco convexo
    for s in puntos_casco:
        plt.plot(points[s, 0], points[s, 1], 'k-')

    # Graficar los puntos originales
    plt.plot(points[:,0], points[:,1], 'o')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Casco Convexo')
    st.pyplot(plt)

    # Limpiar la figura para evitar problemas con gráficos futuros
    plt.clf()


def graficar_mapa(df):
    fig = px.scatter_mapbox(df, 
                            lat="Latitude", 
                            lon="Longitude",
                            hover_name="Restaurant Name",
                            hover_data={"Address": True}, 
                            zoom=10, 
                            height=600)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(title="Mapa de Restaurantes")
    
    return fig

def elegir_restaurantes():
    """ 
    Muestra una interfaz de usuario para elegir una una ciudad.

    Args: None

    Returns: None
    """

    st.title("Elegir ciudad para ver restaurantes.")
    seleccion_ciudad = st.selectbox("Selecciona la ciudad:", ['New Delhi',
                                                              'Gurgaon',
                                                              'Noida',
                                                              'Faridabad',
                                                              'Ghaziabad'])
    
    if st.button("Buscar"):
        if seleccion_ciudad == 'New Delhi':
            mapa = graficar_mapa(NewDelhi)
            st.title(f"Mapa interactivo de restaurantes en {seleccion_ciudad}")
            st.plotly_chart(mapa)

            st.title(f"Otros datos estadisticos de {seleccion_ciudad}")
            triangulacion(NewDelhi)
            casco(NewDelhi) 

        elif seleccion_ciudad == 'Gurgaon':
            mapa = graficar_mapa(Gurgaon)
            st.title(f"Mapa interactivo de restaurantes en {seleccion_ciudad}")
            st.plotly_chart(mapa)
            
            st.title(f"Otros datos estadisticos de {seleccion_ciudad}")
            triangulacion(Gurgaon)
            casco(Gurgaon)

        elif seleccion_ciudad == 'Noida':
            mapa = graficar_mapa(Noida)
            st.title(f"Mapa interactivo de restaurantes en {seleccion_ciudad}")
            st.plotly_chart(mapa)

            st.title(f"Otros datos estadisticos de {seleccion_ciudad}")
            triangulacion(Noida)
            casco(Noida)

        elif seleccion_ciudad == 'Faridabad':
            mapa = graficar_mapa(Faridabad)
            st.title(f"Mapa interactivo de restaurantes en {seleccion_ciudad}")
            st.plotly_chart(mapa)

            st.title(f"Otros datos estadisticos de {seleccion_ciudad}")
            triangulacion(Faridabad)
            casco(Faridabad)

        elif seleccion_ciudad == 'Ghaziabad':
            mapa = graficar_mapa(Ghaziabad)
            st.title(f"Mapa interactivo de restaurantes en {seleccion_ciudad}")
            st.plotly_chart(mapa)

            st.title(f"Otros datos estadisticos de {seleccion_ciudad}:")
            triangulacion(Ghaziabad)
            casco(Ghaziabad)