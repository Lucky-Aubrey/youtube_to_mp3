# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 04:01:37 2023

@author: Lucky
"""

import tkinter as tk

def print_string():
    string = string_var.get()
    print(string)

# Create the main window
root = tk.Tk()
root.title("GUI")

# Create the text field
string_var = tk.StringVar()
string_entry = tk.Entry(root, textvariable=string_var)
string_entry.pack()

# Create the button
print_button = tk.Button(root, text="Print", command=print_string)
print_button.pack()

# Create the checkbox
check_var = tk.BooleanVar()
check_button = tk.Checkbutton(root, text="Check", variable=check_var)
check_button.pack()

# Run the main loop
root.mainloop()