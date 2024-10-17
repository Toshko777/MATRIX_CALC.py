import tkinter as tk
import subprocess
from tkinter import messagebox

def show_error():
    # Display an error message box
    messagebox.showerror("Error", "An unexpected error occurred.")

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

# Add a textbox (Entry widget)
textbox = tk.Entry(root)
textbox.place(x=50, y=30)  # Add some vertical padding
textbox.config(width=7)

textbox0 = tk.Entry(root)
textbox0.place(x=100, y=30)
textbox0.config(width=7)

textbox1 = tk.Entry(root)
textbox2 = tk.Entry(root)
textbox3 = tk.Entry(root)
textbox4 = tk.Entry(root)
textbox5 = tk.Entry(root)
textbox6 = tk.Entry(root)
textbox7 = tk.Entry(root)
textbox8 = tk.Entry(root)
textbox9 = tk.Entry(root)


def txt_in1():
    
    textbox1.place(x=50, y=30)  #1|1
    textbox1.config(width=7)

def txt_in2():
    
    textbox2.place(x=50, y=50) #2|1
    textbox2.config(width=7)

def txt_in3():
    
    textbox3.place(x=100, y=30) #1|2
    textbox3.config(width=7)

def txt_in4():
    
    textbox4.place(x=100, y=50) #2|2
    textbox4.config(width=7)

def txt_in5():
    
    textbox5.place(x=50, y=70) #3|1
    textbox5.config(width=7)

def txt_in6():
    
    textbox6.place(x=100, y=70) #3|2
    textbox6.config(width=7)

def txt_in7():
    
    textbox7.place(x=150, y=30) #1|3
    textbox7.config(width=7)

def txt_in8():
    
    textbox8.place(x=150, y=50) #2|3
    textbox8.config(width=7)

def txt_in9():
    
    textbox9.place(x=150, y=70) #3|3
    textbox9.config(width=7)





def hide_button():
    button.destroy() #----> Hides the button




def get_text():
    numberx = int(textbox.get())
    numbery = int(textbox0.get())

    if numberx ==1 and numbery==1:
        txt_in1()
    elif numberx ==2 and numbery ==1:
        txt_in1()
        txt_in2()
    elif numberx ==1 and numbery ==2:
        txt_in1()
        txt_in3()
    elif numberx ==2 and numbery ==2:
        txt_in1()
        txt_in2()
        txt_in3()
        txt_in4()
    elif numberx ==3 and numbery==1:
        txt_in1()
        txt_in2()
        txt_in5()
    elif numberx ==3 and numbery==2:
        txt_in1()
        txt_in2()
        txt_in3()
        txt_in4()
        txt_in5()
        txt_in6()
    elif numberx == 1 and numbery==3:
        txt_in1()
        txt_in3()
        txt_in7()
    elif numberx == 2 and numbery==3:
        txt_in1()
        txt_in2()
        txt_in3()
        txt_in4()
        txt_in7()
        txt_in8()
    elif numberx == 3 and numbery==3:
        txt_in1()
        txt_in2()
        txt_in3()
        txt_in4()
        txt_in5()
        txt_in6()
        txt_in7()
        txt_in8()
        txt_in9()
    else:
       root.destroy() 
       show_error()
        
def print_matrix():   #el sedi za element

    numberx = int(textbox.get())
    numbery = int(textbox0.get())

    row= numberx
    column= numbery


    el1=int(textbox1.get()) #1|1
    el2=int(textbox2.get()) #2|1
    el3=int(textbox3.get()) #1|2
    el4=int(textbox4.get()) #2|2
    el5=int(textbox5.get()) #3|1
    el6=int(textbox6.get()) #3|2
    el7=int(textbox7.get()) #1|3
    el8=int(textbox8.get()) #2|3
    el9=int(textbox9.get()) #3|3


   

    


def smth():
    for i in range(5):
        for j in range(5):
            label32 = tk.Label(root, text=f"{i + 1}", font=("Arial", 14))
        label32.pack(pady=5)  # Use pack() to add the label to the window



def mltp_commands():# poneje piton e smotan trqbwa da ima funkciq za nqkolko komandi
    get_text()
    hide_button()
    textbox.destroy()
    textbox0.destroy()
    label.destroy()
    label1.destroy()
    label2.destroy()
    smth()





button = tk.Button(root, text="Print Text", command=mltp_commands)
button.place(x=50, y=50)

#starting the window
root.mainloop()
