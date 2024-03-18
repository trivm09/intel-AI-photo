import tkinter as tk
from itertools import cycle
import os
import random
from PIL import Image, ImageTk

class ImageSlideshow:

    def __init__(self, master, image_files, x, y, delay):
        random.shuffle(image_files)
        self.master = master
        self.image_files = cycle(image_files)  # cycle through the images
        self.image = tk.PhotoImage(file=next(self.image_files))
        self.display = tk.Label(master, image=self.image)
        self.display.pack(side=tk.LEFT)
        self.delay = delay
        self.update_image()

    def update_image(self):
        self.image = ImageTk.PhotoImage(Image.open(next(self.image_files)).resize((x, y)))
        self.display.config(image=self.image)
        self.master.after(self.delay, self.update_image)


root = tk.Tk()
hand_drawing_dir = "assets/images/HandDrawing/"
hand_drawing_files = [hand_drawing_dir + img for img in os.listdir(hand_drawing_dir) if img.endswith(('.png', '.jpg', '.gif'))]

warter_color_dir = "assets/images/WaterColor/"
water_color_files = [warter_color_dir + img for img in os.listdir(warter_color_dir) if img.endswith(('.png', '.jpg', '.gif'))]

sunset_coast_dir = "assets/images/SunsetCoast/"
sunset_coast_files = [sunset_coast_dir + img for img in os.listdir(sunset_coast_dir) if img.endswith(('.png', '.jpg', '.gif'))]

fairy_tales_dir = "assets/images/FairyTales/"
fairy_tales_files = [fairy_tales_dir + img for img in os.listdir(fairy_tales_dir) if img.endswith(('.png', '.jpg', '.gif'))]

x = 256
y = 384
delay = 3000

hand_drawing = ImageSlideshow(root, hand_drawing_files, x, y, delay)
water_color = ImageSlideshow(root, water_color_files, x, y, delay)
sunset_coast = ImageSlideshow(root, sunset_coast_files, x, y, delay)
fairy_tale = ImageSlideshow(root, fairy_tales_files, x, y, delay)

root.mainloop()