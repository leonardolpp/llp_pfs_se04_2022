from tkinter import Tk
from tkinter import messagebox

root = Tk()
root.withdraw()

messagebox.showinfo(message="Mensaje", title="Título")

# example string
string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())

# string with numbers
# all alphabets should be lowercase
string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())
txt = "Hello my friends"

x = txt.upper()