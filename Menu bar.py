import tkinter as tk
from tkinter import *


root=tk.Tk()
root.title("IDLE shell 3.11.5")
root.minsize(width=500, height=500)

menu_bar=tk.Menu(root)

file_menu=tk.Menu(menu_bar, tearoff=0)
edit_menu=tk.Menu(menu_bar, tearoff=0)
format_menu=tk.Menu(menu_bar,tearoff=0)
run_menu=tk.Menu(menu_bar,tearoff=0)
options_menu=tk.Menu(menu_bar,tearoff=0)
window_menu=tk.Menu(menu_bar,tearoff=0)
Help_menu=tk.Menu(menu_bar,tearoff=0)

#file dropdown
file_menu.add_command(label="New file")
file_menu.add_command(label="Open")
file_menu.add_command(label="Open module")
file_menu.add_command(label="Recent files")
file_menu.add_command(label="Module browser")
file_menu.add_command(label="Path browser")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as")
file_menu.add_command(label="Save Copy As")
file_menu.add_command(label="Print window")
file_menu.add_command(label="Close window")
file_menu.add_command(label="Exit IDLE")


#edit dropdown
edit_menu.add_command(label="Undo   Ctrl+Z")
edit_menu.add_command(label="Redo  Ctrl+Shift+Z")
edit_menu.add_command(label="Select all Ctrl+A")
edit_menu.add_command(label="Cut  Ctrl+X")
edit_menu.add_command(label="Copy  Ctrl+C")
edit_menu.add_command(label="Paste   Ctrl+V")
edit_menu.add_command(label="Find   Ctrl+F")
edit_menu.add_command(label="Find again   Ctrl+G")
edit_menu.add_command(label="Find selection   Ctrl+F3")
edit_menu.add_command(label="Find in files   Alt+F3")
edit_menu.add_command(label="Replace   Ctrl+H")
edit_menu.add_command(label="Go to line   Alt+G")
edit_menu.add_command(label="Show  compilations   Ctrl+space")
edit_menu.add_command(label="Expand word   Alt+/")
edit_menu.add_command(label="show call tip   Ctrl+backslash")
edit_menu.add_command(label="show surronding Parrens   Ctrl+0")

#Format
format_menu.add_command(label="Format paragraph   Alt+Q")
format_menu.add_command(label="Indent region  Ctrl+]")
format_menu.add_command(label="Dedent region   Ctrl+[")
format_menu.add_command(label="Comment out region   Alt+3")
format_menu.add_command(label="Uncomment region     Alt+4")
format_menu.add_command(label="Tabify region     Alt+5")
format_menu.add_command(label="Untabify region   Alt+6")
format_menu.add_command(label="Toggle Tabs       Alt+T")
format_menu.add_command(label="New indent width     Alt+U")
format_menu.add_command(label="Strip trailing whitespace")

#Run
run_menu.add_command(label="Run Module   F5")
run_menu.add_command(label="Run... Customized Shift+F5")
run_menu.add_command(label="Check Module   Alt+X")
run_menu.add_command(label="Python shell")


#options
options_menu.add_command(label="Configure IDLE")
options_menu.add_command(label="Show code context")
options_menu.add_command(label="Show show line numbers")
options_menu.add_command(label="Zoom height  Alt+2")


#windows
window_menu.add_command(label="IDLE Shell 3.11.5")
window_menu.add_command(label="Project.py")


#Help
Help_menu.add_command(label="About IDLE")
Help_menu.add_command(label="IDLE Doc")
Help_menu.add_command(label="Python Doc  F1")
Help_menu.add_command(label="Turtle Demo")
















#menu
menu_bar.add_cascade(label="File",menu=file_menu)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
menu_bar.add_cascade(label="Format",menu=format_menu)
menu_bar.add_cascade(label="Run",menu=run_menu)
menu_bar.add_cascade(label="Options",menu=options_menu)
menu_bar.add_cascade(label="Window",menu=window_menu)
menu_bar.add_cascade(label="Help",menu=Help_menu)

root.config(menu=menu_bar)
root.mainloop()
