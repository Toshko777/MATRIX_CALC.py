import tkinter as tk
import subprocess
from tkinter import messagebox

def show_error():
    # Display an greshka message box------ murzi me da e poveche ot 3x3
    messagebox.showerror("Error", "An unexpected error occurred.")

def show_warning():
    messagebox.showwarning("Warning", "The textbox is empty!")

#creating the window
root = tk.Tk()

root.title("Matrix Calculator")

root.geometry("600x400")

label = tk.Label(root, text="Enter Matrix size")
label.place(x=50, y=0)

label1 = tk.Label(root, text="X")
label1.place(x=50, y=15)

label2 = tk.Label(root, text="Y")
label2.place(x=100, y=15)

label3 = tk.Label(root, text="Enter Matrix")
label3.place(x=50, y=0)


textbox = tk.Entry(root)
textbox.place(x=50, y=30)  
textbox.config(width=7)

textbox0 = tk.Entry(root)
textbox0.place(x=100, y=30)
textbox0.config(width=7)








global_x=0
global_y=0

global_matrix=[]

#----------------------------------------------------------------------
def matrix_1():
    Rows=global_x
    Columns=global_y
    matri1=[]
    for rows in range(Rows):
        a=[]
        for columns in range(Columns):
            if rows == columns:
                a.append(int(1))
            else:
                a.append(int(0))
        matri1.append(a)

    for rows in range(Rows):
        for columns in range(Columns):
            print("(",matri1[rows][columns],")", end='')
        print()
    #----------------------------------------------------------------



def hide_button():
    button.destroy() #----> Hides the button---- useless fuction bukwalno trqbwa da q premestq w drugata 




def get_text():
    enrty1=textbox.get()
    entry2=textbox0.get()


    if (enrty1 == "" and entry2 =="") or enrty1 == "" or entry2 =="":
        show_warning()


    numberx = int(textbox.get())
    numbery = int(textbox0.get())
    
    global global_x 
    global_x = numberx

    global global_y
    global_y = numbery

    global global_matrix


    

    i=int(0)
    j=int(0)

    matrix2=[]
    
    
    
    for row in range(numberx):
        arr2 = []

        for column in range(numbery):

            i = 50 * (column)  # Distance between columns
            j = 30 * (row)     # Distance between rows


        # Create a unique textbox for each cell
            textbox_prime = tk.Entry(root, width=7)
            textbox_prime.place(x=50 + i, y=30 + j)

        # Function to create label at the same position as textbox
            def make_clearpr(textbox=textbox_prime, x=50 + i, y=30 + j):
                def clearpr(event=None):
                # Retrieve content from textbox
                    text_content = textbox.get()
                    print(f"Text Content for {x},{y}: {text_content}")
                # Create a label with the textbox content at the same position
                    label_prime = tk.Label(root, text=text_content)
                    label_prime.place(x=x, y=y)

                # Store the integer value in arr2 if needed
                    try:
                        arr2.append(int(text_content))
                    except ValueError:
                        arr2.append(0)

                # Hide the textbox
                    textbox.place_forget()
                return clearpr

        # Bind the Enter key for each unique textbox
            textbox_prime.bind("<Return>", make_clearpr())

        matrix2.append(arr2)
        global_matrix= matrix2
        print(f"Row {row} content: {arr2}")



    

   
    
    button2.place(x=200, y=200)
    

    
 



def mltp_commands():# poneje piton e smotan trqbwa da ima funkciq za nqkolko komandi
    get_text()
    hide_button()
    textbox.destroy()
    textbox0.destroy()
    label.destroy()
    label1.destroy()
    label2.destroy()
    
  
def print_matrix():

    matrix_1()

    print("Matrixp Contents:")
    for row in range(global_x):
        for column in range(global_y):
            try:
                print("|", global_matrix[row][column], "|", end=' ')
            except IndexError:
                print("Error: Index out of range for matrix2")
        print()



button = tk.Button(root, text="Enter", command=mltp_commands)
button.place(x=50, y=50)


button2 = tk.Button(root, text="Enter", command=print_matrix)






#hi

#starting the window
root.mainloop()
