# Temp converter using tkinter
import tkinter as tk


def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert
    result into results.
    Added a feature to check whether entries were numbers.
    The best part? No tutorial! Yes!
    """
    fahr = ent_farhen.get() # Gets data
    if fahr.isnumeric(): # Checks for numbers in string
        celsius = (5 / 9) * (float(fahr) - 32)
        lbl_celsius_results["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    else:
        lbl_celsius_results["text"] = f"Error, \N{DEGREE CELSIUS}"


window = tk.Tk()
window.title("Temp Converter by Tristan Griffin")
window.resizable(width=False, height=False)  # This prevents the window from resizing

frm_entry = tk.Frame(master=window) # Create frame within window specifically for form entry

ent_farhen = tk.Entry(master=frm_entry, width=10) # Insert form entry into frame
ent_farhen.grid(row=0, column=0, padx=10)

lbl_farhen = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
lbl_farhen.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
btn_convert.grid(row=0, column=2, pady=10)

lbl_celsius_results = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
lbl_celsius_results.grid(row=0, column=3, padx=10)

frm_entry.grid(row=0, column=0, padx=10)

window.mainloop()

# Personal Notes
"""

- Before I can convert the entry into a temp, I need to answer these:
1) How do I get the text from the entry?
    >>     fahr = ent_farhen.get() << Use .get() to pull the text from the entry space
    
2) How do I convert the text into usable and updatable information
    >>     celsius = (5/9) * (float(fahr) - 32)
    lbl_celsius_results["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    
3) How do I change the lbl_celsius to show the updated information?
    >>     celsius = (5/9) * (float(fahr) - 32)
    lbl_celsius_results["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    
4) How do I check to ensure only numbers are entered?
    >>     fahr = ent_farhen.get() # Gets data
    if fahr.isnumeric(): # Checks for numbers in string
        celsius = (5 / 9) * (float(fahr) - 32)
        lbl_celsius_results["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    else:
        lbl_celsius_results["text"] = f"Error, \N{DEGREE CELSIUS}"

"""
