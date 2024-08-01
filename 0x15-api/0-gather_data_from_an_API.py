#!/usr/bin/python3
"""imports and displays from an api"""
import requests as req
import sys

if __name__ == "__main__":
    id_employee = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"
    url_user = req.get(f"{url}/users/{id_employee}").json()
    url_user_todos = req.get(f"{url}/users/{id_employee}/todos").json()

    name_employee = url_user.get("name")
    total = len(url_user_todos)
    count = 0
    for todos in url_user_todos:
        if todos.get('completed'):
            count += 1

    print(f"Employee {name_employee} is done with tasks({count}/{total}):")
    for todos in url_user_todos:
        if todos.get('completed'):
            print(f"\t {todos['title']}")
