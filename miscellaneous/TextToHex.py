import tkinter as tk
from tkinter import ttk


def textToHex(text, output):
    
    output.delete("1.0", tk.END)
    for letter in text:
        if (hex(ord(letter))[2:]) == '20':
            output.insert('1.0', " ")
        else:
            output.insert("1.0", hex(ord(letter))[2:])
                
                
root = tk.Tk()
root.title("Text to Hex!")

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

textlbl = tk.Label(frame, text="Type here!")
textlbl.grid(row=0, column=0, padx=5, pady=5, sticky="w")

textbx = tk.Text(frame, bg="White", height=10, width=40)
textbx.grid(row=1,column=0, padx=5, pady=5, sticky="nsew")

convertbtn = ttk.Button(frame, text="Convert", command= lambda :textToHex(textbx.get("1.0","end"), output))
convertbtn.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

output = tk.Text(frame, bg="White", height=10, width=40)
output.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

root.mainloop()


# textToHex(textbx.get("1.0","end"), output))
