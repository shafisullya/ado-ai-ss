# Python Todo Application

A simple command-line todo list application written in Python.

## Features

- Add tasks to your todo list
- Mark tasks as completed
- List all tasks with their completion status

## Project Structure

- `src/` - Source code directory
  - `todo.py` - The main todo list application
- `requirements.txt` - Python dependencies

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   ./src/todo.py
   ```

## Development

This project uses:
- pytest for testing
- pylint for linting
- black for code formatting

## Usage

### Add a Task
To add a task to your todo list:
```
python src/todo.py add "task description"
```

### List Tasks
To list all tasks with their completion status:
```
python src/todo.py list
```

### Mark a Task as Completed
To mark a task as completed by its ID:
```
python src/todo.py complete <task_number>
```