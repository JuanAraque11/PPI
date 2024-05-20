import streamlit as st

def info1():
    """
    muestra informacion importante

    Args: None

    Returns: None
    """
    st.title("Información importante")

    st.write("Bienvenido a mi página web, Aquí encontrarás información\
    relevante sobre mi servicio.")

    st.write('''
            Soy Juan Araque, estudiante de Ingeniería de Sistemas en la\
            Universidad Nacional de Colombia sede Medellín Facultad de\
            Minas, actualmente cursando septimo semestre. Poseo\
            conocimientos en una variedad de lenguajes de programación,\
            incluyendo Python, Java, SQL, C, entre otros. Mi pasión por la\
            tecnología y el desarrollo de software me impulsa a buscar\
            oportunidades para aplicar y mejorar mis habilidades en\
            proyectos desafiantes.
            ''')
    st.write("Puedes contactar conmigo por medio de: ")
    st.markdown("- [LinkedIn](https://www.linkedin.com/in/juan-jose-echavarria-araque-a92286296)")
    st.markdown("- [Reddit](https://www.reddit.com/user/JuanAraque/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)")
    st.write()
    st.write("O puedes contratar mis servicios por medio de: ")
    st.markdown("- [Upwork](https://www.upwork.com/workwith/juanjosee)")
    st.markdown("- [Freelancer](https://www.freelancer.com/u/JuanJEchav?sb=t)")
    st.markdown("- [Fiverr](https://www.fiverr.com/juanjechav?public_mode=true)")

    
def info2():
    """
    muestra informacion importante sobre la app

    Args: None
    
    Returns: None
    """
    
    # Título y autor
    st.title("Un mundo en tu plato")
    st.write('''
    ¡Emprende un viaje culinario alrededor del mundo sin salir de\
    casa!
    Descubre recetas auténticas de cada rincón del planeta, desde la vibrante\
    cocina mexicana hasta los exóticos sabores tailandeses.

    Explora una amplia variedad de platos, desde clásicos familiares hasta\
    innovadoras creaciones de chefs galardonados.

    Aprende a preparar platos deliciosos con instrucciones detalladas paso a\
    paso y videos explicativos.

    Conoce los ingredientes de cada receta, su origen y sus propiedades\
    nutricionales.

    Personaliza tu experiencia con filtros avanzados que te permiten buscar\
    recetas por región, tipo de cocina, ingredientes y preferencias dietéticas.

    Guarda tus recetas favoritas para acceder a ellas fácilmente más tarde.

    Comparte tus descubrimientos culinarios con amigos y familiares en las\
    redes sociales.

    ''')


def terminos_condiciones():
    """ 
    Botón para abrir la ventana emergente para política
    
    Args: None

    Returns: None
    """
    st.title("Términos y condiciones")

    st.write('''
    Política de tratamiento de datos personales para los usuarios de Un\
    mundo en tu plato.

    Un mundo en tu plato es una aplicación web que permite a los usuarios\
    explorar y descubrir recetas auténticas de diferentes partes del mundo.\
    La Aplicación está comprometida con la protección de la privacidad de\
    sus usuarios y el tratamiento responsable de sus datos personales.

    Esta Política de tratamiento de datos personales describe cómo la\
    Aplicación recopila, utiliza, divulga y protege los datos personales\
    de sus usuarios. Esta Política se aplica a toda la información que la\
    Aplicación recopila a través de la Aplicación, el sitio web de la\
    Aplicación y cualquier otro servicio relacionado con la Aplicación.

    1. Recopilación de datos personales

    La Aplicación recopila los siguientes datos personales de sus usuarios:

    Información de registro: Cuando un usuario crea una cuenta en la\
    Aplicación, se le solicita que proporcione cierta información, como su\
    usuario y contraseña.
    Datos de actividad: La Aplicación recopila datos sobre la actividad del\
    usuario en la Aplicación, como las recetas que el usuario ha guardado.
                
    2. Uso de datos personales

    La Aplicación utiliza los datos personales de sus usuarios para los\
    siguientes fines:

    Proporcionar y mejorar la Aplicación: La Aplicación utiliza los datos\
    personales de sus usuarios para proporcionarles la Aplicación y mejorar\
    su experiencia.
    Personalizar la experiencia del usuario: La Aplicación utiliza los\
    datos personales de sus usuarios para personalizar su experiencia.
    Investigación y desarrollo: La Aplicación puede utilizar los datos\
    personales de sus usuarios para investigación y desarrollo.
    
    3. Divulgación de datos personales

    La Aplicación no divulgará los datos personales de sus usuarios a\
    terceros sin el consentimiento previo del usuario. Sin embargo, la\
    Aplicación puede divulgar los datos personales de sus usuarios a\
    terceros proveedores de servicios que ayudan a la Aplicación a operar,\
    como proveedores de alojamiento web y proveedores de análisis.

    4. Seguridad de los datos personales

    La Aplicación toma medidas razonables para proteger los datos\
    personales de sus usuarios contra la pérdida, el robo, el uso no\
    autorizado, la divulgación y la alteración. Estas medidas incluyen\
    medidas de seguridad físicas, técnicas y administrativas.

    5. Derechos de los usuarios

    Los usuarios tienen los siguientes derechos con respecto a sus datos\
    personales:

    Derecho de acceso: Los usuarios tienen derecho a acceder a sus datos\
    personales y a obtener información sobre cómo se están utilizando sus\
    datos.
    Derecho de cambio: Los usuarios tienen derecho a solicitar la cambio de\
    sus datos personales si son incorrectos o están incompletos o por deseo\
    personal.
    Derecho de supresión: Los usuarios tienen derecho a solicitar la\
    supresión de sus datos personales en determinados casos.
    Derecho de limitación del tratamiento: Los usuarios tienen derecho a\
    solicitar la limitación del tratamiento de sus datos personales en\
    determinados casos.
    ''')

    # Pie de página
    st.write("© 2024. Todos los derechos reservados.")
