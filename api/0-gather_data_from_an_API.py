#!/usr/bin/python3
"""Usamos API para extraer información de un archivo JSON"""
import requests
from sys import argv


def main():
    """Consultamos el nombre y las tareas de un empleado."""
    if len(argv) != 2 or not argv[1].isdigit():
        print("Argumento no válido, introduzca un solo argumento que sea un número")
        return

    id = int(argv[1])
    url_id = f"https://jsonplaceholder.typicode.com/users/{id}"
    url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    try:
        response = requests.get(url_id).json()
        if response["id"] == id:
            EMPLOYEE_NAME = response["name"]

        todos = requests.get(url_todos).json()
        NUMBER_OF_DONE_TASKS = []
        TOTAL_NUMBER_OF_TASKS = []

        for todo in todos:
            TOTAL_NUMBER_OF_TASKS.append(todo)
            if todo["completed"]:
                NUMBER_OF_DONE_TASKS.append(todo["title"])

        text = (f"Employee {EMPLOYEE_NAME} is done with "
                f"tasks({len(NUMBER_OF_DONE_TASKS)}/{len(TOTAL_NUMBER_OF_TASKS)}):")
        print(text)

        for task in NUMBER_OF_DONE_TASKS:
            print("\t" + task)

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")


if __name__ == "__main__":
    main()
