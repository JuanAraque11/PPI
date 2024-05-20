# Librerías de terceros
import pandas as pd
import streamlit as st


# Guardar en la variable 'ruta' la url del dataset
ruta = "https://raw.githubusercontent.com/JuanAraque11/ppi_dai_ECHAVARRIAjj/main/Un_mundo_en_tu_plato/Datos/recetas.csv"

# Cargar el dataset a partir de la ruta establecida
data = pd.read_csv(ruta, delimiter="|")

def reemplazar_nulos():
    """
    Reemplaza los valores nulos de la base de datos.

    Args: None

    Returns: None 
    """
    data['Ingredientes'] = data['Ingredientes'].fillna('')
    data['Valoracion'] = data['Valoracion'].fillna(0)
    data['Dificultad'] = data['Dificultad'].fillna('media')
    data['Tipo'] = data['Tipo'].fillna('Entrante')
    data['Tiempo'] = data['Tiempo'].fillna('30m')

reemplazar_nulos()

def mostrar_receta_aleatoria():
    """
    Muestra una receta al azar de la base de datos.

    Args: None

    Returns: None
    """
    aleatoria = st.button("Buscar una receta al azar")

    if aleatoria:
        receta_aleatoria = data.sample()

        # Mostrar la información de la receta aleatoria seleccionada
        st.write(f"Nombre: {receta_aleatoria['Nombre'].values[0]}")
        st.write(f"Tiempo: {receta_aleatoria['Tiempo'].values[0]}")
        st.write(f"Ingredientes: {receta_aleatoria['Ingredientes'].values[0]}")
        st.write(f"Link de la Receta: {receta_aleatoria['Link_receta'].values[0]}")


def buscar_receta_por_ingrediente(ingrediente):  
    """
    Busca recetas por el ingrediente especificado.

    Args: ingrediente (str): El ingrediente a buscar.  
    
    Returns: None
    """

    recetas_filtradas = data[data['Ingredientes'].str.contains(ingrediente)]
    recetas_filtradas
    return recetas_filtradas


def buscar_por_valoracion(valoracion, opcion):
    """
    Busca recetas según la valoración especificada.

    Args:
    - valoracion (float): Valor de la valoración a buscar.
    - opcion (str): Opción de búsqueda ('mayores', 'menores' o 'iguales').

    Returns:
    - DataFrame: DataFrame con las recetas que cumplen con los criterios de búsqueda.
    """

    # Filtrar recetas según la opción seleccionada
    if opcion == 'mayores':
        recetas_filtradas = data[data['Valoracion'] > valoracion]
    elif opcion == 'menores':
        recetas_filtradas = data[(data['Valoracion'] < valoracion) & 
         (data['Valoracion'] != 0)]
    elif opcion == 'iguales':
        recetas_filtradas = data[data['Valoracion'] == valoracion]
    elif opcion == 'sin valoración':
        recetas_filtradas = data[data['Valoracion'] == 0]
    else:
        st.error("Opción de búsqueda no válida. Las opciones válidas son\
                  'mayores', 'menores' o 'iguales'.")
        return None
    
    return recetas_filtradas
