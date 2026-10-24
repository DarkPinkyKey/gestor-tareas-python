import os
import auxiliar


def crearTarea():
    texto_usuario = input("¿Qué tarea quieres añadir?: ")
    with open("tareas.txt", "a") as f:
        f.write("- " + texto_usuario + "\n")
    print("Tarea creada con éxito!")


def leerTarea():
    try:
        with open("tareas.txt", "r") as f:
            print("\n--- TUS TAREAS ---")
            print(f.read())
    except FileNotFoundError:
        print("\nTodavía no hay ninguna tarea guardada")


def borrarTareas():
    pregunta = input("Seguro que quieres borrar todas las tareas? ")
    respuesta = auxiliar.filtroPreguntas(pregunta)
    if respuesta:
        if os.path.exists("tareas.txt"):
            os.remove("tareas.txt")
            print("\nSe han borrado todas las tareas.")
        else:
            print("\n El archivo no existe")
    else:
        print("\nSe ha cancelado la operación")
