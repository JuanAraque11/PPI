# Librerías de terceros
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Librerías propias
from recetas import data, reemplazar_nulos
from restaurantes import datos
import streamlit as st # type: ignore
import pandas as pd

def extraer_codigo_iso(pais):
    '''
    Esta función extrae el código ISO 3166-1 alfa-2 de un país dado por el usuario.
    args:
        pais (str): nombre del país
    returns:
        codigo_iso (str): código ISO 3166-1 alfa-2 del país
        None (None): si no se encuentra el código ISO
    '''
    # URL de la página que contiene la lista de códigos ISO 3166-1
    url = "https://es.wikipedia.org/wiki/ISO_3166-1"

    # Leer las tablas de la página
    tablas = pd.read_html(url)

    # Intentar encontrar la tabla correcta
    for i, tabla in enumerate(tablas):
        if 'Nombre común' in tabla.columns:
            iso_table = tabla
            break
    else:
        return None

    # Renombramos las columnas basándonos en la estructura esperada
    iso_table = iso_table[['Nombre común', 'Código alfa-2', 'Código alfa-3', 'Código numérico']]

    # Buscar el país en la columna 'Nombre común'
    for fila in iso_table.itertuples(index=False):
        if str(pais).lower() in str(fila[0]).lower():
            return fila[1].strip()

    # Si no se encontró el país, devolver None
    return None

def mostrar_inicio():
    """
    Muestra el contenido de la página de inicio.

    Args: None

    Returns: None
    """
    st.write("Bienvenido al Inicio")
    st.write("Aquí encontrarás información sobre las funciones de la página:")
    st.write("- Guardar Recetas: Permitirá a los usuarios guardar nuevas\
              recetas en su cuenta.")
    st.write("- Consultar Información de los Platos: Proporciona información\
    detallada sobre los platos disponibles.")
    st.write("- Ver Distribuciones Estadísticas: Muestra distribuciones\
    estadísticas sobre los platos.")


# Ejemplo de uso:
recetas = {
    "Tacos al Pastor": "México",
    "Pizza Margarita": "Italia",
    "Pad Thai": "Tailandia",

    # Agregar más recetas con sus países de origen
}

# Ejemplo de uso:
platos = ["Tacos al Pastor", "Pizza Margarita", "Pad Thai"]
popularidad = [100, 75, 50]

# Diccionario de recetas con ingredientes por porción
recetas = {
    "Tacos al Pastor": {"Carne de cerdo": 100, "Piña": 50, "Cebolla": 30,
                        "Cilantro": 10, "Tortillas de maíz": 2},
    "Pizza Margarita": {"Masa de pizza": 200, "Tomate": 100, "Mozzarella": 150,
                        "Albahaca": 5},
    "Pad Thai": {"Fideos de arroz": 100, "Tofu": 50, "Huevo": 30, "Brotes de\
                       soja": 20, "Cacahuetes": 10, "Salsa de tamarindo": 50}
}

# Datos de ejemplo de recetas
datos_recetas = {
    "Nombre": ["Tacos al Pastor", "Pizza Margarita", "Pad Thai"],
    "Calorías": [300, 250, 400],
    "Grasas (g)": [15, 10, 20],
    "Proteínas (g)": [20, 15, 25]
}

def calcular_ingredientes(plato, num_personas):
    """Calcula la cantidad de ingredientes requeridos para una receta.

    Args: plato (str): El nombre de la receta.
          num_personas (int): El número de personas que prepararán la receta.

    Returns: dict: Un diccionario con los ingredientes requeridos.
    """
    ingredientes = recetas.get(plato, {})
    cantidad_por_porcion = np.array(list(ingredientes.values()))
    cantidad_total = cantidad_por_porcion * num_personas
    return dict(zip(ingredientes.keys(), cantidad_total))


def elegir_receta():
    """ 
    Muestra una interfaz de usuario para elegir una receta.

    Args: None

    Returns: None
    """

    reemplazar_nulos()

    st.title("Elegir recetas")
    seleccion_tipo = st.selectbox("Selecciona el tipo de receta:",
                                  ['Acompañamiento','Cena', 'Cumpleaños',
                                   'Desayuno', 'Entrante', 'Merienda',
                                   'Plato principal', 'Postre'])
    seleccion_difi = st.selectbox("Selecciona la dificultad de la receta:",
                                  ['muy baja', 'baja', 'media', 'alta',
                                   'muy alta'])

    if st.button("Buscar"):
        recetas = data[(data['Tipo'] == seleccion_tipo) &
                       (data['Dificultad'] == seleccion_difi)]
        if recetas.empty:
            st.write("No se encontraron recetas.")
        else:
            st.write("Recetas encontradas:")
            st.write(recetas[['Nombre', 'Tipo', 'Ingredientes',
                              'Dificultad','Link_receta']])
        