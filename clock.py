import tkinter as tk
from datetime import datetime
import pytz  # pip install pytz

def update_time():
    # Get current EST time
    est = pytz.timezone('US/Eastern')
    current_time = datetime.now(est).strftime('%Y-%m-%d %H:%M:%S')
    
    # Update label text
    time_label.config(text=current_time)
    
    # Schedule the function to run again after 1000 ms (1 second)
    root.after(1000, update_time)

# Create main window
root = tk.Tk()
root.title("EST Time Display")
root.geometry("260x100")
root.wm_attributes("-topmost", True)

# Create label for time
time_label = tk.Label(root, font=("Helvetica", 20), fg="white", bg="black")
time_label.pack(expand=True, fill="both")

# Start updating time
update_time()

# Run the Tkinter event loop
root.mainloop()