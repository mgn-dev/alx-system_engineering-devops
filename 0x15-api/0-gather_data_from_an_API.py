#!/usr/bin/python3
"""This module implements Python script that returns
information about his/her TODO list progress.
"""
import requests


def get_employee_todo_progress(employee_id):
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

    # Print the progress
    print(f'Employee {employee_name} is done'
          f'with tasks({done_tasks}/{total_tasks}):')
    for task in todos:
        if task['completed']:
            print('\t ' + task['title'])


# Test the function
get_employee_todo_progress(2)
