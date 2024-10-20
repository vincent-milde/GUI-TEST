import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mileIn = entryInt.get()
    kmOut = (mileIn * 1.61 ) 
    outputStr.set(kmOut)


#window
window = ttk.Window(themename = 'darkly')
window.title('Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert )
entry.pack(side = 'left')
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
outputStr = tk.StringVar()
output_label = ttk.Label(
                         master = window,
                         text = 'output',
                         font = 'Calibri 18',
                         textvariable = outputStr)
output_label.pack()
#run
window.mainloop()