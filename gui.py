import tkinter as tk
import psutil
from tkinter import ttk
import threading

def get_system_info():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    # Get RAM usage
    memory = psutil.virtual_memory()
    ram_usage = memory.percent
    # Get Disk usage
    disk_usage = psutil.disk_usage('/').percent

    return cpu_usage, ram_usage, disk_usage

def update_dashboard():
    cpu_usage, ram_usage, disk_usage = get_system_info()
    
    cpu_bar['value'] = cpu_usage
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    
    ram_bar['value'] = ram_usage
    ram_label.config(text=f"RAM Usage: {ram_usage}%")
    
    disk_bar['value'] = disk_usage
    disk_label.config(text=f"Disk Usage: {disk_usage}%")
    
    root.after(5000, update_dashboard)

root = tk.Tk()
root.title("System Monitor Dashboard")

cpu_label = tk.Label(root, text="CPU Usage: 0%")
cpu_label.pack()
cpu_bar = ttk.Progressbar(root, length=400, mode='determinate', maximum=100)
cpu_bar.pack()

ram_label = tk.Label(root, text="RAM Usage: 0%")
ram_label.pack()
ram_bar = ttk.Progressbar(root, length=400, mode='determinate', maximum=100)
ram_bar.pack()

disk_label = tk.Label(root, text="Disk Usage: 0%")
disk_label.pack()
disk_bar = ttk.Progressbar(root, length=400, mode='determinate', maximum=100)
disk_bar.pack()

# Run the update_dashboard function in a separate thread to prevent GUI freezing
def start_dashboard():
    update_dashboard()
    
dashboard_thread = threading.Thread(target=start_dashboard)
dashboard_thread.start()

root.mainloop()
