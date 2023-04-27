#!/usr/bin/python3
"""Pulls the necessary data... and thank you for reading this"""
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    id, req = int(argv[1]), "https://jsonplaceholder.typicode.com"

    # GETS THE TITLE OF COMPLETES TASKS
    task_data = get(req + '/todos/?userId={}'.format(id)).json()

    # GETS THE NAME OF THE USER
    user_data = get(req + '/users').json()
    for data in user_data:
        if data['id'] == id:
            name = data.get('username')

    filename = '{}.csv'.format(id)
    with open(filename, mode='w') as file:
        w = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in task_data:
            w.writerow([id, name, task.get('completed'), task.get('title')])
