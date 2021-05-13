# calculate the probablity of getting 1 success in x tries based on a % chance
# % chance of failure ^ (attempts)

import tkinter as tk

def calculate(chance,attempts):
    # convert the % chance to a decimal
    chanceV = (float(chance) / 100)
    # convert # of attempts from str to int
    attemptsV = int(attempts)
    # raises the chance of a success to the power of how many attempts are being made
    output = chanceV ** attemptsV
    # convert the result to a percentage
    temp = output * 100
    hold = 100 - temp
    # print("%.2f" % hold)
    # clear any previous output
    output_txt.delete(1.0, "end-1c")
    # print to output field with 2 sig figs
    output_txt.insert("end-1c", "There is a %.2f percent chance of getting 1 success" % hold)
    
# make the window
window = tk.Tk()
window.title("Chance Calculator")

window.columnconfigure(0, minsize=100, weight=1)
window.rowconfigure(5, minsize=50, weight=1)

percent_lbl = tk.Label(window, text="% Chance of failure")
percent_lbl.grid(row=0,column=0,sticky="ew")

value_ent = tk.Entry(window, width=20, relief="solid")
value_ent.grid(row=1,column=0,padx=5,sticky="ew")

attempt_lbl = tk.Label(window, text="# of attempts")
attempt_lbl.grid(row=2,column=0,sticky="ew")

attempt_ent = tk.Entry(window, width=20, relief="solid")
attempt_ent.grid(row=3,column=0,padx=5,sticky="ew")

calc_btn = tk.Button(window, text="Calculate", relief="raised",bd=2,command=lambda : calculate(value_ent.get(), attempt_ent.get()))
calc_btn.grid(row=4,column=0,padx=5,pady=5,sticky="ew")

output_txt = tk.Text(window, width=42, height=10, bd=2, relief="solid")
output_txt.grid(row=5,column=0,pady=5,padx=5,sticky="nsew")

window.mainloop()

#idea for layout
#lbl
#ent
#lbl
#ent
#btn
