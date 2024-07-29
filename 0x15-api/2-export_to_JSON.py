#!/usr/bin/python3
"""This module implements Python script that returns
todo list info and exports to CSV.
"""
import json
import requests
import sys


def export_employee_todo_to_csv(employee_id):
    """Function that export api data in the CSV format.
    """
    # Get the user details
    user = requests.\
        get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    # Get the todos for the user
    todos = requests.\
        get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')\
        .json()

    csv_file_name = f"{user['id']}.json"

    # Prepare the data in the specified JSON format
    data = {
        str(user['id']): [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username']
            }
            for task in todos
        ]
    }

    # Write the data to a JSON file
    with open(csv_file_name, 'w') as file:
        json.dump(data, file, indent=4)


# Run the function
if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    export_employee_todo_to_csv(emp_id)
