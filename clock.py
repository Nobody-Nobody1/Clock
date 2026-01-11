import tkinter as tk
root = tk.Tk()
root.title("My Tkinter App")
root.geometry("400x300")
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)
root.mainloop()