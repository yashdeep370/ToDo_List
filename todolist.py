import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []
dark_mode = False  # flag to track current mode

def add_task():
    task_text = task_entry.get().strip()
    deadline_text = deadline_entry.get().strip()

    if not task_text:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return

    if deadline_text:
        try:
            datetime.strptime(deadline_text, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Date Error", "Use deadline format: YYYY-MM-DD")
            return
    else:
        deadline_text = "No deadline"

    tasks.append({'text': task_text, 'deadline': deadline_text, 'done': tk.BooleanVar()})
    task_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)
    update_task_list()

def update_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for task in tasks:
        cb = tk.Checkbutton(
            task_frame,
            text=f"{task['text']} (Due: {task['deadline']})",
            variable=task['done'],
            font=("Arial", 12),
            bg=theme['bg'],
            fg=theme['fg'],
            selectcolor=theme['bg'],
            activebackground=theme['bg'],
            activeforeground=theme['fg'],
            anchor="w"
        )
        cb.pack(fill='x', pady=2)

def delete_done_tasks():
    global tasks
    tasks = [task for task in tasks if not task['done'].get()]
    update_task_list()

def toggle_dark_mode():
    global dark_mode, theme
    dark_mode = not dark_mode
    theme = dark if dark_mode else light

    # Apply theme to all elements
    root.configure(bg=theme['bg'])
    title_label.configure(bg=theme['bg'], fg=theme['fg'])
    task_entry.configure(bg=theme['entry_bg'], fg=theme['fg'], insertbackground=theme['fg'])
    deadline_entry.configure(bg=theme['entry_bg'], fg=theme['fg'], insertbackground=theme['fg'])
    task_frame.configure(bg=theme['bg'])
    add_button.configure(bg=theme['button_bg'], fg=theme['button_fg'], activebackground=theme['button_active'])
    delete_button.configure(bg=theme['button_bg'], fg=theme['button_fg'], activebackground=theme['button_active'])
    toggle_button.configure(bg=theme['button_bg'], fg=theme['button_fg'], activebackground=theme['button_active'])

    update_task_list()

# --- Themes ---
light = {
    'bg': '#e6f2ff',
    'fg': '#000000',
    'entry_bg': '#ffffff',
    'button_bg': '#4CAF50',
    'button_fg': '#ffffff',
    'button_active': '#388e3c'
}

dark = {
    'bg': '#121212',
    'fg': '#f5f5f5',
    'entry_bg': '#1e1e1e',
    'button_bg': '#333333',
    'button_fg': '#ffffff',
    'button_active': '#555555'
}

theme = light  # default to light

# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List (Dark Mode Enabled)")
root.geometry("400x500")
root.configure(bg=theme['bg'])

# Title
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg=theme['bg'], fg=theme['fg'])
title_label.pack(pady=10)

# Task Entry
task_entry = tk.Entry(root, font=("Arial", 14), width=30, bg=theme['entry_bg'], fg=theme['fg'], insertbackground=theme['fg'])
task_entry.pack(pady=5)

# Deadline Entry
deadline_entry = tk.Entry(root, font=("Arial", 12), width=30, bg=theme['entry_bg'], fg=theme['fg'], insertbackground=theme['fg'])
deadline_entry.insert(0, "YYYY-MM-DD")
deadline_entry.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg=theme['bg'])
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=15, bg=theme['button_bg'], fg=theme['button_fg'], activebackground=theme['button_active'])
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Done", command=delete_done_tasks, width=15, bg=theme['button_bg'], fg=theme['button_fg'], activebackground=theme['button_active'])
delete_button.grid(row=0, column=1, padx=5)

# Toggle Dark Mode
toggle_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode, width=30, bg=theme['button_bg'], fg=theme['button_fg'], activebackground=theme['button_active'])
toggle_button.pack(pady=5)

# Task Frame
task_frame = tk.Frame(root, bg=theme['bg'], bd=2, relief=tk.SUNKEN)
task_frame.pack(fill='both', expand=True, padx=10, pady=10)

root.mainloop()
