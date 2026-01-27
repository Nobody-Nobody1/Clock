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

def place_at_bottom():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    win_width = 250
    win_height = 45
    x = (screen_width - win_width) // 20  # Position
    y = screen_height - win_height - 0  # 0px above taskbar
    root.geometry(f"{win_width}x{win_height}+{x}+{y}")

def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    root.geometry(f"+{root.winfo_x() + deltax}+{root.winfo_y() + deltay}")
# Create main window
root = tk.Tk()
root.wm_attributes("-topmost", True)
root.resizable(True, True)

# Remove title bar
root.overrideredirect(True) # Removes title bar for free dragging

# Create label for time
time_label = tk.Label(root, font=("Times New Roman", 20), fg="white", bg="black")
time_label.pack(expand=True, fill="both")

frame = tk.Frame(root, bg="black")
frame.pack(fill="both", expand=True)

time_label.bind("<ButtonPress-1>", start_move)
time_label.bind("<B1-Motion>", do_move)

# Start updating time
update_time()

# Run the Tkinter event loop
root.mainloop()