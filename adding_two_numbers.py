# importing the tkinter module

import tkinter

root = tkinter.Tk()   # creating a window
root.title("Temperature Converter")   # naming the recently created window
root.geometry("1000x500")   #  setting the size of the window
#root.config(bg="tan")   # setting the background color for the window


# Function to activate Celcius entry
def c_active():
    f_entry.configure(state='disable')
    c_entry.configure(state="normal")

# Function to activate Fahrenhiet entry
def f_active():
    c_entry.configure(state="disable")
    f_entry.configure(state="normal")

# Function to close the window
def close():
    root.destroy()

# Function to convert Celcius to Fahrenhiet
def Fahrenhiet():
    if c_entry["state"] == "normal" and c_entry.get() != "":
        celsius = float(c_entry.get())
        fahrenheit = (celsius*9/5)+32
        result_entry.insert(0, str(fahrenheit))

# Function to convert Fahrenhiet to Ceclius
def Celcius():
    if f_entry["state"] == "normal" and f_entry.get() != "":
        fahrenheit = float(f_entry.get())
        celsius = (fahrenheit-32)*5/9
        result_entry.insert(0, celsius)

 # Function for the clear button
def clear():
    c_entry.delete(0)
    f_entry.delete(0)
    result_entry.delete(0)


# Ceclius entry label
C_Frame_label = tkinter.LabelFrame(root, text="Celsius to Farenheit", padx=20, pady=20)
C_Frame_label.grid(row=2, column=0)

# Celcius entry
c_entry = tkinter.Entry(C_Frame_label, state="disable")
c_entry. grid(row=4, column=0)

# Celcius activating button
C_btn_active = tkinter.Button(root, text="Active -Celcius to Fahrenheit", command=c_active)
C_btn_active.grid(row=6, column=0)

# Fahrenhiet label
f_label = tkinter.LabelFrame(root, text="Fahrenheit to Celsius", padx=20, pady=20)
f_label.grid(row=2, column=5)

# Fahrenheit entry
f_entry = tkinter.Entry(f_label, state="disable")
f_entry.grid(row=4, column=5)

# Button to activate Fahrenheit entry
F_btn_active1 =tkinter.Button(root, text="Active -Fahrenheit to Celsius", command=f_active)
F_btn_active1.grid(row=6, column=5)


# Placing the exit button
exit_btn = tkinter.Button(text="Exit Program", command=close)
exit_btn.grid(row=9, column=6)

# placing the results button
result_btn = tkinter.Button(root, text="Convert C-F", command=Fahrenhiet)
result_btn.grid(row=7, column=2)


# creating the action button for converting Fahrenheit to Celsius and calling the convert_f()
result_btn2 = tkinter.Button(root, text="Convert F-C", command=Celcius)
result_btn2.grid(row=7, column=4)


# creating the result_entry or output entry
result_entry = tkinter.Entry(root, bg="light green")
result_entry.grid(row=8, column=3)



# creating the Clear button and calling the clear()
clear_btn = tkinter.Button(root, text="Clear", command=clear)
clear_btn.grid(row=8, column=6)

# starting the app
root.mainloop()
