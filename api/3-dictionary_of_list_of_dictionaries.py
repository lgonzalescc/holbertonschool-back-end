#!/usr/bin/python3
"""Pulls the necessary data... and thank you for reading this"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    req = "https://jsonplaceholder.typicode.com"

    task_data = get(req + '/todos').json()
    user_data = get(req + '/users').json()

    def fetch_name(id):
        """Fetches the name for each ID"""
        for data in user_data:
            if data['id'] == id:
                return data.get('username')

    # Gets all the applicable IDs
    id_list = []
    for ids in user_data:
        id_list.append(ids['id'])

    # Generate the data for each dictionary, then append
    final_data = {}
    for all_ids in id_list:
        the_dayta = [{'username': fetch_name(all_ids),
                      'task': task.get('title'),
                      'completed': task.get('completed')}
                     for task in task_data]
        final_data.update({all_ids: the_dayta})

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as the_file:
        json.dump(final_data, the_file)
