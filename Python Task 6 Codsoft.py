# Import libraries
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

# Initialize window
root = Tk()
root.geometry('700x550')
root.config(bg='#f5e6d3')
root.title('Simple Notepad')
root.resizable(0, 0)

# Temporary storage for saved files
saved_files = {}

# Function to open the Home Page
def open_home():
    # Clear the current window
    for widget in root.winfo_children():
        widget.destroy()

    # Home page UI
    Label(root, text="Home Page", font=("Helvetica", 24, "bold"), bg="#f5e6d3").pack(pady=20)

    if saved_files:
        Label(root, text="Saved Files:", font=("Helvetica", 16, "bold"), bg="#f5e6d3").pack(pady=10)
        listbox = Listbox(root, font=("Helvetica", 14), width=50, height=10)
        listbox.pack(pady=10)

        for name in saved_files.keys():
            listbox.insert(END, name)

        # Button to open a selected file
        def open_selected_file():
            if listbox.curselection():
                selected = listbox.get(listbox.curselection())
                open_file(selected)
            else:
                messagebox.showwarning("No Selection", "Please select a file to open!")

        Button(root, text="Open File", font="Helvetica 14 bold", bg="#add8e6", command=open_selected_file).pack(pady=10)
    else:
        Label(root, text="No saved files found!", font=("Helvetica", 14), bg="#f5e6d3").pack(pady=10)

    # New file button
    Button(root, text="New File", font="Helvetica 14 bold", bg="#90ee90", command=new_file).pack(pady=10)

# Function to create a new file
def new_file():
    open_editor()

# Function to open the editor with file content (new or existing)
def open_editor(file_name=None):
    # Clear the current window
    for widget in root.winfo_children():
        widget.destroy()

    global temp_file_content
    temp_file_content = saved_files.get(file_name, "") if file_name else ""

    # Editor UI
    def save_file():
        global temp_file_content
        temp_file_content = text_area.get(1.0, END).strip()
        file_name = simpledialog.askstring("Save File", "Enter file name:")
        if file_name:
            saved_files[file_name] = temp_file_content
            messagebox.showinfo("Saved", f"File '{file_name}' saved successfully!")
            open_home()

    def close_editor():
        result = messagebox.askyesno("Confirmation", "Do you want to save the file before closing?")
        if result:
            save_file()
        open_home()

    # Menu bar
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Close", command=close_editor)
    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)

    Label(root, text="Notepad", font=("Helvetica", 24, "bold"), bg="#f5e6d3").pack(pady=10)

    # Text area
    text_area = Text(root, wrap=WORD, font=("Times New Roman", 14), bg="#ffffff", borderwidth=2, relief="sunken")
    text_area.pack(expand=1, fill=BOTH, padx=10, pady=10)

    # Load content if opening an existing file
    if temp_file_content:
        text_area.insert(1.0, temp_file_content)

# Function to open an existing file
def open_file(file_name):
    open_editor(file_name)

# Start the application with the Home Page
open_home()
root.mainloop()
