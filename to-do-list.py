import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task_index = tasks_list.curselection()
    if selected_task_index:
        tasks_list.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def clear_tasks():
    tasks_list.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack()

tasks_list = tk.Listbox(root, width=40)
tasks_list.pack(pady=10)

root.mainloop()
