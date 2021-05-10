# making the % of book cost dynamic
# and allowing the user to decide the %
# changed cost to reflect 100% book cost

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
def display(itemize, total, ammo_list, labels, cost, bCost):
    """TO DO"""
    # add bookCost as a variable to be passed to display
    
    """END"""
        
    # clear text fields
    itemize.delete('1.0', tk.END)
    total.delete('1.0', tk.END)
    
    bCost = bCost.get()
    if not bCost.isnumeric() == True or len(bCost) > 3 or int(bCost)==0:
        msg = 'Make sure the % of book cost value is a numeric value betwen 1 and 100'
        mBox = tk.messagebox.showerror(title='Incorrect Value', message=msg)
        return
    
    bCost = int(bCost)/100
    # initialize temp varialbe
    final = [0, 0, 0]
    
    # create a dictionary for label cost pairs
    d = dict(zip(labels,cost))
    
    # iterate through dictionary to format values and print to text box
    idx = 0
    for key in d:
        # set item amount to 0 if entry is empty or has a non-numeric value
        if not ammo_list[idx].get().isnumeric() == True:
            ammo_list[idx].delete(0, tk.END)
            ammo_list[idx].insert(tk.END, 0)
        # only print itemized output for items with value > 0
        if int(ammo_list[idx].get()) > 0:
            # key value == base cost
            # base cost * % * amount
            d[key] = cFilter(d[key]*int(ammo_list[idx].get()) * bCost)
            final = add(d[key], final)
            itemize.insert(tk.END, f'{key}: {d[key][0]}g {d[key][1]}s {d[key][2]}c\n')
        idx+=1
        
    # display the total cost of all items in game currency    
    total.insert(tk.END, f'{final[0]}g {final[1]}s {final[2]}c')
    
def main():
    """TO DO"""
    # add bookCost as a variable to be passed to display
    # add an entry widget nested in labels for user input
        # Use [ ]% of book cost
    # change cost list to reflect 100% of book cost for crafting
    """END"""
    
    window = tk.Tk()
    window.title("Pathfinder Ammo Calculator v0.2.0")
    
    # frame for title text
    tFrame = tk.Frame(window)
    tFrame.grid(row=0, column=0, padx=5)
    
    tLabel = tk.Label(tFrame, text="Crafting Calculator")
    tLabel.grid(row=0, column=0, sticky="NSEW")
    
    # frame for deciding % cost by user input
    cFrame = tk.Frame(window)
    cFrame.grid(row=1,column=0, padx=5, pady=5)
    
    #
    label1 = tk.Label(cFrame, text='Ammo cost will be ')
    label1.grid(row=0,column=0)
    
    entry = ttk.Entry(cFrame, width=3)
    entry.grid(row=0,column=1)
    entry.insert(tk.END, 100)
    bCost = entry
    
    label2 = tk.Label(cFrame, text='% of book cost.')
    label2.grid(row=0, column=2)
    
    # frame for quantity input
    iFrame = tk.Frame(window)
    iFrame.grid(row=2, column=0, pady=5, padx=5)
       
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
    # cost for each item is at book cost
    # will be modified during display calculations
    cost = [1, # black powder
            0.1, # bullet
            0.5, #bullet (pitted)
            6.1, # bullet (Adamantine)
            2.5, # Bullet (Silver)
            0.2, # bullet (cold iron)
            0.1, # pellets
            20, # Alchemical cartridge, dragon's breath
            20, # Alchemical cartdidge, entangling shot
            5, #Alchemical cartdidge, flare
            6, # Alchemical cartdidge, paper shot
            6, # Alchemical cartdidge, salt shot
            7.5] # Metal cartridge
    
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
    cButton = ttk.Button(iFrame, text="Calculate", command= lambda : display(itemize, total, ammo_list, labels, cost, bCost))
    cButton.grid(row=6, column=3, pady=2)
    
    # frame for output
    oFrame = tk.Frame(window)
    oFrame.grid(row=3, column=0, pady=5)
    
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