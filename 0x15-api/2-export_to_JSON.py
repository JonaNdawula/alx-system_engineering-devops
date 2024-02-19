#!/usr/bin/python3
"""
A python script to get
data from an API and
change it to json
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    user_info_request = requests.get(user_url)
    user_name = user_info_request.json().get('username')

    user_task_url = f'{user_url}/todos'
    user_info_request = requests.get(user_task_url)
    user_tasks = user_info_request.json()

    dictionary_data = {user_id: []}
    for tsk in user_tasks:
        completed_task = tsk.get('completed')
        task_name = tsk.get('title')
        dictionary_data[user_id].append({
                                        "task": task_name,
                                        "completed": completed_task,
                                        "username": user_name})
    with open(f'{user_id}.json', 'w') as fl:
        json.dump(dictionary_data, fl)
