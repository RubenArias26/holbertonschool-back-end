#!/usr/bin/python3

import requests
import sys

def main ():
    #coloco el url del json donde vamos a sacar la informacion
    url = "https://jsonplaceholder.typicode.com/"
    #luego se crea una variable para que contenga el parametro de busqueda que el usuario introducira
    id_employee = int(sys.argv[1])
    #luego iniciamos con la peticion http
    todos = requests.get(url + "/todos").json()
    names = requests.get(url + "/users").json()
    #ahora creamos la variable donde va a contener toda la informacion que obtendra , luego de la iteracion que realizemos
    user_todos = []
    user_names = []
    user_tasks = [] 
    #este bucle es para encontrar y filtrar los titles
    for todo in todos:
        if todo["userId"] == id_employee:
            user_tasks.append(todo)
            if todo["completed"] == True:
                user_todos.append(todo["title"])


    #este es para encontrar el nombre del empleado
    for name in names:
        if name["id"] == id_employee:
            user_names.append(name["name"])
    

    EMPLOYEE_NAME = user_names
    NUMBER_OF_DONE_TASKS = user_todos
    TOTAL_NUMBER_OF_TASKS = user_tasks
    # print("Employee {} is done with tasks ({}/{}):".format(user_names[0], len(user_todos), len(user_tasks)))
    text =  f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"

    print(text)
    for task in user_todos:
        print("\t " + task)



if __name__ == '__main__':
    main()