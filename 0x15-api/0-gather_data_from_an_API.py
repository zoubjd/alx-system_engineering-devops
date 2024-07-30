#!/usr/bin/python3
"""Gather data from api"""


import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Fetch employee's TODO list data
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
