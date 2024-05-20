# Librerías de terceros
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Librerías propias
from recetas import data


def distri_categorias():
    """
    Muestra una gráfica de barras de las categorías de las recetas.

    Args: None

    Returns: None
    """
    st.write("Distribución de categorías:")
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Categoria', data=data,
                  order=data['Categoria'].value_counts().index)
    plt.title('Distribución de Categorías')
    plt.xlabel('Frecuencia')
    plt.ylabel('Categoría')
    
    st.pyplot(plt)

    # Limpiar la figura para evitar problemas con gráficos futuros
    plt.clf()


def distri_valoraciones():
    """
    Muestra una gráfica de barras de las valoraciones de las recetas.

    Args: None

    Returns: None
    """
    st.write("Distribución de valoraciones:")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Valoracion'], bins=20, kde=True)
    plt.title('Distribución de Valoraciones')
    plt.xlabel('Valoración')
    plt.ylabel('Frecuencia')
    
    st.pyplot(plt)

    # Limpiar la figura para evitar problemas con gráficos futuros
    plt.clf()


def valoracion_por_dificultad():
    """
    Muestra una gráfica de barras de la valoración por la dificultad de las
    recetas.

    Args: None

    Returns: None
    """
    st.write("Valoración por la dificultad:")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Dificultad', y='Valoracion', data=data)
    plt.title('Valoración por la Dificultad')
    plt.xlabel('Dificultad')
    plt.ylabel('Valoración')
    
    st.pyplot(plt)

    # Limpiar la figura para evitar problemas con gráficos futuros
    plt.clf()


def top_recetas_reviews():
    """
    Muestra las 10 recetas con más valoraciones.

    Args: None

    Returns: None
    """
    st.write("Top 10 recetas con más valoraciones:")
    top_reviews = data.nlargest(10, 'Num_reviews')
    plt.figure(figsize=(10, 6))
    sns.barplot(y='Nombre', x='Num_reviews', data=top_reviews,
                palette='Purples_d')
    plt.title('Top 10 Recetas con Más Reviews')
    plt.xlabel('Número de Reviews')
    plt.ylabel('Nombre de la Receta')
    st.pyplot(plt)

    # Limpiar la figura para evitar problemas con gráficos futuros
    plt.clf()


def top_recetas_comentadas():
    """ 
    Muestra las 10 recetas con más comentarios.

    Args: None

    Returns: None
    """
    st.write("Top 10 recetas con más comentarios:")
    top_comentadas = data.nlargest(10, 'Num_comentarios')
    plt.figure(figsize=(10, 6))
    sns.barplot(y='Nombre', x='Num_comentarios', data=top_comentadas,
                palette='viridis')
    plt.title('Top 10 Recetas Más Comentadas')
    plt.xlabel('Número de Comentarios')
    plt.ylabel('Nombre de la Receta')
    st.pyplot(plt)

    # Limpiar la figura para evitar problemas con gráficos futuros
    plt.clf()