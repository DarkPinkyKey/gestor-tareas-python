import tareas


def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Borrar tarea")
    print("4. Salir")


def iniciar_programa():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            tareas.leerTarea()
        elif opcion == "2":
            tareas.crearTarea()
        elif opcion == "3":
            tareas.borrarTareas()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n Opción no válida. Por favor, elige entre 1 y 4.")


if __name__ == "__main__":
    iniciar_programa()
