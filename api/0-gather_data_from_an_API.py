#!/usr/bin/python3
"""Pulls the necessary data... and thank you for reading this"""
from requests import get
from sys import argv


if __name__ == "__main__":
    id, req = int(argv[1]), "https://jsonplaceholder.typicode.com"

    task_data = get(req + '/todos').json()
    completed_tasks = []
    for data in task_data:
        if data['userId'] == id and data['completed'] is True:
                completed_tasks.append(data.get('title'))

    task_data = get(req + '/todos').json()
    total = 0
    for data in task_data:
        if data['userId'] == id:
                total += 1

    task_data = get(req + '/todos').json()
    comp = 0
    for data in task_data:
        if data['userId'] == id and data['completed'] is True:
                comp += 1

    user_data = get(req + '/users').json()
    for data in user_data:
        if data['id'] == id:
            name = data.get('name')

    print("Employee {} is done with tasks({}/{}):".format(name, comp, total))
    for tasks in completed_tasks:
        print('\t {}'.format(tasks))
