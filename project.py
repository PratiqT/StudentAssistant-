import json
import os

tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

def clear(n):
    global tasks
    try:
        tasks.pop(n)
        save_tasks()
        return f"Task {n+1} cleared"
    except IndexError:
        return "No such Task"

def clear_all():
    global tasks
    tasks.clear()
    save_tasks()
    return "Every Task cleared!"



def show():
    for number, task in enumerate(tasks, 1):
        print(f"{number}. {task}")


def add():

    t = input("> ")
    t = t.lower()

#for add
    if t.startswith("add"):
        a, b = t.split("add", 1)
        if b.strip() == "":
            return "please enter some task"
        tasks.append(b)
        save_tasks()
        return f"Added: {b.strip()}"
    elif t.startswith("a_"):
        x, y = t.split("a_", 1)
        if y.strip() == "":
            return "please enter some task"
        tasks.append(y)
        save_tasks()
        return f"Added: {y.strip()}"

#for show
    elif t.startswith("show"):
        show()
        return ""

#for clear
    elif t.startswith("clear_"):
        p, q = t.split("clear_", 1)
        q = q.lower()
        if q.startswith("all"):
            return clear_all()
        elif not q.startswith("all"):
            try:
                q = int(q)
                q -= 1
                return clear(q)
            except ValueError:
                print("Clear What?")
                return ""
        else:
            print("check your commands again")

    else:
        return "Invalid Input"



def main():
    try:
        while True:
            print(add())
    except KeyboardInterrupt:
        print("\nHave a nice day!")



if __name__ == "__main__":
    load_tasks()
    main()