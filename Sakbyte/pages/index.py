# Importamos las librerías y módulos necesarios
import reflex as rx
from Sakbyte.components.navbar import navbar  # Componente de la barra de navegación
from Sakbyte.views.header import header  # Vista del encabezado
from Sakbyte.components.footer import footer  # Componente del pie de página
from Sakbyte.views.index_links import index_links  # Vista de los enlaces principales
from Sakbyte.components.background_animation import animation_bg  # Animación de fondo
from Sakbyte import utils  # Utilidades generales del proyecto
from Sakbyte.routes import Route  # Definición de rutas
import Sakbyte.styles.styles_index as style  # Estilos específicos para la página de inicio

# Decorador que define la configuración de la página principal
@rx.page(
    route=Route.INDEX.value,  # Ruta asociada a la página de inicio
    title=utils.index_title,  # Título de la página
    description=utils.index_description,  # Descripción de la página
    meta=utils.index_meta,  # Metadatos adicionales
    image=utils.index_image,
)
def index() -> rx.Component:
    """
    Función que define la estructura y los componentes de la página de inicio.
    Retorna un componente de Reflex que representa la página.
    """
    return rx.box(  # Contenedor principal de la página
        navbar(),  # Barra de navegación en la parte superior
        animation_bg(),  # Animación de fondo

        # Contenedor central con el contenido principal
        rx.center(
            rx.vstack(  # Apilamos los componentes verticalmente
                header(),  # Encabezado principal
                index_links(),  # Enlaces principales de la página
                max_width=style.MAX_WIDTH,  # Ancho máximo del contenedor
                margin_y=style.Size.MEDIUM.value,  # Margen vertical
                margin_x=style.Size.MEDIUM.value,  # Margen horizontal
            ),
        ),
        footer(),  # Pie de página
    )