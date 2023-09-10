import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Function to add a new task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to mark a task as complete
def mark_as_complete():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.itemconfig(selected_task_index, {'bg': 'green'})
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

# Function to delete a task from the list
def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to edit a task
def edit_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task = task_list.get(selected_task_index)
        updated_task = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=selected_task)
        if updated_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, updated_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Increase font size
font = ("Helvetica", 16)

# Create an entry widget for adding tasks
task_entry = tk.Entry(root, font=font)
task_entry.pack(pady=10)

# Create buttons for adding, marking, deleting, and editing tasks
add_button = tk.Button(root, text="Add Task", command=add_task, font=font)
complete_button = tk.Button(root, text="Mark as Complete", command=mark_as_complete, font=font)
delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=font)
edit_button = tk.Button(root, text="Edit Task", command=edit_task, font=font)

add_button.pack()
complete_button.pack()
delete_button.pack()
edit_button.pack()

# Create a listbox to display tasks
task_list = tk.Listbox(root, selectmode=tk.SINGLE, font=font, selectbackground="yellow")
task_list.pack()

# Run the tkinter main loop
root.mainloop()
