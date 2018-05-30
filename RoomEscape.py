__author__ = 'Lily Du'

from tkinter import *
import random

def init(data):
    data.regretPill = 0
    data.bag = ["tape1", "Regret Pill * " + str(data.regretPill)]
    data.room = []
    data.curRoom = "livingRoom"
    data.text = []
    data.textLine = 0

    data.livingRoomChosen = "white"

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def startInfo(data):
    if(data.textLine == 0):
        data.text.insert(0, "Hi.")
        data.textLine += 1
    elif(data.textLine == 1):
        data.text.insert(0, "Unfortunately, you are trapped in a \n"+
                            "haunted crooked house.")
        data.textLine += 1
    elif(data.textLine == 2):
        data.text.insert(0, "You and your friend Owen were trying \n"+
                            "to find out a dark secret in the house")
        data.textLine += 1
    elif(data.textLine == 3):
        data.text.insert(0, "when someone attacked you from \n"+
                            "behind and you fainted.")
        data.textLine += 1
    elif(data.textLine == 4):
        data.text.insert(0, "You need to leave the house ASAP \n"+
                            "before something happen to you.")
        data.textLine += 1
    elif(data.textLine == 5):
        data.text.insert(0, "Now, try to escape the house safely.")
        data.textLine += 1
    elif(data.textLine == 6):
        data.text.insert(0, "You are now in the living room")
        data.textLine += 1

def timerFired(data):
    startInfo(data)
    if(data.curRoom == "livingRoom"):
        data.room = ["diningRoom", "bathRoom", "bedRoom", "balcony"]

def drawVoiceOver(canvas, data):
    for i in range(len(data.text)):
        canvas.create_text(10, data.height/20*(i+1), font="Arial 14", 
                           text=data.text[i], anchor="nw", 
                           fill="white")

def drawLivingRoom(canvas, data):
    canvas.create_text(data.width/2.5, data.height/20, font="Arial 14", 
                       text="Living Room", anchor="nw", 
                       fill=data.livingRoomChosen)

def drawDiningRoom(canvas, data):
    canvas.create_text(data.width/2.5, data.height/20, font="Arial 14", 
                       text="Dining Room", anchor="nw", 
                       fill=data.diningRoomChosen)

def drawBag(canvas, data):
    canvas.create_text(data.width/5*4, data.height/20, font="Arial 14", 
                       text="Bag", anchor="nw", 
                       fill="white")
    for i in range(len(data.bag)):
        canvas.create_text(data.width/5*4, data.height/20*(i+2), 
                           font="Arial 14", text=data.bag[i], anchor="nw", 
                           fill="white")

def redrawAll(canvas, data):
    drawVoiceOver(canvas, data)
    drawBag(canvas, data)
    if(data.curRoom == "livingRoom"):
        drawLivingRoom(canvas, data)
    elif(data.curRoom == "diningRoom"):
        drawDiningRoom(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height, fill="black")
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 2000 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)
