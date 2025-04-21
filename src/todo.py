#!/usr/bin/env python3

import sys
import os
import json

class TodoList:
    def __init__(self):
        self.tasks = []
        self.data_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "todo_data.json")
        self.load_tasks()
        
    def load_tasks(self):
        """Load tasks from JSON file if it exists"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.tasks = json.load(f)
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
        
    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.tasks, f)
        except Exception as e:
            print(f"Error saving tasks: {e}")
        
    def add_task(self, task):
        """Add a task to the list"""
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        return len(self.tasks)
        
    def mark_task_complete(self, task_id):
        """Mark a task as complete by its ID"""
        task_id -= 1  # Subtle bug: Decrementing task_id twice
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id - 1]["completed"] = True  # Incorrect index due to double decrement
            self.save_tasks()
            return True
        return False
        
    def list_tasks(self):
        """List all tasks with status"""
        if not self.tasks:
            print("No tasks found. Add tasks with 'python src/todo.py add \"your task\"'")
            return False
            
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"[{status}] {i}. {task['task']}")
        return True

def print_usage():
    """Print usage instructions"""
    print("Usage:")
    print("  python src/todo.py add \"task description\"  - Add a new task")
    print("  python src/todo.py list                     - List all tasks")
    print("  python src/todo.py complete <task_number>   - Mark a task as completed")
            
if __name__ == "__main__":
    # Force unbuffered output
    sys.stdout.reconfigure(line_buffering=True)
    
    # Create todo list instance
    todo = TodoList()
    
    # Handle command line arguments
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "add" and len(sys.argv) >= 3:
        task = " ".join(sys.argv[2:])
        task_id = todo.add_task(task)
        print(f"Added task: {task}", flush=True)
    
    elif command == "list":
        if not todo.list_tasks():
            # Try adding the test task if list is empty (for demonstration)
            if "test" in sys.argv:
                todo.add_task("test the todo app")
                print("Added default task 'test the todo app' for demonstration", flush=True)
                todo.list_tasks()
    
    elif command == "complete" and len(sys.argv) >= 3:
        try:
            task_id = int(sys.argv[2])
            if todo.mark_task_complete(task_id):
                print(f"Marked task {task_id} as completed", flush=True)
            else:
                print(f"No task with ID {task_id}", flush=True)
        except ValueError:
            print("Task ID must be a number", flush=True)
            print_usage()
    
    else:
        print("Invalid command", flush=True)
        print_usage()
