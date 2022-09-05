# Six Sided Die Simulator Exercise, learning tkinter
import tkinter as tk
import random

def roll_die():
    value = random.randint(1, 6)
    lbl_die_results["text"] = value


window = tk.Tk()


# Button on top, results on bottom
window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

btn_die = tk.Button(master=window, text="Roll", command=roll_die)
btn_die.grid(row=0, column=0, sticky="NSEW") # Attach button to grid, then size it

lbl_die_results = tk.Label(master=window, text="...")
lbl_die_results.grid(row=1, column=0, sticky="NSEW")# Attach label to grid, then size


window.mainloop()


# Personal Notes
"""
- Before I can roll the die, I need to answer these questions:
1) How to create button with text "Roll"
    -> tk.Button is stored in a variable
2) How to create & update label with the results of the button click
    -> tk.Label is stored in a variable, and the results come from the dice roll function updating it
3) How do I create a random int generator function
    -> Import the random module, the create function 
        def roll_die(): <--- Name the function
            value = random.randint(1, 6) <--- Store random values from 1-6 in a var
            lbl_die_results["text"] = value <--- Get text index, set it to the new variable

"""