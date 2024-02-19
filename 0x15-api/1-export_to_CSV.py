#!/usr/bin/python3
"""
A python script to
Export to csv
"""
import json
import csv
import requests
import sys

if __name__ == '__main__':
    individual = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + individual
    user_info_request = requests.get(user_url)
    user_name = user_info_request.json().get('username')
    user_task = f"{user_url}/todos"
    user_info_request = requests.get(user_task)
    user_tasks = user_info_request.json()

    with open(f'{individual}.csv', 'w') as csvfile:
        for tsk in user_tasks:
            task_done = tsk.get('completed')
            task_name = tsk.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                undividual, user_name, task_done, task_name))
