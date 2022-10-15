#---------------01001111 01110100 01110100 00110110 01110010 01001111 01110100 01110100 00110110 01110010--------------#
#
# Code Created By : Ott6r
# Addional Help By : Codemy.com ( thanks for the help <3 )
#
# License : Creative Commons Legal Code         |           CC0 1.0 Universal
#
# Version : 1.0.0-Alpha
#
#---------------01001111 01110100 01110100 00110110 01110010 01001111 01110100 01110100 00110110 01110010--------------#

# Imports For Program
from tkinter import *
from tkinter import font
import ctypes

# Creating Definitions & Fuctions For Basic Text Maniplulation

# Creating A Def For Being Able To See What User Has Seleted
def select():

    # Saves Selected Text In Variable
    selected = textbox.selection_get()

def bolder():

    # Saves A Font Type Called bold_font For Text Box Widget; Gives It Properites Of Bolding
    bold_font = font.Font(textbox, textbox.cget("font"))
    bold_font.configure(weight="bold")

    # Allows Tag To Change Text To Bold
    textbox.tag_configure("bold", font=bold_font)

    # Saves Current Seleted Tags From Text Into A Variable
    current_tags = textbox.tag_names("sel.first")

    # Logic For Checking If The Text Is Already Bolded Or Not
    if "bold" in current_tags:
        textbox.tag_remove("bold", "sel.first", "sel.last")
    else:
        textbox.tag_add("bold", "sel.first", "sel.last")

def italic_txt():

    # Saves A Font Type Called italics_font For Text Box Widget; Gives It Properites Of Italicizing
    italics_font = font.Font(textbox, textbox.cget("font"))
    italics_font.configure(slant="italic")

    # Allows Tag To Change Text To Italicize
    textbox.tag_configure("italic", font=italics_font)

    # Saves Current Seleted Tags From Text Into A Variable
    current_tags = textbox.tag_names("sel.first")

    # Logic For Checking If The Text Is Already Italicized Or Not
    if "italic" in current_tags:
        textbox.tag_remove("italic", "sel.first", "sel.last")
    else:
        textbox.tag_add("italic", "sel.first", "sel.last")

# Basic Boiler Info For Tkinter Window
root = Tk()
root.geometry("1000x800")
root.title('Minimus')

# Changes Background Of Window To Match Text Box
root.config(background="#171717")

# Addes Higher DPI Awareness To The Program; Allows For Better Resolution When Using App
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Creates Text Box For Entry And Editing
textbox = Text(

    master=root,

    font=("Arial", 15),

    relief=FLAT,

    bg="#171717",

    fg="white",

    insertbackground="white",

    selectbackground="white",

    selectforeground="black"

)

# Adds The Text Box Widget To The Window
textbox.pack(fill=BOTH, expand=TRUE, padx=40, pady=40)


# Allows The Window To Run
root.mainloop()

