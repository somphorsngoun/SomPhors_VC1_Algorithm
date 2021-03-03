# Import module  
from tkinter import *
import tkinter
from winsound import *
import winsound
from tkinter import messagebox

# from glob import glob



# Create object  
root = Tk() 
root.title("Create by @SomPhors")
# Adjust size  
root.geometry("1000x600") 
root.resizable(0,0)

# Create Canvas 
canvas1 = Canvas( root, width = 800, height = 600) 
canvas1.pack(fill = "both", expand = True) 


# Variable................................................................................................
levelArray = []
levelnumber = []
array = []
clicksound = True
heartnumber = 0
Right = False
Left = False
Down = False
Up = False
point = 0
win = False
Lose = False
# Function ....................................................................................................................

# Display sound................................................................................................................
def displaysound():
    global clicksound
    if clicksound:
        winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\click.wav", winsound.SND_FILENAME)

# Drawing.......................................................................................................................
def drawgraphic():
    global array,point
    positionX = 200
    positionY = 30
    for n in range(len(array)):
        for r in range(len(array[n])):

            if array[n][r] == 1:
                canvas1.create_image( positionX, positionY, image = wall, anchor = "nw", tags="wall")
            elif array[n][r] == 2:
                canvas1.create_image( positionX, positionY, image = spacecrafter1, anchor = "nw", tags="craft")
            elif array[n][r] == 3:
                canvas1.create_image( positionX, positionY, image = Earth, anchor = "nw", tags="craft")
            elif array[n][r] == 5 or array[n][r] == 6:
                canvas1.create_image( positionX, positionY, image = Animy, anchor = "nw", tags="animy")
            elif array[n][r] == 0:
                canvas1.create_image( positionX, positionY, image = coin3, anchor = "nw", tags="gold")

            elif array[n][r] == 4:
                canvas1.create_rectangle( positionX, positionY, positionX+30, positionY+30, outline="white", fill="white", tags="craft")
            positionX +=30
        positionX = 200
        positionY += 30
    canvas1.create_text(840, 80, text = "Point: "+str(point), fill="white", font="DotGothic16 14 italic bold", tags="point")
    if win:
        winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\coin2.wav", winsound.SND_FILENAME)
        messagebox.showinfo(message="You Win")

    elif Lose:
        winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\gameover5.wav", winsound.SND_FILENAME)
        canvas1.create_image( 300, 200, image = over, anchor = "nw", tags="over")
        messagebox.showinfo(message="Game over")

# Delete heart.................................................................................................................
def lift():
    global heartnumber, Lose
    winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\lose4.wav",
    winsound.SND_FILENAME)
    heartnumber += 1
    print(heartnumber)
    if heartnumber == 1:
        canvas1.delete("heart1")
    elif heartnumber == 2:
        canvas1.delete("heart2")
    elif heartnumber == 3:
        canvas1.delete("heart3")
    elif heartnumber == 4:
        Lose = True

# Check spacecraft.............................................................................................................
def findSpacecraft():
    global array, Down, Left, Right, Up, point, win
    
    spacecraft = []
    for num1 in range(len(array)):
        for num2 in range(len(array[num1])):
            if array[num1][num2] == 2:
                spacecraft.append(num2)
                spacecraft.append(num1)
    if Up:
        if array[spacecraft[1]-1][spacecraft[0]] == 0 or array[spacecraft[1]-1][spacecraft[0]] == 4:
            winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\coin2.wav", winsound.SND_FILENAME)
            point += 5
            array[spacecraft[1]-1][spacecraft[0]] = 2
            array[spacecraft[1]][spacecraft[0]] = 7
        elif array[spacecraft[1]-1][spacecraft[0]] == 5 or array[spacecraft[1]-1][spacecraft[0]] == 6:
            lift()
        elif array[spacecraft[1]-1][spacecraft[0]] == 3:
            win = True


        Up = False
    elif Down:
        if array[spacecraft[1]+1][spacecraft[0]] == 0 or array[spacecraft[1]+1][spacecraft[0]] == 4:
            winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\coin2.wav", winsound.SND_FILENAME)
            point += 5
            array[spacecraft[1]+1][spacecraft[0]] = 2
            array[spacecraft[1]][spacecraft[0]] = 7
        elif array[spacecraft[1]+1][spacecraft[0]] == 5 or array[spacecraft[1]+1][spacecraft[0]] == 6:
            lift()
        elif array[spacecraft[1]+1][spacecraft[0]] == 3:
            win = True

        Down = False
    elif Right:
        if array[spacecraft[1]][spacecraft[0]+1] == 0 or  array[spacecraft[1]][spacecraft[0]+1] == 4:
            winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\coin2.wav", winsound.SND_FILENAME)
            point += 5
            array[spacecraft[1]][spacecraft[0]+1] = 2
            array[spacecraft[1]][spacecraft[0]] = 7
        elif array[spacecraft[1]][spacecraft[0]+1] == 5 or array[spacecraft[1]][spacecraft[0]+1] == 6:
            lift()
        elif array[spacecraft[1]][spacecraft[0]+1] == 3:
            win = True
        Right = False
    elif Left:
        if array[spacecraft[1]][spacecraft[0]-1] == 0 or array[spacecraft[1]][spacecraft[0]-1] == 0:
            winsound .PlaySound("E:\\SomPhors_VC1_Algorithm\\Sounds\\coin2.wav", winsound.SND_FILENAME)
            point += 5
            array[spacecraft[1]][spacecraft[0]-1] = 2
            array[spacecraft[1]][spacecraft[0]] = 7
        elif array[spacecraft[1]][spacecraft[0]-1] == 5 or array[spacecraft[1]][spacecraft[0]-1] == 6:
            lift()
        elif array[spacecraft[1]][spacecraft[0]-1] == 3:
            win =True
        Left = False
    canvas1.delete("craft")
    canvas1.delete("animy")
    canvas1.delete("gold")
    canvas1.delete("point")
    drawgraphic()

# Go Up.......................................................................................................................
def goUp(event):
    global Up
    Up = True
    findSpacecraft()

# Go Down......................................................................................................................
def goDown(event):
    global Down
    Down = True
    findSpacecraft()

# Go Right.....................................................................................................................
def goRight(event):
    global Right
    Right = True
    findSpacecraft()

# Go Left......................................................................................................................
def goLeft(event):
    global Left
    Left =True
    findSpacecraft()

# Exit from game................................................................................................................
def Exit(event):
    displaysound()
    canvas1.delete("bggraphic")
    canvas1.delete("wall")
    canvas1.delete("exit")
    canvas1.delete("heart1")
    canvas1.delete("heart2")
    canvas1.delete("heart3")
    canvas1.delete("craft")
    canvas1.delete("animy")
    canvas1.delete("gold")
    # canvas1.delete("display")
    canvas1.delete("over")


# Choose level..................................................................................................................
def find(event):
    global levelArray,levelnumber,bg,array,point
    displaysound()

    canvas1.create_image( 0, 0, image = bggraphic, anchor = "nw", tags="bggraphic") 
    canvas1.create_image( 800, 10, image = heart, anchor = "nw", tags="heart1")
    canvas1.create_image( 850, 10, image = heart, anchor = "nw", tags="heart2")
    canvas1.create_image( 900, 10, image = heart, anchor = "nw", tags="heart3")

    level = 1
    for index in range(len(levelArray)):
        if (levelArray[index][0] <= event.x and levelArray[index][2] >= event.x) and (levelArray[index][1] <= event.y and levelArray[index][3] >= event.y):
            level = index+1
 
    file = open("E:\\SomPhors_VC1_Algorithm\\files\\"+str(level)+".txt", "r")
    array = file.read()
    array = array.split(';')
    for i in range(len(array)):
        array[i] = array[i].strip('\n')
        array[i] = array[i].split(',')
        for j in range(len(array[i])):
            array[i][j] = int(array[i][j])
    # print(array)
    file.close()
    
    canvas1.create_rectangle(0, 0, 70, 40, outline="black", fill="#2C6CAC", tags="exit")
    canvas1.create_text(35, 20, text = "Exit", fill="white", font="Times 14 italic bold", tags="exit")

    drawgraphic()

def back(event):
    global bg,startbg
    displaysound()
    canvas1.delete("back")
    canvas1.delete("level")
    canvas1.delete("image")
    startbg()

# Delete Setting................................................................................................................
def remove(event):
    displaysound()
    canvas1.delete("remove")
    canvas1.delete("delete")
    canvas1.delete("soundon")
    canvas1.delete("soundoff")
    canvas1.delete("musicon")
    canvas1.delete("musicoff")
    canvas1.delete("senario")
    canvas1.move("welcome", 0, 100)

# Display levels................................................................................................................
def startNew(event):
    global bg,X,Y,levelArray
    displaysound()
    X = 180
    Y = 100
    number = 1
    levelArray = []
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
    displaysound()
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 125, text = "X", fill="black", font="Oswald 25 italic bold", tags="remove")
    if clicksound:
        canvas1.create_image( 330, 160, image = soundOn, anchor = "nw", tags="soundon")
        canvas1.create_text(500, 210, text = "Sound On", fill="black", font="Times 18 bold", tags="soundon")
    else:
        canvas1.create_image( 330, 160, image = soundOff, anchor = "nw", tags="soundoff")
        canvas1.create_text(500, 210, text = "Sound Off", fill="black", font="Times 18 bold", tags="soundoff")
    canvas1.create_image( 330, 270, image = soundOn, anchor = "nw", tags="musicon")
    canvas1.create_text(500, 330, text = "Music On", fill="black", font="Times 18 bold", tags="musicon")

    

# Identify Sound ............................................................................................................
def ClickMusicOff(event):
    displaysound()
    canvas1.delete("musicoff")
    canvas1.create_image( 330, 270, image = soundOn, anchor = "nw", tags="musicon")
    canvas1.create_text(500, 330, text = "Music On", fill="black", font="Times 18 bold", tags="musicon")

def ClickSoundOff(event):
    global clicksound
    clicksound = True
    canvas1.delete("soundoff")
    canvas1.create_image( 330, 160, image = soundOn, anchor = "nw", tags="soundon")
    canvas1.create_text(500, 210, text = "Sound On", fill="black", font="Times 18 bold", tags="soundon")

def ClickSoundOn(event):
    global clicksound
    displaysound()
    clicksound = False
    canvas1.delete("soundon")
    canvas1.create_image( 330, 160, image = soundOff, anchor = "nw", tags="soundoff")
    canvas1.create_text(500, 210, text = "Sound Off", fill="black", font="Times 18 bold", tags="soundoff")
def ClickMusicOn(event):
    displaysound()
    canvas1.delete("musicon")
    canvas1.create_image( 330, 270, image = soundOff, anchor = "nw", tags="musicoff")
    canvas1.create_text(500, 330, text = "Music Off", fill="black", font="Times 18 bold", tags="musicoff")

# Quit diplay................................................................................................................
def quitNew(event):
    displaysound()
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 115, text = "X", fill="black", font="Oswald 25 italic bold", tags="remove")
    canvas1.create_text(350, 190, anchor=W, font="Purisa",text="- Step1: Click start to choose levels.", tags="senario")
    canvas1.create_text(350, 220, anchor=W, font="Purisa",text="- Step2: Spacecraft find the way go to Earth.", tags="senario")
    canvas1.create_text(410, 250, anchor=W, font="Purisa",text="But have some animy on the way.", tags="senario")
    canvas1.create_text(350, 280, anchor=W, font="Purisa",text="- Step3: If spacecraft meet animy it will lose 1 lift.", tags="senario")
    canvas1.create_text(410, 310, anchor=W, font="Purisa",text="If spacecraft lose 3 lift Game over!", tags="senario")
    canvas1.create_text(410, 340, anchor=W, font="Purisa",text="If spacecraft arrive Earth it will Win", tags="senario")

#Start game.....................................................................................................................
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
    
    
# First of game...............................................................................................................
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

canvas1.tag_bind("next", "<Button-1>", Exit)
canvas1.tag_bind("exitlose", "<Button-1>", Exit)

canvas1.tag_bind("soundon", "<Button-1>", ClickSoundOn)
canvas1.tag_bind("musicon", "<Button-1>", ClickMusicOn)
canvas1.tag_bind("soundoff", "<Button-1>", ClickSoundOff)
canvas1.tag_bind("musicoff", "<Button-1>", ClickMusicOff)
canvas1.tag_bind("over", "<Button-1>", Exit)

# Image........................................................................................................................

bg = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\start.gif") 
canvas1.create_image( 0, 0, image = bg, anchor = "nw", tags="bg1")

space = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\Cartoon_spaceship_dn.png") 
bglevel = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\level.png") 
spacecrafter1 = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\playerShip2_orange.png") 
Earth = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\Earth.png") 
bggraphic = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\spaces.gif") 
heart = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\hearts.png") 
soundOn = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\soundOn.png") 
soundOff = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\soundOff.png") 
Animy = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\robot_walk1.png") 

coin3 = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\gold_3.png") 

wall = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\stoneCenter.png") 
over = PhotoImage(file = "E:\\SomPhors_VC1_Algorithm\\images\\over.gif") 




begin()


# Execute tkinter 
root.mainloop()