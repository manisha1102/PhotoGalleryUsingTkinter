# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:55:30 2021

@author: manisha
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My Gallery')
root.geometry('1010x900+30+30')

myimg1 = Image.open('dog1.jpg')
#myimg1 = myimg1.resize((1000, 700), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(myimg1.resize((1000, 700)))

myimg2 = Image.open('dog2.jpg')
#myimg2 = myimg2.resize((1000, 7000), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(myimg2.resize((1000, 700)))

myimg3 = Image.open('dog3.jpg')
#myimg3 = myimg3.resize((1000, 700), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(myimg3.resize((1000, 700)))

myimg4 = Image.open('dog4.jpg')
#myimg4 = myimg4.resize((1000, 700), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(myimg4.resize((1000, 700)))

myimg5 = Image.open('dog5.jpg')
##myimg5 = myimg5.resize((1000, 700), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(myimg5.resize((1000, 700)))

myimg6 = Image.open('dog6.jpg')
#myimg6 = myimg6.resize((1000, 700), Image.ANTIALIAS)
img6 = ImageTk.PhotoImage(myimg6.resize((1000, 700)))

myimg7 = Image.open('dog7.jpg')
#myimg7 = myimg7.resize((1000, 700), Image.ANTIALIAS)
img7 = ImageTk.PhotoImage(myimg7.resize((1000, 700)))

image_list = [img1, img2, img3, img4, img5, img6, img7]

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

def backward(num):
    global image_list
    global label
    global button_prev
    global button_next
    
    label.grid_forget()
    label = Label(image=image_list[num-1])
    label.grid(row=0, column=0, columnspan=3)
    
    button_prev = Button(root, text='<<', padx=50, bg='green', fg='white', command=lambda: backward(num-1))
    button_next = Button(root, text='>>', padx=50, bg='green', fg='white', command=lambda: forward(num+1))
    status = Label(root, text='Image '+str(num)+' of '+str(len(image_list)))
    
    if num==1:
        button_prev = Button(root, text='<<', padx=50, bg='green', fg='white', state=DISABLED)
    
    button_prev.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3)

def forward(num):
    global image_list
    global label
    global button_prev
    global button_next
    
    label.grid_forget()
    label = Label(image=image_list[num-1])
    label.grid(row=0, column=0, columnspan=3)
    
    button_prev = Button(root, text='<<', padx=50, bg='green', fg='white',  command=lambda: backward(num-1))
    button_next = Button(root, text='>>', padx=50, bg='green', fg='white', command=lambda: forward(num+1))
    status = Label(root, text='Image '+str(num)+' of '+str(len(image_list)))
    
    if num==7:
        button_next = Button(root, text='>>', padx=50, bg='green', fg='white', state=DISABLED)
    
    button_prev.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3)

button_prev = Button(root, text='<<', padx=50, bg='green', fg='white', state=DISABLED, command= backward)
button_next = Button(root, text='>>', padx=50, bg='green', fg='white', command=lambda: forward(2))
button_exit = Button(root, text='EXIT GALLERY', bg='green', fg='white', padx=80, command=root.destroy)

status = Label(root, text='Image 1 of '+str(len(image_list)))

button_prev.grid(row=1, column=0)
button_next.grid(row=1, column=2)
button_exit.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3)




root.mainloop()