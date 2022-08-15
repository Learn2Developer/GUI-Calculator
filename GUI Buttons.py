from faulthandler import disable
from tkinter import *
from turtle import color

root = Tk()


def my_click():
    my_label = Label(root, text="Look! I clicked a thing!!")
    my_label.pack()


my_button = Button(root, text="Click me!", command=my_click, fg="blue", bg="orange")
my_button.pack()


root.mainloop()
