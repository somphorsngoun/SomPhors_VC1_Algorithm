# Import module  
from tkinter import *
import tkinter
from winsound import *
import winsound

# from glob import glob

# winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\1918.wav",
# winsound.SND_FILENAME)

# Create object  
root = Tk() 
root.title("Create by @SomPhors")
# Adjust size  
root.geometry("1000x600") 
root.resizable(0,0)

# Create Canvas 
canvas1 = Canvas( root, width = 800, height = 600) 
canvas1.pack(fill = "both", expand = True) 


#Variable
levelArray = []
levelnumber = []
array = []
# Function .............................................................................

def goUp(event):
    global array,levelArray,levelnumber
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\rockHit2.wav",
    winsound.SND_FILENAME)

    positionX = 200
    positionY = 30
    spacecraft = []
    for num1 in range(len(array)):
        for num2 in range(len(array[num1])):
            if array[num1][num2] == 2:
                spacecraft.append(num2)
                spacecraft.append(num1)
    if array[spacecraft[1]-1][spacecraft[0]] == 0:
        array[spacecraft[1]-1][spacecraft[0]] = 2
        array[spacecraft[1]][spacecraft[0]] = 0
    for n in range(len(array)):
        for r in range(len(array[n])):
            if array[n][r] == 1:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="darkblue", fill="darkblue", tags="wall")
            elif array[n][r] == 2:
                canvas1.create_image( positionX+5, positionY, image = spacecrafter1, anchor = "nw", tags="craft")
            elif array[n][r] == 3:
                canvas1.create_image( positionX, positionY, image = Earth, anchor = "nw", tags="craft")
            elif array[n][r] == 5:
                canvas1.create_image( positionX, positionY, image = Animy2, anchor = "nw", tags="animy")
            elif array[n][r] == 6:
                canvas1.create_image( positionX, positionY, image = Animy1, anchor = "nw", tags="animy")
            elif array[n][r] == 0:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="white", fill="white", tags="wall")

            positionX +=30
        positionX = 200
        positionY += 30
    
def goDown(event):
    global array,levelArray,levelnumber
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\rockHit2.wav",
    winsound.SND_FILENAME)
    positionX = 200
    positionY = 30
    spacecraft = []
    for num1 in range(len(array)):
        for num2 in range(len(array[num1])):
            if array[num1][num2] == 2:
                spacecraft.append(num2)
                spacecraft.append(num1)
    if array[spacecraft[1]+1][spacecraft[0]] == 0:
        array[spacecraft[1]+1][spacecraft[0]] = 2
        array[spacecraft[1]][spacecraft[0]] = 0
    for n in range(len(array)):
        for r in range(len(array[n])):
            if array[n][r] == 1:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="darkblue", fill="darkblue", tags="wall")
            elif array[n][r] == 2:
                canvas1.create_image( positionX+5, positionY-5, image = spacecrafter3, anchor = "nw", tags="craft")
            elif array[n][r] == 3:
                canvas1.create_image( positionX, positionY, image = Earth, anchor = "nw", tags="craft")
            elif array[n][r] == 5:
                canvas1.create_image( positionX, positionY, image = Animy2, anchor = "nw", tags="animy")
            elif array[n][r] == 6:
                canvas1.create_image( positionX, positionY, image = Animy1, anchor = "nw", tags="animy")
            elif array[n][r] == 0:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="white", fill="white", tags="wall")

            positionX +=30
        positionX = 200
        positionY += 30
def goRight(event):
    global array,levelArray,levelnumber
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\rockHit2.wav",
    winsound.SND_FILENAME)

    positionX = 200
    positionY = 30
    spacecraft = []
    for num1 in range(len(array)):
        for num2 in range(len(array[num1])):
            if array[num1][num2] == 2:
                spacecraft.append(num2)
                spacecraft.append(num1)
    if array[spacecraft[1]][spacecraft[0]+1] == 0:
        array[spacecraft[1]][spacecraft[0]+1] = 2
        array[spacecraft[1]][spacecraft[0]] = 0
    for n in range(len(array)):
        for r in range(len(array[n])):
            if array[n][r] == 1:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="darkblue", fill="darkblue", tags="wall")
            elif array[n][r] == 2:
                canvas1.create_image( positionX-5, positionY+5, image = spacecrafter2, anchor = "nw", tags="craft")
            elif array[n][r] == 3:
                canvas1.create_image( positionX, positionY, image = Earth, anchor = "nw", tags="craft")
            elif array[n][r] == 5:
                canvas1.create_image( positionX, positionY, image = Animy2, anchor = "nw", tags="animy")
            elif array[n][r] == 6:
                canvas1.create_image( positionX, positionY, image = Animy1, anchor = "nw", tags="animy")
            elif array[n][r] == 0:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="white", fill="white", tags="wall")

            positionX +=30
        positionX = 200
        positionY += 30
def goLeft(event):
    global array,levelArray,levelnumber
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\rockHit2.wav",
    winsound.SND_FILENAME)

    positionX = 200
    positionY = 30
    spacecraft = []
    for num1 in range(len(array)):
        for num2 in range(len(array[num1])):
            if array[num1][num2] == 2:
                spacecraft.append(num2)
                spacecraft.append(num1)
    if array[spacecraft[1]][spacecraft[0]-1] == 0:
        array[spacecraft[1]][spacecraft[0]-1] = 2
        array[spacecraft[1]][spacecraft[0]] = 0
    for n in range(len(array)):
        for r in range(len(array[n])):
            if array[n][r] == 1:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="darkblue", fill="darkblue", tags="wall")
            elif array[n][r] == 2:
                canvas1.create_image( positionX, positionY+5, image = spacecrafter4, anchor = "nw", tags="craft")
            elif array[n][r] == 3:
                canvas1.create_image( positionX, positionY, image = Earth, anchor = "nw", tags="craft")
            elif array[n][r] == 5:
                canvas1.create_image( positionX, positionY, image = Animy2, anchor = "nw", tags="animy")
            elif array[n][r] == 6:
                canvas1.create_image( positionX, positionY, image = Animy1, anchor = "nw", tags="animy")
            elif array[n][r] == 0:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="white", fill="white", tags="wall")

            positionX +=30
        positionX = 200
        positionY += 30
def Exit(event):
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)

    canvas1.delete("bggraphic")
    canvas1.delete("wall")
    canvas1.delete("exit")
    canvas1.delete("heart1")
    canvas1.delete("heart2")
    canvas1.delete("heart3")
    canvas1.delete("craft")
    canvas1.delete("animy")
    # startNew()

def find(event):
    global levelArray,levelnumber,bg,array
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)

    canvas1.create_image( 0, 0, image = bggraphic, anchor = "nw", tags="bggraphic") 
    canvas1.create_image( 800, 10, image = heart, anchor = "nw", tags="heart1")
    canvas1.create_image( 850, 10, image = heart, anchor = "nw", tags="heart2")
    canvas1.create_image( 900, 10, image = heart, anchor = "nw", tags="heart3")

    level = 1
    for index in range(len(levelArray)):
        if (levelArray[index][0] <= event.x and levelArray[index][2] >= event.x) and (levelArray[index][1] <= event.y and levelArray[index][3] >= event.y):
            level = index+1
            print(level)
        # print(levelArray[index])
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
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="darkblue", fill="darkblue", tags="wall")
            elif array[n][r] == 2:
                canvas1.create_image( positionX+5, positionY, image = spacecrafter1, anchor = "nw", tags="craft")
            elif array[n][r] == 3:
                canvas1.create_image( positionX, positionY, image = Earth, anchor = "nw", tags="craft")
            elif array[n][r] == 5:
                canvas1.create_image( positionX, positionY, image = Animy2, anchor = "nw", tags="animy")
            elif array[n][r] == 6:
                canvas1.create_image( positionX, positionY, image = Animy1, anchor = "nw", tags="animy")
            elif array[n][r] == 0:
                canvas1.create_rectangle(positionX, positionY, positionX+30, positionY+30, outline="white", fill="white", tags="wall")

            positionX +=30
        positionX = 200
        positionY += 30
    canvas1.create_rectangle(0, 0, 70, 40, outline="black", fill="orange", tags="exit")
    canvas1.create_text(35, 20, text = "Exit", fill="black", font="Times 14 italic bold", tags="exit")

def back(event):
    global bg,startbg
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)
    canvas1.delete("back")
    canvas1.delete("level")
    # canvas1.delete("number")
    canvas1.delete("image")
    startbg()


def remove(event):
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)
    canvas1.delete("remove")
    canvas1.delete("delete")
    canvas1.delete("soundon")
    canvas1.delete("soundoff")
    canvas1.delete("musicon")
    canvas1.delete("musicdoff")
    canvas1.move("welcome", 0, 100)

# Display levels................................................................................................................
def startNew(event):
    global bg,X,Y
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)
    X = 180
    Y = 100
    number = 1
    canvas1.create_image( 0, 0, image = bglevel, anchor = "nw", tags="image")
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

# Setting display............................................................................................................
def settingNew(event):
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 125, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas1.create_image( 330, 160, image = soundOn, anchor = "nw", tags="soundon")
    canvas1.create_text(500, 210, text = "Sound On", fill="black", font="Times 18 italic bold", tags="soundon")

    canvas1.create_image( 330, 270, image = soundOn, anchor = "nw", tags="musicon")
    canvas1.create_text(500, 330, text = "Music On", fill="black", font="Times 18 italic bold", tags="musicon")

# Identify Sound ............................................................................................................
def ClickMusicOff(event):
    canvas1.delete("musicoff")
    canvas1.create_image( 330, 270, image = soundOn, anchor = "nw", tags="musicon")
    canvas1.create_text(500, 330, text = "Music On", fill="black", font="Times 18 italic bold", tags="musicon")

def ClickSoundOff(event):
    canvas1.delete("soundoff")
    canvas1.create_image( 330, 160, image = soundOn, anchor = "nw", tags="soundon")
    canvas1.create_text(500, 210, text = "Sound On", fill="black", font="Times 18 italic bold", tags="soundon")

def ClickSoundOn(event):
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)
    canvas1.delete("soundon")
    canvas1.create_image( 330, 160, image = soundOff, anchor = "nw", tags="soundoff")
    canvas1.create_text(500, 210, text = "Sound Off", fill="black", font="Times 18 italic bold", tags="soundoff")
def ClickMusicOn(event):
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)
    canvas1.delete("musicon")
    canvas1.create_image( 330, 270, image = soundOff, anchor = "nw", tags="musicoff")
    canvas1.create_text(500, 330, text = "Music Off", fill="black", font="Times 18 italic bold", tags="musicoff")

# Quit diplay................................................................................................................
def quitNew(event):
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
    winsound.SND_FILENAME)
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 115, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas1.create_text(350, 130, anchor=W, font="Purisa",text="Most relationships seem so transitory")


def startbg():
    global bg

    canvas1.create_image( 0, 0, image = space, anchor = "nw") 

    # Add Text 
    canvas1.create_text(500, 150, text = "Welcome to the maze game!!!", fill="#0D4D8D", font="Times 35 italic bold", tags="welcome")
    
    #Start
    canvas1.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
    canvas1.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")

    # Setting
    canvas1.create_rectangle(430, 320, 610, 380, fill="white", tags="setting")
    canvas1.create_text(515,350, text = "Setting", fill="black", font="Times 35 italic bold", tags="setting")

    # Quit
    canvas1.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
    canvas1.create_text(515, 450, text = "Quit", fill="black", font="Times 35 italic bold", tags="quit")


def begin():
    canvas1.create_text(500, 550, text = "Loading...", fill="white", font="Times 20 italic bold", tags="welcome")
    canvas1.after(2000, startbg)

# ClickOn.....................................................................................................................
canvas1.tag_bind("start", "<Button-1>", startNew)
canvas1.tag_bind("setting", "<Button-1>", settingNew)
canvas1.tag_bind("quit", "<Button-1>", quitNew)
canvas1.tag_bind("remove", "<Button-1>", remove)

canvas1.tag_bind("back", "<Button-1>", back)
canvas1.tag_bind("level", "<Button-1>", find)
canvas1.tag_bind("exit", "<Button-1>", Exit)

root.bind("<Up>", goUp)
root.bind("<Down>", goDown)
root.bind("<Right>", goRight)
root.bind("<Left>", goLeft)

canvas1.tag_bind("soundon", "<Button-1>", ClickSoundOn)
canvas1.tag_bind("musicon", "<Button-1>", ClickMusicOn)
canvas1.tag_bind("soundoff", "<Button-1>", ClickSoundOff)
canvas1.tag_bind("musicoff", "<Button-1>", ClickMusicOff)

# Image........................................................................................................................

bg = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\start.gif") 
canvas1.create_image( 0, 0, image = bg, anchor = "nw", tags="bg1")

space = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\Cartoon_spaceship_dn.png") 
bglevel = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\level.png") 
spacecrafter1 = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\images1.png")
spacecrafter2 = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\images2.png") 
spacecrafter3 = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\images3.png") 
spacecrafter4 = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\images4.png") 
Earth = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\Earth.png") 
bggraphic = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\wp2863950.gif") 
heart = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\hearts.png") 
soundOn = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\soundOn.png") 
soundOff = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\soundOff.png") 
Animy2 = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\animy2.png") 
Animy1 = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\animy1.png") 


begin()

# winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav",
# winsound.SND_FILENAME)
# Execute tkinter 
root.mainloop()