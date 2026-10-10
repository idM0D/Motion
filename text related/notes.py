import tkinter as tk

root = tk.Tk()
root.title("note")
root.geometry("400x600")

editor = tk.Text(root)
editor.pack(expand = True, fill = "both")
root.mainloop()



text = editor.get("1.0", "end-1c")
