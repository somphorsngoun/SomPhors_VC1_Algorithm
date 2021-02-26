# Import module  
from tkinter import *
import tkinter
# import os
  
# Create object  
root = Tk() 
  
# Adjust size  
root.geometry("1000x600") 
root.resizable(0,0)

# Create Canvas 
canvas1 = Canvas( root, width = 800, height = 600) 
canvas1.pack(fill = "both", expand = True) 

#Variable
X = 180
Y = 100
levelArray = []
number = 1
# Function .............................................................................

def remove(event):
    canvas1.delete("remove")
    canvas1.delete("delete")
    canvas1.move("welcome", 0, 100)


def startNew(event):
    global bg,X,Y,number
    # canvas1.create_rectangle(0, 0, 1000, 600, fill="white", tags="remove")
    bg = PhotoImage(file = "C:\\Users\\LYHENG\\Pictures\\Saved Pictures\\8667194144_e735ac328b_o.gif") 
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text(50, 40, text = "<<", fill="white", font="Times 30 italic bold", tags="<<")
    
    for n in range(3):
        Array = []
        for r in range(5):
            X1 = X+100
            Y1 = Y+100
            canvas1.create_rectangle(X, Y, X1, Y1, outline="black", fill="white")
            canvas1.create_text(X+50, Y+40, text = number, fill="orange", font="Times 35 italic bold")
            Array.append(X)
            Array.append(X1)
            Array.append(Y)
            Array.append(Y1)
            X +=130
            levelArray.append(Array)
            number +=1
        Y += 130
        X = 180
    
    print(levelArray)
def settingNew(event):
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 125, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    

def quitNew(event):
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 115, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas1.create_text(350, 130, anchor=W, font="Purisa",text="Most relationships seem so transitory")


def startbg():
    global bg
    bg = PhotoImage(file = "C:\\Users\\LYHENG\\Pictures\\Saved Pictures\\8670933798_2a8f52c6c6_o.gif") 


    # Display image 
    canvas1.create_image( 0, 0, image = bg, anchor = "nw") 

    # Add Text 
    canvas1.create_text(500, 150, text = "Welcome to the maze game!!!", fill="#0D4D8D", font="Times 35 italic bold", tags="welcome")


    canvas1.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
    canvas1.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")
    canvas1.tag_bind("start", "<Button-1>", startNew)

    canvas1.create_rectangle(430, 320, 610, 380, fill="white", tags="setting")
    canvas1.create_text(515,350, text = "Setting", fill="black", font="Times 35 italic bold", tags="setting")
    canvas1.tag_bind("setting", "<Button-1>", settingNew)

    canvas1.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
    canvas1.create_text(515, 450, text = "Quit", fill="black", font="Times 35 italic bold", tags="quit")
    canvas1.tag_bind("quit", "<Button-1>", quitNew)

    canvas1.tag_bind("remove", "<Button-1>", remove)

def begin():
    canvas1.create_text(500, 500, text = "Loading...", fill="white", font="Times 20 italic bold", tags="welcome")
    canvas1.after(1000, startbg)


bg = PhotoImage(file = "C:\\Users\\LYHENG\\Pictures\\Saved Pictures\\431509ba45834631-.gif") 
canvas1.create_image( 0, 0, image = bg, anchor = "nw", tags="bg1")
begin()


# Execute tkinter 
root.mainloop()