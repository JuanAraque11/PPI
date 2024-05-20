class Usuario:
    """Representa un usuario de la aplicación.

    Esta clase almacena información sobre un usuario, incluyendo su nombre\
        de usuario y contraseña.

    Args:
        username (str): El nombre de usuario del usuario.
        contraseña (str): La contraseña del usuario.

    Attributes:
        _username (str): El nombre de usuario del usuario.
        _contraseña (str): La contraseña del usuario.

    """

    def __init__(self, username, contraseña):
        """Inicializa una nueva instancia de la clase Usuario.

        Args:
            username (str): El nombre de usuario del usuario.
            contraseña (str): La contraseña del usuario.

        """
        self._username = username
        self._contraseña = contraseña

    def get_username(self):
        return self._username

    def set_username(self, nuevo_username):
        self._username = nuevo_username

    def get_contraseña(self):
        return self._contraseña


    def set_contraseña(self, nueva_contraseña):
        self._contraseña = nueva_contraseña
