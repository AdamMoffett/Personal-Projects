# added dictionary for calculations
# to allow for future changes and avoid hard coding values

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
    window.title("Pathfinder Ammo Calculator v0.0.1")
    
    # frame for title text
    tFrame = tk.Frame(window)
    tFrame.grid(row=0, column=0, padx=5)
    
    tLabel = tk.Label(tFrame, text="Crafting Calculator")
    tLabel.grid(row=0, column=0, sticky="NSEW")
    
    # frame for quantity input
    iFrame = tk.Frame(window)
    iFrame.grid(row=1, column=0, pady=5, padx=5)
        
    labels = ['Black Powder',
             'Bullet',
             'Bullet (Adamantite)',
             'Bullet (Silver)',
             'Bullet (Cold Iron)',
             'Paper Shot']
    
    # cost of each item corresponding to
    # the order of items in 'labels'
    cost = [0.75,
            .075,
            4.575,
            1.875,
            .15,
            4.5]
    
    ammo_list = []
    
    for idx, text in enumerate(labels):
        label = tk.Label(iFrame, text=text)
        label.grid(row=idx, column=0, sticky="W")
        
        entry = ttk.Entry(iFrame, width=5)
        entry.grid(row=idx, column=1, pady=1)
        entry.insert(tk.END, 0)
        ammo_list.append(entry)
      
    # button to trigger calculations and display output
    cButton = ttk.Button(iFrame, text="Calculate", command= lambda : display(itemize, total, ammo_list, labels, cost))
    cButton.grid(row=6, column=1)
    
    # frame for output
    oFrame = tk.Frame(window)
    oFrame.grid(row=2, column=0, pady=5)
    
    itemize = tk.Text(oFrame, height=7, width=50)
    itemize.grid(row=0, column=0)
    
    total = tk.Text(oFrame, height=5, width=50)
    total.grid(row=1, column=0, pady=5, padx=5)
    
    window.mainloop()
    
main()