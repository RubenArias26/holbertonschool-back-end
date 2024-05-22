#!/usr/bin/python3
"""Usamos API para extraer información de un archivo JSON y exportarlo a CSV"""
import requests
from sys import argv
import csv

def main():
    if len(argv) != 2 or not argv[1].isdigit():
        print("Argumento no válido, introduzca un solo argumento que sea un número")
        return
    
    id = int(argv[1])

    url_id = f"https://jsonplaceholder.typicode.com/users/{id}"
    url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    try:
        response = requests.get(url_id)
        response.raise_for_status()
        user = response.json()

        EMPLOYEE_NAME = user["name"]

        response = requests.get(url_todos)
        response.raise_for_status()
        todos = response.json()

        # Aquí vamos a crear la lista de registros que queremos escribir en el CSV
        employee_todos = []

        for todo in todos:
            record = [str(id), EMPLOYEE_NAME, str(todo["completed"]), todo["title"]]
            employee_todos.append(record)

        # Escribir los registros en un archivo CSV
        filename = f"{id}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(employee_todos)

        print(f"Datos exportados a {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    main()