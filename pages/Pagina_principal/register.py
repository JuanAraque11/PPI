import streamlit as st

registered_users = {}

def mostrar_usuarios():
    """
    Mostrar los usuarios registrados

    Args: None

    Returns: None
    """
    st.write(registered_users)


def register_user():
    """
    Registra un nuevo usuario en el sistema.
    
    Args:
        new_username (str): El nombre de usuario del nuevo usuario.
        new_password (str): La contraseña del nuevo usuario.

    Returns:
        None
    """
    st.subheader("Registro de usuario")
    new_username = st.text_input("Nuevo usuario")
    new_password = st.text_input("Nueva contraseña", type="password")
    if st.button("Registrarse"):
        if new_username in registered_users:
            st.error("El usuario ya existe. Por favor, elige otro.")
        else:
            registered_users[new_username] = new_password
            st.success("Usuario registrado exitosamente. Por favor,\
            inicia sesión.")

# Función para mostrar usuarios registrados
def show_registered_users():
    """
    Muestra los usuarios registrados en el sistema.
    
    Args: None

    Returns:
        None
    """	
    st.subheader("Usuarios registrados")
    st.write(list(registered_users.keys()))


def change_password():
    """
    Cambia la contraseña de un usuario existente.
    
    Args: None

    Returns:
        None
    """
    st.subheader("Cambio de contraseña")
    user = st.text_input("Usuario:")
    contraseña_actual = st.text_input("Contraseña actual:", type="password")
    nueva_contraseña = st.text_input("Nueva contraseña:", type="password")

    if st.button("Actualizar"):
        if user in registered_users:
            if registered_users[user] == contraseña_actual:
                registered_users[user] = nueva_contraseña
                st.success("¡Contraseña actualizada con éxito!")
            else:
                st.error("Contraseña incorrecta")
        else:
            st.error("Usuario no registrado")
 
