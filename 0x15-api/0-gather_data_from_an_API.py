#!/usr/bin/python3
"""This module implements Python script that returns
information about todo list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Function that returns
       information about todo list progress.
    """
    # Get the user details
    user = requests.\
        get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    # Get the todos for the user
    todos = requests.\
        get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')\
        .json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = len([task for task in todos if task['completed']])
    employee_name = user['name']

    # Print the progress and todos
    print(f'Employee {employee_name} is done'
          f' with tasks({done_tasks}/{total_tasks}):')
    for task in todos:
        if task['completed']:
            print('\t ' + task['title'])


# Run the function
if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    get_employee_todo_progress(emp_id)
