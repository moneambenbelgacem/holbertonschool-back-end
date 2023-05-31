#!/usr/bin/python3
"""Create an API to get todo list for employe"""





import requests
import sys

def get_employee_tasks(employeeId):
    employee = requests.get(f'https://new_url_for_employee_info/{employeeId}').json()
    todos = requests.get(f'https://new_url_for_todos?userId={employeeId}').json()

    done_tasks = [task for task in todos if task.get('completed') == True]
    total_tasks = len(todos)

    print(f"Employee {employee.get('name')} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print("\t " + task.get('title'))

if __name__ == "__main__":
    get_employee_tasks(int(sys.argv[1]))
