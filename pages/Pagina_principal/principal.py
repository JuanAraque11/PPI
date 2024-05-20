# Librerías de terceros
import streamlit as st

# Librerías propias
import info
import login
import recetas
import register
import secun
import funciones


# Función principal
def main():
    """
    Función principal del programa.

    Args: None

    Returns: None
    """
    
    
    # Inicializar el estado si no existe
    if 'visible' not in st.session_state:
        st.session_state.visible = False

    if 'aceptado' not in st.session_state:
        st.session_state.aceptado = False

    # Verificar si el usuario acepta los términos y condiciones
    ver_terminos = st.button("Ver términos y condiciones")

    # Actualización de la variable "visible" según el estado del botón
    if ver_terminos:
        st.session_state.visible = not st.session_state.visible

    # Mostrar términos y condiciones solo si la variable "visible" es True
    if st.session_state.visible and not st.session_state.aceptado:
        info.terminos_condiciones()
        aceptado = st.checkbox("Acepto los términos y condiciones")
        
        if aceptado:
            st.session_state.aceptado = True
            st.session_state.visible = False
            st.experimental_rerun()


    if st.session_state.aceptado:

        # Menú desplegable para elegir entre iniciar sesión y registrar usuario
        opcion = st.sidebar.selectbox("Menú:", ["Inicio", "Registrarse", 
                                                "Actualizar contraseña", 
                                                "Buscar recetas", 
                                                "Receta al azar", 
                                                "Buscar por valoración",
                                                "Información y contacto"])


        # estado_politi = info.mostrar_ventana_emergente()

        # if estado_politi:

        if opcion == "Información y contacto":
            info.info1()
            # Sección de codigo ISO
            st.header("Código ISO")
            nombrecomun = st.text_input("Ingrese el nombre del país:")
            codigonombre = None
            if st.button("Ver Código ISO"):
                codigonombre = funciones.extraer_codigo_iso(nombrecomun)
                if codigonombre:
                    st.write(f"El código ISO alfa-2 de {nombrecomun} es: {codigonombre}")
                else:
                    st.write(f"No se encontró el código ISO alfa-2 para {nombrecomun}.")

        elif opcion == "Registrarse":
            register.register_user()
            # if st.button("Ver lista de usuarios"):
                # register.show_registered_users()

        elif opcion == "Inicio":

            info.info2()

            estado = login.login_user()
            if not estado:
                st.info("Por favor, inicie sesión.")
            else:
                secun.main()
                # Redirigir al usuario a un enlace después de iniciar sesión
                # st.markdown("[Ir al enlace](https://unmundoentuplato-funciones.streamlit.app/)")


        elif opcion == "Actualizar contraseña":
            register.change_password()

        elif opcion == "Buscar recetas":
            # Interfaz de usuario
            st.title("Buscar recetas por ingredientes")
            ingrediente_busqueda = st.text_input("Ingrese un ingrediente:")
            buscar_button = st.button("Buscar recetas")
            if buscar_button:
                recetas_encontradas = recetas.buscar_receta_por_ingrediente(ingrediente_busqueda)
                if recetas_encontradas.empty:
                    st.write(f"No se encontraron recetas con el ingrediente: {ingrediente_busqueda}.")
                else:
                    st.write("Recetas encontradas:")
                    st.write(recetas_encontradas[['Nombre', 'Tiempo',
                                                  'Ingredientes', 
                                                  'Link_receta']])

        # else:
            # st.stop()
        elif opcion == "Receta al azar":
            st.title("Receta al azar")
            recetas.mostrar_receta_aleatoria()

        elif opcion == "Buscar por valoración":

            st.title("Buscar por valoración")
            valoracion = st.number_input("Ingrese la valoración a buscar",
                                         min_value=1.0, max_value=5.0,
                                         step=0.1, value=3.0)
            opcion_buscar = st.radio("Selecciona una opción:",
                                     ['mayores', 'menores', 'iguales',
                                      'sin valoración'])

            if st.button("Buscar"):
                recetas_valoradas = recetas.buscar_por_valoracion(valoracion,
                                                                  opcion_buscar)
                if recetas_valoradas.empty:
                    st.write("No se encontraron recetas.")
                else:
                    st.write("Recetas encontradas:")
                    st.write(recetas_valoradas[['Nombre', 'Tiempo',
                                                'Ingredientes', 'Valoracion',
                                                'Link_receta']])
    else:
        # Mostrar mensaje para aceptar los términos y condiciones
        st.warning("Debe aceptar los términos y condiciones para utilizar la\
                    aplicación Un mundo en tu plato.")



if __name__ == "__main__":
    main()
