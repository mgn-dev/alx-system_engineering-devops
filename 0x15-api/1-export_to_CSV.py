#!/usr/bin/python3
"""This module implements Python script that returns
todo list info and exports to CSV.
"""
import csv
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

    user_id = user['id']
    csv_file_name = f"{user_id}.csv"

    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([f"{user['id']}",
                             f"{user['username']}",
                             f"{task['completed']}",
                             f"{task['title']}"])


# Run the function
if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    export_employee_todo_to_csv(emp_id)
