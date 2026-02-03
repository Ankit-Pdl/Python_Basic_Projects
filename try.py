import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

# ---------- File Functions ----------

def create_file():
    filename = entry.get()
    if not filename:
        messagebox.showwarning("Warning", "Enter a filename")
        return
    try:
        with open(filename, 'x'):
            output.insert(tk.END, f"{filename} created successfully!\n")
    except FileExistsError:
        messagebox.showerror("Error", "File already exists")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def view_files():
    output.delete(1.0, tk.END)
    files = [f for f in os.listdir() if os.path.isfile(f)]
    if not files:
        output.insert(tk.END, "No files found.\n")
    else:
        output.insert(tk.END, "Files in directory:\n")
        for file in files:
            output.insert(tk.END, file + "\n")


def read_file():
    filename = entry.get()
    try:
        with open(filename, 'r') as f:
            output.delete(1.0, tk.END)
            output.insert(tk.END, f.read())
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")


def edit_file():
    filename = entry.get()
    content = entry_text.get()
    if not filename or not content:
        messagebox.showwarning("Warning", "Enter filename and text")
        return
    try:
        with open(filename, 'a') as f:
            f.write(content + '\n')
        output.insert(tk.END, f"Content added to {filename}\n")
        entry_text.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_file():
    filename = entry.get()
    if not filename:
        messagebox.showwarning("Warning", "Enter filename")
        return
    if messagebox.askyesno("Confirm", "Are you sure you want to delete?"):
        try:
            os.remove(filename)
            output.insert(tk.END, f"{filename} deleted\n")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")


# ---------- GUI ----------

root = tk.Tk()
root.title("File Management System")
root.geometry("500x500")

tk.Label(root, text="Filename").pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Label(root, text="Text (for edit)").pack()
entry_text = tk.Entry(root, width=40)
entry_text.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Create", width=10, command=create_file).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View", width=10, command=view_files).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Read", width=10, command=read_file).grid(row=1, column=0, padx=5)
tk.Button(btn_frame, text="Edit", width=10, command=edit_file).grid(row=1, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_file).grid(row=2, column=0, columnspan=2, pady=5)

output = scrolledtext.ScrolledText(root, width=55, height=15)
output.pack(pady=10)

root.mainloop()