# Gestor de Tareas en Python

Una sencilla aplicación de consola desarrollada en Python para gestionar tareas diarias de forma interactiva y organizada mediante archivos de texto.

## Características

- **Menú interactivo:** Añade, visualiza y borra tareas de manera intuitiva.
- **Persistencia de datos:** Las tareas se guardan automáticamente en un archivo local (`tareas.txt`).
- **Validación flexible:** Archivo auxiliar para procesar respuestas del usuario sin importar mayúsculas o minúsculas ("si", "yes", "afirmativo").

## Estructura del Proyecto

- `main.py`: Punto de entrada del programa y gestión del bucle principal del menú.
- `tareas.py`: Contiene la lógica de creación, lectura y borrado de tareas.
- `auxiliar.py`: Funciones de apoyo para procesar entradas del usuario.

## Cómo ejecutar el proyecto

1. Tener Python instalado en tu ordenador.
2. Clona este repositorio o descarga los archivos.
3. Abre tu terminal en la carpeta del proyecto y ejecuta:
   ```bash
   python main.py
   ```
