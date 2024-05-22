#!/usr/bin/python3
"""Usamos api para extraer informacion de un archivo json"""
import requests
from sys import argv

def main():
    #luego se crea una variable para que contenga el parametro de busqueda que el usuario introducira
    if len(argv) != 2 or not argv[1].isdigit():
        print("argumento no valido, introduzca un solo argumento que sea un numero")
        return
    
    id = int(argv[1])

    url_id = f"https://jsonplaceholder.typicode.com/users/{id}"
    url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    # bloque de try-except con el que vamos a trabajar
    try:
        # buscamos obtener el id que se da como argumento y guardarlo en una variable con el nombre relacionado a su id
        response = requests.get(url_id).json()

        if response["id"] == id:
            data = response["name"]
            EMPLOYEE_NAME = data

        todos = requests.get(url_todos).json()
        NUMBER_OF_DONE_TASKS = []
        TOTAL_NUMBER_OF_TASKS = []

        # iteramos para poder añadir todas las tasks que tiene tal id, y para obtener tambien las que ha concluido
        for todo in todos:
            if todo["userId"] == id:
                TOTAL_NUMBER_OF_TASKS.append(todo)
                if todo["completed"] == True:
                    NUMBER_OF_DONE_TASKS.append(todo["title"])
        
        text = f"employee {EMPLOYEE_NAME} is done with tasks({len(NUMBER_OF_DONE_TASKS)}/{len(TOTAL_NUMBER_OF_TASKS)}):"

        print(text)

        for task in NUMBER_OF_DONE_TASKS:
            print("\t" + task)

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
if __name__ == "__main__":
    main()