# See-Image
**Visor de imágenes inteligente**  

## Descripción
See-Image es una aplicación de escritorio desarrollada en Python que permite visualizar, explorar y buscar imágenes almacenadas localmente. Utiliza técnicas de visión por computador e inteligencia artificial para ofrecer una experiencia de usuario sencilla y potente.

## Funcionalidades
- Carga y visualización de imágenes en formatos comunes (JPEG, PNG).
- Navegación rápida entre directorios de imágenes.
- Interfaz gráfica intuitiva.

## Tecnologías utilizadas
- Python 3.x
- Pillow: carga y gestión de formatos de imagen.
- Tkinter: construcción de la interfaz gráfica.
- Customtkinter: construcción de la interfaz gráfica.
- waifu2x-ncnn-py: procesamiento de imágenes.
- rembg: procesamiento de imágenes.

## Requisitos
- Python 3.8 o superior
- Paquetes listados en `requeriment.txt`
- Vulkan SDK:
  - Windows: instalar desde https://vulkan.lunarg.com/sdk/home
  - Linux: `sudo apt install -y libomp5 libvulkan-dev`

## Instalación
```bash
pip install -r requeriment.txt
```

## Uso
```bash
python interface.py
```

## Contribución
Las contribuciones son bienvenidas. Por favor, abre un _issue_ o envía un _pull request_.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
