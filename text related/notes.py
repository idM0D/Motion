import tkinter as tk
import time

root = tk.Tk()
#winodw properties
root.title("note")
root.geometry("400x600")

#displaying the text editor
editor = tk.Text(root)
editor.pack(expand = True, fill = "both")
root.mainloop()
#to get the text written
text = editor.get("1.0", "end-1c")

def autosave1():
    #gghjh
    print()