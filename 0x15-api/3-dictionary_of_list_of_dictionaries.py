#!/usr/bin/python3
"""
A Python script to
fetch the rest API
for a todo list of
employees
"""
import json
import requests
import sys


if __name__ == '__main__':
    API = 'https://jsonplaceholder.typicode.com/users'

    response = requests.get(API)
    all_users = response.json()

    dictionary_of_users = {}
    for user in all_users:
        user_id = user.get('id')
        user_name = user.get('username')
        API = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        API = f'{API}/todos/'
        response = requests.get(API)

        user_tasks = response.json()
        dictionary_of_users[user_id] = []
        for tsk in user_tasks:
            completed_task = tsk.get('completed')
            task_name = tsk.get('title')
            dictionary_of_users[user_id].append({
                 "task": task_name,
                 "completed": completed_task,
                 "username": user_name
            })

    with open('todo_all_employees.json', 'w') as fl:
        json.dump(dictionary_of_users, fl)
