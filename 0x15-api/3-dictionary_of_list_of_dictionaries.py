#!/usr/bin/python3
"""This module implements Python script that returns
todo list info and exports to CSV.
"""
import json
import requests


def export_all_employee_todo_to_csv():
    """Function that export api data in the CSV format.
    """
    # Get all users
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    # Initialize the data dictionary
    data = {}

    # Iterate over each user to get their tasks
    for user in users:
        user_id = user['id']
        username = user['username']

        # Get the todos for the user
        todos = requests.\
            get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')\
            .json()

        # Format the tasks for this user
        data[str(user_id)] = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todos
        ]

    # Define the output file name
    file_name = 'todo_all_employees.json'

    # Write the data to a JSON file
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


# Run the function
if __name__ == "__main__":
    export_all_employee_todo_to_csv()
