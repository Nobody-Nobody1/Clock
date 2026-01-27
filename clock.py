import tkinter as tk
root = tk.Tk()
root.title("Keep Window on Top")
root.geometry("300x300")
# Create a new window
top_window = tk.Toplevel(root)
top_window.title("Top Window")
top_window.geometry("200x200")
# Set the top_window on top of the root window
top_window.wm_attributes("-topmost", True)
root.mainloop()