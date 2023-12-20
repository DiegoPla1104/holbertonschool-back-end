#!/usr/bin/python3
"""Prints the completed tasks of an employee"""
import requests
from sys import argv

if __name__ == '__main__':

    users = requests.get(f"https://jsonplaceholder.typicode.com/\
users?id={argv[1]}")
    todos = requests.get(f"https://jsonplaceholder.typicode.com/\
todos?userId={argv[1]}")

    users = users.json()
    todos = todos.json()

    with open(f"{users[0]['id']}.csv", "w", encoding="utf-8") as file:
        for todo in todos:
            Uid = users[0]['id']
            name = users[0]['username']
            state = todo['completed']
            tname = todo['title']
            string = (f"\"{Uid}\",\"{name}\",\"{state}\",\"{tname}\"\n")
            file.write(string)
