import tkinter as tk
from tkinter import messagebox

def show_error():
    messagebox.showerror("Error", "An unexpected error occurred.")

def show_warning():
    messagebox.showwarning("Warning", "The textbox is empty!")

# creating the window
root = tk.Tk()
root.title("Matrix Calculator")
root.geometry("600x400")

label = tk.Label(root, text="Enter Matrix size")
label.place(x=50, y=0)

label1 = tk.Label(root, text="X")
label1.place(x=50, y=15)

label2 = tk.Label(root, text="Y")
label2.place(x=100, y=15)

textbox = tk.Entry(root)
textbox.place(x=50, y=30)  
textbox.config(width=7)

textbox0 = tk.Entry(root)
textbox0.place(x=100, y=30)
textbox0.config(width=7)

global_x = 0
global_y = 0
global_matrix = []

# Define identity matrix
def matrix_1():
    Rows = global_x
    Columns = global_y
    matri1 = [[1 if rows == columns else 0 for columns in range(Columns)] for rows in range(Rows)]
    
    print("Identity Matrix:")
    for row in matri1:
        print(" ".join(f"({cell})" for cell in row))

# Hide the button
def hide_button():
    button.destroy()

# Retrieve input and create matrix
def get_text():
    enrty1 = textbox.get()
    entry2 = textbox0.get()

    if not enrty1 or not entry2:
        show_warning()
        return

    global global_x, global_y, global_matrix
    global_x = int(enrty1)
    global_y = int(entry2)
    
    
    textboxes = []

    # Generate the textboxes and store references
    for row in range(global_x):
        arr2 = []
        for column in range(global_y):
            i = 50 * column  # Distance between columns
            j = 30 * row     # Distance between rows
            
            # Create a unique textbox for each cell
            textbox_prime = tk.Entry(root, width=7)
            textbox_prime.place(x=50 + i, y=60 + j)
            arr2.append(textbox_prime)  # Store textbox reference in arr2

        textboxes.append(arr2)  # Store each row of textboxes in textboxes

    global_matrix = [[0] * global_y for _ in range(global_x)]  # Initialize the matrix with zeros

    # Update global_matrix after values are entered in textboxes
    def update_matrix():
        for row in range(global_x):
            for column in range(global_y):
                try:
                    global_matrix[row][column] = int(textboxes[row][column].get())
                except ValueError:
                    global_matrix[row][column] = 0  # Default to 0 if no valid input

        button2.place(x=350, y=10)

    # Button to confirm matrix input
    confirm_button = tk.Button(root, text="Confirm Matrix", command=update_matrix)
    confirm_button.place(x=200, y=10)

# Handle multiple commands
def mltp_commands():
    get_text()
    hide_button()
    textbox.destroy()
    textbox0.destroy()
    label.destroy()
    label1.destroy()
    label2.destroy()

# Print matrix contents
def print_matrix():
    matrix_1()
    
    # Create a new Toplevel window
    matrix_window = tk.Toplevel(root)
    matrix_window.title("Matrix Contents")
    matrix_window.geometry("200x200")

    for row in range(global_x):
        for column in range(global_y):
            # Display each matrix element in the new window
            value = global_matrix[row][column]
            label = tk.Label(matrix_window, text=f"{value}", borderwidth=1, relief="solid", width=5, height=2)
            label.grid(row=row, column=column, padx=5, pady=5)

# Buttons
button = tk.Button(root, text="Enter", command=mltp_commands)
button.place(x=50, y=50)

button2 = tk.Button(root, text="Print Matrix", command=print_matrix)

# Start the window
root.mainloop()
