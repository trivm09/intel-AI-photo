import tkinter as tk
from itertools import cycle

class ImageSlideshow:

    def __init__(self, master, image_files, x, y, delay):
        self.master = master
        self.image_files = cycle(image_files)  # cycle through the images
        self.image = tk.PhotoImage(file=next(self.image_files))
        self.display = tk.Label(master, image=self.image)
        self.display.pack()
        self.delay = delay
        self.update_image()

    def update_image(self):
        self.image = tk.PhotoImage(file=next(self.image_files))
        self.display.config(image=self.image)
        self.master.after(self.delay, self.update_image)