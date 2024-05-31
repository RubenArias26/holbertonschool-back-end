#!/usr/bin/python3
"""Usamos API para extraer información de un archivo JSON"""
import csv
import requests
from sys import argv


def main():
    """Consultamos el nombre y las tareas de un empleado."""
    if len(argv) != 2 or not argv[1].isdigit():
        print("Argumento no válido")
        return

    id = int(argv[1])
    url_id = f"https://jsonplaceholder.typicode.com/users/{id}"
    url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    try:
        response = requests.get(url_id)
        if response.status_code == 200:
            data = response.json()
            EMPLOYEE_NAME = data["username"]

        todos = requests.get(url_todos).json()

        task_status = [todo["completed"] for todo in todos]
        all_tasks = [todo["title"]for todo in todos]
        employee_todos = []

        for index in range(0, len(all_tasks)):
            record = [str(id), EMPLOYEE_NAME, str(task_status[index]), 
                      all_tasks[index]]
            employee_todos.append(record)

        csv_file = f"{id}.csv"

        with open(csv_file, mode='w', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerows(employee_todos)

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")


if __name__ == "__main__":
    main()
