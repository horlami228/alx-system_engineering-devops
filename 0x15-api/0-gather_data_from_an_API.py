#!/usr/bin/python3

"""
    This script accepts one argument as employye_id
    and returns information about his/her TODO list progress
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com"

        req = requests.get("{}/users/{}".format(url, employee_id))
        json_res = req.json()
        name = json_res.get("name")
        if name is not None:
            req = requests.get("{}/todos/?userId={}".format(url, employee_id))
            todo_list = req.json()
            all_task = len(todo_list)
            completed_task = []
            for task in todo_list:
                if task.get("completed") is True:
                    completed_task.append(task)
            len_com_task = len(completed_task)

            print("Employee {} is done with tasks ({}/{}):".
                  format(name, len_com_task, all_task))
            for task in completed_task:
                print("\t {}".format(task.get("title")))
