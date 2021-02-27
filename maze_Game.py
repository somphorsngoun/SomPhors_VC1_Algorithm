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

levelArray = []
levelnumber = []
# Function .............................................................................


def find(event):
    global levelArray,levelnumber
    canvas1.create_rectangle(0, 0, 1000, 800, fill="orange")
    level = 1
    for index in range(len(levelArray)):
        if (levelArray[index][0] <= event.x and levelArray[index][2] >= event.x) and (levelArray[index][1] <= event.y and levelArray[index][3] >= event.y):
            level = index+1
            print(event,level)
        print(levelArray[index])
    positionX = 200
    positionY = 30
    file = open(str(level)+".txt", "r")
    array = file.read()
    array = array.split(';')
    for i in range(len(array)):
        array[i] = array[i].strip('\n')
        array[i] = array[i].split(',')
        for j in range(len(array[i])):
            array[i][j] = int(array[i][j])
    # print(array)
    file.close()
    for n in range(len(array)):
        for r in range(len(array[n])):
            if array[n][r] == 1:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="black", fill="black")
            else:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="white", fill="white")
            positionX +=30
        positionX = 200
        positionY += 30

def back(event):
    global bg,startbg
    canvas1.delete("back")
    canvas1.delete("level")
    # canvas1.delete("number")
    canvas1.delete("image")
    startbg()


def remove(event):
    canvas1.delete("remove")
    canvas1.delete("delete")
    canvas1.move("welcome", 0, 100)


def startNew(event):
    global bg,X,Y
    X = 180
    Y = 100
    number = 1

    # canvas1.create_rectangle(0, 0, 1000, 600, fill="white", tags="remove")
    bg = PhotoImage(file = "C:\\Users\\LYHENG\\Pictures\\Saved Pictures\\8667194144_e735ac328b_o.gif") 
    canvas1.create_image( 0, 0, image = bg, anchor = "nw", tags="image")
    canvas1.create_text(50, 40, text = "<<", fill="white", font="Times 30 italic bold", tags="back")
    
    for n in range(3):
        for r in range(5):
            Array = []
            levelnumber.append(number)
            X1 = X+100
            Y1 = Y+100
            canvas1.create_rectangle(X, Y, X1, Y1, outline="black", fill="white", tags="level")
            canvas1.create_text(X+50, Y+50, text = number, fill="orange", font="Times 35 italic bold", tags="level")
            Array.append(X)
            Array.append(Y)
            Array.append(X1)
            Array.append(Y1)
            X +=130
            number += 1
            levelArray.append(Array)
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
    # fondo = PhotoImage(file= 'C:\\Users\\LYHENG\\Pictures\\Saved Pictures\\—Pngtree—spaceship cartoon cartoon spaceship the_3923112.png')
    # background_label =canvas1.create_image(0, 0, image=fondo)
    
    #Start
    canvas1.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
    canvas1.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")
    canvas1.tag_bind("start", "<Button-1>", startNew)

    # Setting
    canvas1.create_rectangle(430, 320, 610, 380, fill="white", tags="setting")
    canvas1.create_text(515,350, text = "Setting", fill="black", font="Times 35 italic bold", tags="setting")
    canvas1.tag_bind("setting", "<Button-1>", settingNew)

    # Quit
    canvas1.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
    canvas1.create_text(515, 450, text = "Quit", fill="black", font="Times 35 italic bold", tags="quit")
    canvas1.tag_bind("quit", "<Button-1>", quitNew)

    canvas1.tag_bind("remove", "<Button-1>", remove)

def begin():
    canvas1.create_text(500, 500, text = "Loading...", fill="white", font="Times 20 italic bold", tags="welcome")
    canvas1.after(1000, startbg)
    # canvas1.bind("<Button-1>", startbg)




canvas1.tag_bind("back", "<Button-1>", back)

canvas1.tag_bind("level", "<Button-1>", find)


bg = PhotoImage(file = "C:\\Users\\LYHENG\\Pictures\\Saved Pictures\\431509ba45834631-.gif") 
canvas1.create_image( 0, 0, image = bg, anchor = "nw", tags="bg1")
begin()


# Execute tkinter 
root.mainloop()