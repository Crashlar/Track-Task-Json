#  Task CLI Manager

A lightweight, command-line task manager built with Python. Manage your to-do list directly from the terminal — add, update, delete, and track tasks with ease. Tasks are stored locally in a JSON file, making this tool portable, fast, and dependency-free.

---

## Features

-  Add, update, and delete tasks
-  Mark tasks as `todo`, `in-progress`, or `done`
-  List all tasks or filter by status
-  Persistent storage using a local JSON file
-  No external libraries — pure Python

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Crashlar/Track-Task-Json.git
cd Track-Task-Json
```

## Task Structure

```json
{
  "id": id_name,
  "description": "A short description",
  "status": "todo",
  "createdAt": "current saving/created time ",
  "updatedAt": "update current time"
}
```

> Future Enhancements
 - 🔍 Search tasks by keyword
 - 📅 Sort tasks by creation or update time
 - 📦 Package as a pip-installable CLI tool
 - 🧪 Add unit tests with unittest
 - 🌐 Optional web interface

## File Directory 
```
task-cli/
│
├── main.py                         # Main entry point
├── saved-data.json                 # Auto-created task storage
├── readme.md    
├── gitignore                   
├── image/
    ├── map.jpeg
└── files/
    ├── add.py
    ├── update.py
    ├── delete.py
    ├── listall.py
    ├── notdone.py
    ├── mediator.py           # For mark-in-progress and mark-done
    ├── utils.py              # handle json file
```

##### try roadmap
````
https://roadmap.sh/projects/number-guessing-game
````

<p align="center">
  <strong>Made by 
    <a href="https://www.linkedin.com/in/crashlar/" style="color:red; text-decoration:none;">
      Crashlar
    </a>
  </strong>
</p>
