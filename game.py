from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from random import randint
import time
import playsound
import pyglet


root=Tk()
root.title("Rock Paper Scissor")
root.geometry("650x600")
filename = ImageTk.PhotoImage(Image.open('1.png'))
background_label =Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# root.configure(background='1.jpg')
# canvas=Canvas(root)
# canvas.pack()
# background_img=PhotoImage(file='1.jpg')
# background_label=Label(root,image=background_img)
# background_label.place(x=0,y=0,relwidth=1,relheight=1)
# background_label.pack()
you=0
comp=0
hi=Label(root,font=("Helvetica",12))
hi.config(text="Computer thinking!!\n\nComputer: common Mate!! make your choice\n")
hi.pack(pady=50)
# media = pyglet.media.load('1.mp3')
# media.play()
# pyglet.app.run()
def first():
    you=1
    comp=randint(1,3)
    spin(comp,you)

def second():
    you=2
    comp=randint(1,3)
    spin(comp,you)

def third():
    you=3
    comp=randint(1,3)
    spin(comp,you)

def spin(comp,you):
    #rock 1
    #paper 2
    #scissor 3
    

    if comp==you:
        win_lose_label.config(text="Tie")
        
    elif comp==1:
        if you==2:
           win_lose_label.config(text="Congo!! you won, Paper covered rock",textvariable=comp) 
        elif you==3:
            win_lose_label.config(text="You lose!! Rock smashed Scissor") 
    elif comp==2:
        if you==1:
            win_lose_label.config(text="You lose!! Rock got covered by paper") 
        elif you==3:
            win_lose_label.config(text="Congo!! You won, Scissor cut the paper") 
    elif comp==3:
        if you==1:
            win_lose_label.config(text="Congo!! Rock smashed Scissor") 
        elif you==2:
            win_lose_label.config(text="You lose!! Your paper got cut by Scissor")
    
    if comp==1:
        str="Rock"
    elif comp==2:
        str="Paper"
    else:
        str="Scissor"
    computer.config(text="Computer Choosed")
    computer1.config(text=str)
canvas=Canvas(root,height=600,width=600)
canvas.pack()
img_file = Image.open("rock.png")
img_file=img_file.resize((200,200))
img = ImageTk.PhotoImage(img_file)
button=Button(canvas,image=img,command=first).grid(row=0,column=0)



img_file1 = Image.open("paper.png")
img_file1=img_file1.resize((200,200))
img1 = ImageTk.PhotoImage(img_file1)
button1=Button(canvas,image=img1,command=second).grid(row=0,column=1)


img_file2 = Image.open("scissor.png")
img_file2=img_file2.resize((200,200))
img2 = ImageTk.PhotoImage(img_file2)
b3=Button(canvas,image=img2,command=third).grid(row=0,column=2)


win_lose_label=Label(root,text="",font=("Helvetica",14),bg='#F0E68C')
win_lose_label.pack(pady=20)
computer=Label(root,text=" ",font=("Helvetica",14),bg='#FFA07A')
computer.pack(pady=20)
computer1=Label(root,font=("Helvetica",14))
computer1.pack(pady=20)


root.mainloop()