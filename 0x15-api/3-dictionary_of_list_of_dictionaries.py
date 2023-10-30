#!/usr/bin/python3
"""
    This script export data in JSON format
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    req = requests.get("{}/users".format(url))
    json_res = req.json()
    list_id = [int(id.get("id")) for id in json_res]
    username_list = [username.get("username") for username in json_res]
    rec = {}
    for id in list_id:
        req = requests.get("{}/todos?userId={}".format(url, id))
        all_task = req.json()

        data = [{"username": username_list[id - 1],
                 "task": task.get("title"),
                 "completed": task.get("completed")} for task in all_task]

        rec[id] = data

    with open("todo_all_employees.json", mode="w", encoding="UTF-8") as file:
        file.write(json.dumps(rec))
