import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess

def refresh_listbox(path, listbox):
    listbox.delete(0, tk.END)
    for item in os.listdir(path):
        listbox.insert(tk.END, item)
    for i in range(listbox.size()):
        item = listbox.get(i)
        if os.path.isdir(os.path.join(path, item)):
            listbox.itemconfig(i, {'bg': 'orange'})

def create_folder():
    folder_name = simpledialog.askstring("Input", "Enter folder name:")
    if folder_name:
        try:
            os.mkdir(os.path.join(current_path, folder_name))
            refresh_listbox(current_path, listbox)
        except OSError:
            messagebox.showerror("Error", "Creation of the directory failed")

def create_file():
    file_name = simpledialog.askstring("Input", "Enter file name:")
    if file_name:
        try:
            with open(os.path.join(current_path, file_name), 'w') as f:
                pass
            refresh_listbox(current_path, listbox)
        except OSError:
            messagebox.showerror("Error", "Creation of the file failed")

def view_or_open(event):
    selected_item = listbox.curselection()
    if selected_item:
        item = listbox.get(selected_item)
        if os.path.isdir(os.path.join(current_path, item)):
            open_folder()
        else:
            view_file()

def view_file():
    selected_item = listbox.curselection()
    if selected_item:
        item = listbox.get(selected_item)
        file_path = os.path.join(current_path, item)
        if os.path.isfile(file_path):
            try:
                subprocess.Popen(['xdg-open', file_path])
            except:
                messagebox.showerror("Error", "Failed to open file")

def rename_file():
    selected_item = listbox.curselection()
    if selected_item:
        item = listbox.get(selected_item)
        new_name = simpledialog.askstring("Rename", f"Enter new name for {item}:")
        if new_name:
            try:
                os.rename(os.path.join(current_path, item), os.path.join(current_path, new_name))
                refresh_listbox(current_path, listbox)
            except OSError:
                messagebox.showerror("Error", "Rename failed")

def delete_item():
    selected_item = listbox.curselection()
    if selected_item:
        item = listbox.get(selected_item)
        confirm = messagebox.askyesno("Delete", f"Are you sure you want to delete {item}?")
        if confirm:
            try:
                path = os.path.join(current_path, item)
                if os.path.isdir(path):
                    os.rmdir(path)
                else:
                    os.remove(path)
                refresh_listbox(current_path, listbox)
            except OSError:
                messagebox.showerror("Error", "Deletion failed")

def go_back():
    global current_path
    current_path = os.path.dirname(current_path)
    refresh_listbox(current_path, listbox)
    update_tree()

def open_folder():
    global current_path
    selected_item = listbox.curselection()
    if selected_item:
        item = listbox.get(selected_item)
        if os.path.isdir(os.path.join(current_path, item)):
            current_path = os.path.join(current_path, item)
            refresh_listbox(current_path, listbox)
            update_tree()

def update_tree():
    tree_path = current_path.replace(os.path.expanduser('~'), 'Home')
    tree_label.config(text=tree_path)

root = tk.Tk()
root.title("File Manager")

root.resizable(False, False)

home_path = os.path.expanduser('~')
current_path = home_path

tree_label = tk.Label(root, font=('Arial', 10, 'bold'), pady=5)
tree_label.pack(side=tk.TOP, fill=tk.X)

back_button = tk.Button(root, text="Back", command=go_back)
back_button.pack(side=tk.TOP, padx=5, pady=5)

listbox = tk.Listbox(root, width=100, height=30)
listbox.pack()

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=5)

create_folder_button = tk.Button(button_frame, text="Create Folder", command=create_folder)
create_folder_button.pack(side=tk.LEFT, padx=5)

create_file_button = tk.Button(button_frame, text="Create File", command=create_file)
create_file_button.pack(side=tk.LEFT, padx=5)

open_folder_button = tk.Button(button_frame, text="Open Folder", command=open_folder)
open_folder_button.pack(side=tk.LEFT, padx=5)

rename_button = tk.Button(button_frame, text="Rename", command=rename_file)
rename_button.pack(side=tk.RIGHT, padx=5)

delete_button = tk.Button(button_frame, text="Delete", command=delete_item)
delete_button.pack(side=tk.RIGHT, padx=5)

refresh_listbox(current_path, listbox)
update_tree()

listbox.bind("<Double-Button-1>", view_or_open)

root.mainloop()
