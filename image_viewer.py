import random
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("picture1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("picture2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("picture3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("picture4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("picture5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward= Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back=Button(root, text='<<', command=lambda: back(image_number-1))

    if image_number==5:
        button_forward= Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number==1:
        button_back= Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state=DISABLED)
buttonquit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1,column=0)
buttonquit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()

