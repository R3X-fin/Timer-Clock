from tkinter import Tk, Label, Entry, Button
from tkinter import ttk
import time
import threading
import pygame

# Initialize Pygame mixer for sound effects
pygame.mixer.init()

# Load the sound effect
sound_effect = pygame.mixer.Sound(r"path\to\sound\your\effect.wav")

def start_timer():
    try:
        # Stop any currently playing sound effect
        sound_effect.stop()

        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
        countdown_time = hours * 3600 + minutes * 60 + seconds
        for i in range(countdown_time, -1, -1):
            count(i)
            time.sleep(1)
        sound_effect.play()  # Play sound effect when timer reaches zero
    except ValueError:
        label.config(text="Invalid input")

def count(i):
    hours = i // 3600
    minutes = (i % 3600) // 60
    seconds = i % 60
    label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
    root.update()  # Update the GUI to reflect changes

def on_closing():
    sound_effect.stop()
    root.destroy()

root = Tk()
root.title("Timer")
root.geometry("450x200")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.configure("TLabel", background="#1e1e1e", foreground="#d4d4d4", font=("Helvetica", 14))
style.configure("TEntry", background="#1e1e1e", foreground="#4B0082", fieldbackground="#1e1e1e", font=("Helvetica", 14))
style.configure("TButton", background="#007acc", foreground="#4B0082", font=("Helvetica", 14), borderwidth=0)
style.map("TButton", background=[("active", "#005f9e")])

label = Label(root, text="00:00:00", font=("Helvetica", 48), bg="#1e1e1e", fg="#d4d4d4")
label.place(x=20, y=20)

hours_label = ttk.Label(root, text="Hours:")
hours_label.place(x=20, y=100)
hours_entry = ttk.Entry(root, width=5, foreground="#4B0082")
hours_entry.insert(0, "0")
hours_entry.place(x=80, y=100)

minutes_label = ttk.Label(root, text="Minutes:")
minutes_label.place(x=150, y=100)
minutes_entry = ttk.Entry(root, width=5, foreground="#4B0082")
minutes_entry.insert(0, "0")
minutes_entry.place(x=230, y=100)

seconds_label = ttk.Label(root, text="Seconds:")
seconds_label.place(x=300, y=100)
seconds_entry = ttk.Entry(root, width=5, foreground="#4B0082")
seconds_entry.insert(0, "0")
seconds_entry.place(x=380, y=100)

button = ttk.Button(root, text="Start Timer", command=lambda: threading.Thread(target=start_timer).start())
button.place(x=20, y=150)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()