# changing text boxes to read only
# to prevent the user from adding text to the output boxes

import tkinter as tk
from tkinter import ttk
from math import floor

# function to convert decimal to coin values
# print itemized conversion?
def cFilter(money):
    
    gold = floor(money)
    money -= gold
    silver = floor(money  * 10)
    copper = floor(money * 100) - (silver * 10)
    
    coins = [gold, silver, copper]
    return coins

# this function will filter all coin values to gold 
# with leftover silver and copper values
def add(money, total):
    
    total[0] += money[0] # gold
    total[1] += money[1] # silver
    total[2] += money[2] # copper
    
    return total

# function to display desired output 
# for itemized and total cost areas
def display(itemize, total, ammo_list, labels, cost):
    
    # clear text fields
    itemize.delete('1.0', tk.END)
    total.delete('1.0', tk.END)
    
    # initialize temp varialbe
    final = [0, 0, 0]
    
    # create a dictionary for label cost pairs
    d = dict(zip(labels,cost))
    
    # iterate through dictionary to format values and print to text box
    idx = 0
    for key in d:
        d[key] = cFilter(d[key]*int(ammo_list[idx].get()))
        final = add(d[key], final)
        itemize.insert(tk.END, f'{key}: {d[key][0]}g {d[key][1]}s {d[key][2]}c\n')
        idx+=1
        
    total.insert(tk.END, f'{final[0]}g {final[1]}s {final[2]}c')
    
def main():
    
    window = tk.Tk()
    window.title("Pathfinder Ammo Calculator v0.1.1")
    
    # frame for title text
    tFrame = tk.Frame(window)
    tFrame.grid(row=0, column=0, padx=5)
    
    tLabel = tk.Label(tFrame, text="Crafting Calculator")
    tLabel.grid(row=0, column=0, sticky="NSEW")
    
    # frame for quantity input
    iFrame = tk.Frame(window)
    iFrame.grid(row=1, column=0, pady=5, padx=5)
       
    # total = 13
    labels = ['Black Powder',
             'Bullet',
             'Bullet (Pitted)',
             'Bullet (Adamantine)',
             'Bullet (Silver)',
             'Bullet (Cold Iron)',
             'Pellets', # idx = 6
             "Alchemical cartridge, dragon's breath",
             'Alchemical cartdidge, entangling shot',
             'Alchemical cartdidge, flare',
             'Alchemical cartdidge, paper shot',
             'Alchemical cartdidge, salt shot',
             'Metal cartridge']
    
    # cost of each item corresponding to
    # the order of items in 'labels'
    cost = [0.75, # black powder
            0.075, # bullet
            0.375, #bullet (pitted)
            4.575, # bullet (Adamantine)
            1.875, # Bullet (Silver)
            0.15, # bullet (cold iron)
            0.075, # pellets
            15, # Alchemical cartridge, dragon's breath
            15, # Alchemical cartdidge, entangling shot
            3.75, #Alchemical cartdidge, flare
            4.5, # Alchemical cartdidge, paper shot
            4.5, # Alchemical cartdidge, salt shot
            5.625] # Metal cartridge
    
    ammo_list = []
    
    for idx, text in enumerate(labels):
        if idx > 6:
            label = tk.Label(iFrame, text=text)
            label.grid(row=idx-7, column=2, padx=3,sticky="W")
            
            entry = ttk.Entry(iFrame, width=5)
            entry.grid(row=idx-7, column=3, pady=1)
            entry.insert(tk.END, 0)
            ammo_list.append(entry)
        else:
            label = tk.Label(iFrame, text=text)
            label.grid(row=idx, column=0, padx=3, sticky="W")
            
            entry = ttk.Entry(iFrame, width=5)
            entry.grid(row=idx, column=1, pady=1)
            entry.insert(tk.END, 0)
            ammo_list.append(entry)
      
    # button to trigger calculations and display output
    cButton = ttk.Button(iFrame, text="Calculate", command= lambda : display(itemize, total, ammo_list, labels, cost))
    cButton.grid(row=6, column=3, pady=2)
    
    # frame for output
    oFrame = tk.Frame(window)
    oFrame.grid(row=2, column=0, pady=5)
    
    itemize = tk.Text(oFrame, height=7, width=55)
    itemize.grid(row=0, column=0)
    # prevent user from typing in to the text widget
    itemize.bind("<Key>", lambda e: "break")
    
    total = tk.Text(oFrame, height=5, width=55)
    total.grid(row=1, column=0, pady=5, padx=5)
    # prevent user from typing in to the text widget
    total.bind("<Key>", lambda e: "break")
    
    window.mainloop()
    
main()