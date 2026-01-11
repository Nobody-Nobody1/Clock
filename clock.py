import tkinter as tk
from time import strftime

def update_time():
    """Update the clock label every second."""
    current_time = strftime('%H:%M:%S %p')  # 24-hour format with AM/PM
    label.config(text=current_time)
    label.after(1000, update_time)  # Schedule next update in 1 second

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)

# Clock label styling
label = tk.Label(
    root,
    font=('Arial', 40, 'bold'),
    background='black',
    foreground='cyan'
)
label.pack(anchor='center', expand=True)

# Start updating time
update_time()

# Run the application
root.mainloop()