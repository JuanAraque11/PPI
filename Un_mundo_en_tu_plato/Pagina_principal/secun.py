# Librerías de terceros
import streamlit as st
import pandas as pd

# Librerías propias
import funciones
import recetas
import restaurantes
import estadisticas


# Menú de opciones desplegables
opcion = st.sidebar.selectbox("Selecciona una opción:",
                              ["Información",
                               "Consultar Información de los Platos",
                               "Estadísticas de recetas", "Carga tus recetas",
                               "Elegir recetas", "Restaurantes"])

def main():
    """
    Función principal del programa secundario.

    Args: None

    Returns: None
    """
    
    # Mostrar contenido según la opción seleccionada
    if opcion == "Información":
        # Título de la página
        st.title("Contenido")
        funciones.mostrar_inicio()
    elif opcion == "Consultar Información de los Platos":
        # Título de la página
        st.title("Calculadora de Ingredientes")

        # Solicitar información al usuario
        plato = st.selectbox("Selecciona un plato:",
                             list(funciones.recetas.keys()))
        num_personas = st.number_input("Número de personas que van a comer:",
                                       min_value=1, value=1)

        # Calcular ingredientes y mostrar resultado
        if st.button("Calcular"):
            cantidad_ingredientes = funciones.calcular_ingredientes(plato,
                                                                    num_personas)
            st.write("Cantidad de Ingredientes Necesarios:")
            for ingrediente, cantidad in cantidad_ingredientes.items():
                st.write(f"- {ingrediente}: {cantidad} gramos")
    elif opcion == "Estadísticas de recetas":
        st.title("Aqui puedes ver las estadísticas de las recetas existentes\
         en la app.")
        
        estadisticas.distri_categorias()

        estadisticas.distri_valoraciones()

        estadisticas.valoracion_por_dificultad()

        estadisticas.top_recetas_reviews()

        estadisticas.top_recetas_comentadas()
        

    elif opcion == "Carga tus recetas":
        
        # Widget para cargar archivo CSV o Excel
        archivo = st.file_uploader("Cargar archivo con tus recetas:", type=["csv", "xlsx"])

        # Si se carga un archivo, leer los datos y mostrarlos
        if archivo is not None:
            # Leer los datos del archivo
            if archivo.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":  # Excel
                df_datos_adicionales = pd.read_excel(archivo)
            else:  # CSV
                df_datos_adicionales = pd.read_csv(archivo)
            
            # Mostrar los datos cargados
            st.write("Datos cargados:")
            st.write(df_datos_adicionales)

    elif opcion == "Elegir recetas":
        funciones.elegir_receta()

    elif opcion == "Restaurantes":
        st.title("Aqui puede ver la ubicación de los mejores restaurantes\
        en la app.")
        restaurantes.elegir_restaurantes()


if __name__ == "__main__":
    main()