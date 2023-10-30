#!/usr/bin/python3
"""
    This script export data in JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com"

        req = requests.get("{}/users/{}".format(url, user_id))
        json_res = req.json()
        username = json_res.get("username")

        if username is not None:
            req = requests.get("{}/todos?userId={}".format(url, user_id))
            all_task = req.json()

        data = [{"task": task.get("title"),
                 "completed": task.get("completed"),
                 "username": username} for task in all_task]

        rec = {}
        rec[user_id] = data

        with open("{}.json".format(user_id),
                  mode="w", encoding="UTF-8") as file:
            file.write(json.dumps(rec))
