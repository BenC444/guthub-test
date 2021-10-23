# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:10:32 2021

@author: Ben Chapman
"""
import tkinter as tk

import PyPDF2

from PIL import Image

from PIL import ImageTk
 
root=tk.Tk()

canvas=tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=100)

#logo
logo=Image.open('logo.png')
logo=ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo

#this is the edit


root.mainloop()


