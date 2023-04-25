#!/usr/bin/python3
"""Create an API to get todo list for employe"""



import requests
from sys import argv

url_base = "https://jsonplaceholder.typicode.com/users/"


if __name__ == "__main__":
    employee = requests.get(url_base + argv[1]).json()
    todo_list = requests.get(url_base + argv[1] + "/todos/").json()
    completed_tasks = 0
    text = ""

    for task in todo_list:
        if task['completed'] is True:
            text += f"\t {task['title']}\n"
            completed_tasks += 1

    print(
        f"Employee {employee['name']} is done with tasks({completed_tasks}/20):\n{text}",
        end="",
    )