import tkinter as tk
from tkinter import simpledialog

task_list = []

def add_task():
    task_name = simpledialog.askstring("Add Task", "Enter Task:")
    if task_name:
        task_list.append(task_name)
        update_task_list()

def view_tasks():
    if not task_list:
        tk.messagebox.showinfo("Task List", "You have no tasks in the list.")
    else:
        task_str = "\n".join([f"{number}. {task}" for number, task in enumerate(task_list, start=1)])
        tk.messagebox.showinfo("Task List", f"Tasks in your to-do list:\n{task_str}")

def edit_task():
    if not task_list:
        tk.messagebox.showinfo("Edit Task", "You don't have any tasks to edit.")
        return

    view_tasks()
    try:
        task_index = simpledialog.askinteger("Edit Task", "Enter the task number to edit:") - 1
        if 0 <= task_index < len(task_list):
            new_task = simpledialog.askstring("Edit Task", "Enter the new task:")
            if new_task:
                task_list[task_index] = new_task
                tk.messagebox.showinfo("Edit Task", "Task edited successfully!")
                update_task_list()
            else:
                tk.messagebox.showwarning("Edit Task", "Invalid task name. Task not edited.")
        else:
            tk.messagebox.showwarning("Edit Task", "Invalid task number.")
    except ValueError:
        tk.messagebox.showwarning("Edit Task", "Invalid input. Please enter a valid number.")

def delete_task():
    if not task_list:
        tk.messagebox.showinfo("Delete Task", "You don't have any tasks to delete.")
        return

    view_tasks()
    task_to_delete = simpledialog.askstring("Delete Task", "Enter the task to delete:")
    if task_to_delete in task_list:
        task_list.remove(task_to_delete)
        tk.messagebox.showinfo("Delete Task", "Task deleted successfully!")
        update_task_list()
    else:
        tk.messagebox.showwarning("Delete Task", "Task not found in the list.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in task_list:
        task_listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
root.title("To-Do List Manager")

# Create and place widgets
task_listbox = tk.Listbox(root)
task_listbox.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

view_button = tk.Button(root, text="View Tasks", command=view_tasks)
view_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=5)

# Run the main loop
root.mainloop()
