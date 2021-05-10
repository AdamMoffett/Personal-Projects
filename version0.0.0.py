# initial testing for adding coin totals

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
def display(itemize, total, ammo_list, labels):
    
    # clear text fields
    itemize.delete('1.0', tk.END)
    total.delete('1.0', tk.END)
    
    # initialize temp varialbes
    final = [0, 0, 0]
    # coins = [0, 0, 0]
    
    # coin formot = G.SCI
    # Gold.SilverCopperIron
    # calculate itemized values
    if ammo_list[0].get() != '0':
        # black powder
        bp = int(ammo_list[0].get()) * 0.75 # 7s 5c to craft
        bpl = cFilter(bp)
        final = add(bpl, final)
        itemize.insert(tk.END, f'Black Powder: {bpl[0]}g {bpl[1]}s {bpl[2]}c \n')
        
    if ammo_list[1].get() != '0':
        # bullet
        bullet = int(ammo_list[1].get()) * .075 
        bl = cFilter(bullet)
        final = add(bl, final)
        itemize.insert(tk.END, f'Bullet: {bl[0]}g {bl[1]}s {bl[2]}c\n')
        
    if ammo_list[2].get() != '0':
        # Adamantine Bullet
        adamantite = int(ammo_list[2].get()) * 4.575
        ad = cFilter(adamantite)
        final = add(ad, final)
        itemize.insert(tk.END, f'Bullet (Adamantite): {ad[0]}g {ad[1]}s {ad[2]}c\n')
        
    if ammo_list[3].get() != '0':
        # Silver Bullet
        sBullet = int(ammo_list[3].get()) * 1.875 
        sb = cFilter(sBullet)
        final = add(sb, final)
        itemize.insert(tk.END, f'Bullet (Silver): {sb[0]}g {sb[1]}s {sb[2]}c\n')
        
    if ammo_list[4].get() != '0':
        # Cold Iron Bullet
        cBullet = int(ammo_list[4].get()) * .15
        cb = cFilter(cBullet)
        final = add(cb, final)
        itemize.insert(tk.END, f'Bullet (Cold Iron): {cb[0]}g {cb[1]}s {cb[2]}c\n')
        
    if ammo_list[5].get() != '0':
        # Paper Shot
        pShot = int(ammo_list[5].get()) * 4.5
        ps = cFilter(pShot)
        final = add(ps, final)
        itemize.insert(tk.END, f'Paper Shot: {ps[0]}g {ps[1]}s {ps[2]}c\n')
        
        
    total.insert(tk.END, f' {final[0]}g {final[1]}s {final[2]}c')
    
def main():
    
    window = tk.Tk()
    window.title("Pathfinder Ammo Calculator v0.0.0")
    
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
             'Bullet (Adamantine)',
             'Bullet (Silver)',
             'Bullet (Cold Iron)',
             'Paper Shot']
    
    ammo_list = []
    
    for idx, text in enumerate(labels):
        label = tk.Label(iFrame, text=text)
        label.grid(row=idx, column=0, sticky="W")
        
        entry = ttk.Entry(iFrame, width=5)
        entry.grid(row=idx, column=1, pady=1)
        entry.insert(tk.END, 0)
        ammo_list.append(entry)
      
    # button to trigger calculations and display output
    cButton = ttk.Button(iFrame, text="Calculate", command= lambda : display(itemize, total, ammo_list, labels))
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