#!/usr/bin/python3
"""
A python script
that uses REST API
for a given employee ID, returns
information about his/her
TODO list progress.
"""

import requests
import sys
import re
import json

API = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    arg_len = len(sys.argv)
    if arg_len > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            emp_id = int(sys.argv[1])
            info_request = requests.get(f'{API}/users/{emp_id}').json()
            task_data = requests.get(f'{API}/todos').json()
            emp_name = info_request.get('name')
            emp_tasks = list(filter(lambda i: i.get('userId')
                                    == emp_id, task_data))
            complete_tasks = list(filter(lambda i:
                                  i.get('completed'), emp_tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(complete_tasks),
                    len(emp_tasks)
                 )
            )
            if len(complete_tasks) > 0:
                for tsk in complete_tasks:
                    print('\t {}'.format(tsk.get('title')))
