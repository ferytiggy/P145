# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:50:54 2023

@author: Aidan
"""

from tkinter import *



root= Tk()

root.title("P145")

root.geometry("400x200")

resultado=Label(root)


def add():
    result= 3*7
    
    resultado["text"]= result
    
btn = Button(root, text="Multiplicar", command=add)

resultado.pack()

btn.pack()







root.mainloop()
