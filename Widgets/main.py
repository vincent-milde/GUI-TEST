import tkinter as tk
from tkinter import ttk

def buttonFunction():
    print("a button was pressed")

def butFunction():
    stringVar.set("Hello")
#Create window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

#ttk label
Label = ttk.Label(master = window, text="Nice")
Label.pack()

#tk Text
text = tk.Text(master = window)
text.pack()

#tk entry
entry = ttk.Entry(master = window)
entry.pack()

#exercise
#text label that prints hello when a button is pressed
stringVar = tk.StringVar()
label2 = ttk.Label(master = window, text = "", textvariabl = stringVar )
button2 = ttk.Button(master = window, text = "print hello", command = butFunction)
label2.pack()
button2.pack()

#ttk button
button = ttk.Button(master = window, text = "Button", command = buttonFunction)
button.pack()

#run
window.mainloop()