#!/usr/bin/python3
"""
    This script export data in CSV format
"""
import csv
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

            with open("{}.csv".format(user_id), mode="w") as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                for task in all_task:
                    row = [int(user_id), username,
                           task.get("completed"), task.get("title")]
                    writer.writerow(row)
