# eXOtended!
from tkinter import *
from threading import Thread
from tkinter.font import Font
import time

tk = Tk()
tk.geometry("666x866")
tk.title("eXOtended!")
tk.configure(background = "snow")

# Gameboard
full = Canvas(tk, width = 666, height = 866, highlightthickness = 0, bg = "DodgerBlue2")
full.grid(row = 0, column = 0)

infos = Canvas(tk, width = 666, height = 150, highlightthickness = 0, bg = "azure")
infos.grid(row = 1, column = 0)

playerDisplay = Canvas(tk, width = 666, height = 50, highlightthickness = 0, bg = "mint cream")
playerDisplay.grid(row = 2, column = 0)

border = Canvas(tk, width = 666, height = 50, highlightthickness = 0, bg = "snow")
border.grid(row = 3, column = 0)

game = Canvas(tk, width = 566, height = 566, highlightthickness = 0, bg = "white")
game.grid(row = 4, column = 0)

# Values for Grid (0 = nothing, 1 = player 1, 2 = player 2)
global A, B, C, D, E, F, G, H, I, grid
A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

##A = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
##B = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
##C = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
##D = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
##E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
##F = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
##G = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
##H = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
##I = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
grid = [[A, B, C], [D, E, F], [G, H, I]]

global pointX1, pointY1, pointX2, pointY2, mouse1Canvas, mouse2Canvas, playerTurn, smallX1, smallY1, smallX2, smallY2, bigX1, bigY1, bigX2, bigY2, bigGrid1, bigGrid2, validGrids, validBigGridLetter
global player1Lines, player2Lines, winningPlayer, freePlace, ended, stage, colorTemp, possibleColors, okay1, okay2, index1, index2, player1MouseColor, player2MouseColor, doneMouse, doneGrid
global doneWelcome1, doneBeginGame, clicked1, clicked2, doneWelcome2, messageNo, justClicked, askedTutorial
defaultColor = "snow"
player1GridColor = "turquoise"
player2GridColor = "magenta"

player1MouseColor = "red"
player2MouseColor = "orange"

pointX1 = 25
pointY1 = 20
pointX2 = 25
pointY2 = 20

mouse1Canvas = "full"
mouse2Canvas = "full"

playerTurn = "Player 1"

smallX1 = 3
smallY1 = 3
smallX2 = 3
smallY2 = 3

bigX1 = 3
bigY1 = 3
bigX2 = 3
bigY2 = 3

bigGrid1 = A
bigGrid2 = A

validGrids = [[], [], [], [], [], [], [], [], []]
validBigGridLetter = ""

gridLetters = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

player1Lines = 0
player2Lines = 0

winningPlayer = "Tie"

freePlace = False

stage = "Welcomes"

ended = False

doneMouse = False
doneGrid = False
doneBeginGame = False
doneWelcome1 = False
doneWelcome2 = False
clicked1 = False
clicked2 = False
justClicked = False
askedTutorial = False

colorTemp1 = "red"
colorTemp2 = "red"

yellow = "yellow"
paleGreen = "pale green"
khaki = "khaki"

ratio = 1

if (ratio == 1 or ratio == 60/94):
    yellow = "yellow"
##elif (ratio == 60/94):
##    yellow = "yellow3"

if (ratio == 1 or ratio == 60/94):
    paleGreen = "pale green"
##elif (ratio == 60/94):
##    paleGreen = "azure"

if (ratio == 1 or ratio == 60/94):
    khaki = "khaki"
##elif (ratio == 60/94):
##    khaki = "lemon chiffon"

if (ratio == 60/94):
    gentiumBookClassic = "gentuim book clasic"
elif (ratio == 1):
    gentiumBookClassic = "kai"
    
possibleColors = ["red", "orange", yellow, "green2", "turquoise", "magenta", "purple", "RosyBrown4", "gray64"]

okay1 = "OK?"
okay2 = "OK?"

index1 = 0
index2 = 0

messageNo = -1

def font(x):
    return str(int(x * ratio))

def exitFull():
    full.grid_forget()
    infos.grid()
    playerDisplay.grid()
    border.grid()
    game.grid()

def createFull():
    full.grid()
    infos.grid_forget()
    playerDisplay.grid_forget()
    border.grid_forget()
    game.grid_forget()

def pause(seconds):
    tk.update_idletasks()
    tk.update()
    time.sleep(seconds)

def drawgrid():
    game.delete("all")
    
    # Small Lines
    game.create_rectangle(60, 0, 61, 566, fill = "gray", outline = "")
    game.create_rectangle(121, 0, 122, 566, fill = "gray", outline = "")
    
    game.create_rectangle(252, 0, 253, 566, fill = "gray", outline = "")
    game.create_rectangle(313, 0, 314, 566, fill = "gray", outline = "")

    game.create_rectangle(444, 0, 445, 566, fill = "gray", outline = "")
    game.create_rectangle(505, 0, 506, 566, fill = "gray", outline = "")

    game.create_rectangle(0, 60, 566, 61, fill = "gray", outline = "")
    game.create_rectangle(0, 121, 566, 122, fill = "gray", outline = "")

    game.create_rectangle(0, 252, 566, 253, fill = "gray", outline = "")
    game.create_rectangle(0, 313, 566, 314, fill = "gray", outline = "")

    game.create_rectangle(0, 444, 566, 445, fill = "gray", outline = "")
    game.create_rectangle(0, 505, 566, 506, fill = "gray", outline = "")
    
    # Big Lines
    game.create_rectangle(182, 0, 192, 566, fill = "blue", outline = "")
    game.create_rectangle(374, 0, 384, 566, fill = "blue", outline = "")
    game.create_rectangle(0, 182, 566, 192, fill = "blue", outline = "")
    game.create_rectangle(0, 374, 566, 384, fill = "blue", outline = "")

    for j in range (0, 3):
        for i in range (0, 3):
            for y in range (0, 3):
                for x in range (0, 3):
                    if (grid[j][i][y][x] == 0):
                        game.create_rectangle(x * 61 + i * 192, y * 61 + j * 192, x * 61 + 60 + i * 192, y * 61 + 60 + j * 192, fill = defaultColor, outline = "")
                    if (grid[j][i][y][x] == 1):
                        game.create_rectangle(x * 61 + i * 192, y * 61 + j * 192, x * 61 + 60 + i * 192, y * 61 + 60 + j * 192, fill = player1GridColor, outline = "")
                    if (grid[j][i][y][x] == 2):
                        game.create_rectangle(x * 61 + i * 192, y * 61 + j * 192, x * 61 + 60 + i * 192, y * 61 + 60 + j * 192, fill = player2GridColor, outline = "")

    checkFullBoard()
    if (ended == True):
        winDraw()

def drawMouse1():
    global mouse1Canvas, pointX1, pointY1
    if (mouse1Canvas == "game"):
        game.create_rectangle(pointX1 - 5, pointY1 + 15, pointX1 + 25, pointY1 + 35, fill = player1MouseColor, outline = "")
        game.create_rectangle(pointX1, pointY1, pointX1 + 10, pointY1 + 15, fill = player1MouseColor, outline = "")

    if (mouse1Canvas == "infos"):
        infos.create_rectangle(pointX1 - 5, pointY1 + 15, pointX1 + 25, pointY1 + 35, fill = player1MouseColor, outline = "")
        infos.create_rectangle(pointX1, pointY1, pointX1 + 10, pointY1 + 15, fill = player1MouseColor, outline = "")

    if (mouse1Canvas == "full"):
        full.create_rectangle(pointX1 - 5, pointY1 + 15, pointX1 + 25, pointY1 + 35, fill = player1MouseColor, outline = "")
        full.create_rectangle(pointX1, pointY1, pointX1 + 10, pointY1 + 15, fill = player1MouseColor, outline = "")

def drawMouse2():
    global mouse2Canvas, pointX2, pointY2
    if (mouse2Canvas == "game"):
        game.create_rectangle(pointX2 - 5, pointY2 + 15, pointX2 + 25, pointY2 + 35, fill = player2MouseColor, outline = "")
        game.create_rectangle(pointX2, pointY2, pointX2 + 10, pointY2 + 15, fill = player2MouseColor, outline = "")

    if (mouse2Canvas == "infos"):
        infos.create_rectangle(pointX2 - 5, pointY2 + 15, pointX2 + 25, pointY2 + 35, fill = player2MouseColor, outline = "")
        infos.create_rectangle(pointX2, pointY2, pointX2 + 10, pointY2 + 15, fill = player2MouseColor, outline = "")

    if (mouse2Canvas == "full"):
        full.create_rectangle(pointX2 - 5, pointY2 + 15, pointX2 + 25, pointY2 + 35, fill = player2MouseColor, outline = "")
        full.create_rectangle(pointX2, pointY2, pointX2 + 10, pointY2 + 15, fill = player2MouseColor, outline = "")

def displayPlayerTurn():
    if (playerTurn == "Player 1"):
        playerDisplay.create_text(310, 25, fill = player1GridColor, font = "arial " + font(25) + " bold", text = playerTurn)
        playerDisplay.create_rectangle(370, 20, 400, 40, fill = player1MouseColor, outline = "")
        playerDisplay.create_rectangle(375, 5, 385, 20, fill = player1MouseColor, outline = "")

    if (playerTurn == "Player 2"):
        playerDisplay.create_text(310, 25, fill = player2GridColor, font = "arial " + font(25) + " bold", text = playerTurn)
        playerDisplay.create_rectangle(370, 20, 400, 40, fill = player2MouseColor, outline = "")
        playerDisplay.create_rectangle(375, 5, 385, 20, fill = player2MouseColor, outline = "")

def resetInfos():
    global winningPlayer
    infos.delete("all")
    infos.create_rectangle(0, 0, 666, 150, fill = "azure", outline = "")
    if ((playerTurn == "Player 1" and mouse1Canvas == "game" and ended == False) or (playerTurn == "Player 2" and mouse2Canvas == "game" and ended == False)):
        infos.create_rectangle(20, 30, 50, 50, fill = player1MouseColor, outline = "")
        infos.create_rectangle(25, 15, 35, 30, fill = player1MouseColor, outline = "")
        infos.create_text(170, 33, fill = player1GridColor, font = "arial " + font(25) + " bold", text = "Player 1 (WASD): ")
        infos.create_text(295, 33, fill = darkerColor(player1GridColor), font = "arial " + font(25) + " bold", text = str(player1Lines))

        infos.create_rectangle(20, 100, 50, 120, fill = player2MouseColor, outline = "")
        infos.create_rectangle(25, 85, 35, 100, fill = player2MouseColor, outline = "")
        infos.create_text(170, 103, fill = player2GridColor, font = "arial " + font(25) + " bold", text = "Player 2 (Arrow): ")
        infos.create_text(295, 103, fill = darkerColor(player2GridColor), font = "arial " + font(25) + " bold", text = str(player2Lines))
    elif ((mouse2Canvas == "infos" and ended == True) and (mouse1Canvas == "infos" and ended == True)):
        infos.create_rectangle(20, 30, 50, 50, fill = "black", outline = "")
        infos.create_rectangle(25, 15, 35, 30, fill = "black", outline = "")
        infos.create_text(170, 33, fill = "black", font = "arial " + font(25) + " bold", text = "Player 1 (WASD): ")
        infos.create_text(295, 33, fill = "black", font = "arial " + font(25) + " bold", text = str(player1Lines))

        infos.create_rectangle(20, 100, 50, 120, fill = "black", outline = "")
        infos.create_rectangle(25, 85, 35, 100, fill = "black", outline = "")
        infos.create_text(170, 103, fill = "black", font = "arial " + font(25) + " bold", text = "Player 2 (Arrow): ")
        infos.create_text(295, 103, fill = "black", font = "arial " + font(25) + " bold", text = str(player2Lines))
    elif (playerTurn == "Player 1" and mouse1Canvas == "infos" and ended == False):
        infos.create_rectangle(20, 30, 50, 50, fill = "black", outline = "")
        infos.create_rectangle(25, 15, 35, 30, fill = "black", outline = "")
        infos.create_text(170, 33, fill = "black", font = "arial " + font(25) + " bold", text = "Player 1 (WASD): ")
        infos.create_text(295, 33, fill = "black", font = "arial " + font(25) + " bold", text = str(player1Lines))

        infos.create_rectangle(20, 100, 50, 120, fill = player2MouseColor, outline = "")
        infos.create_rectangle(25, 85, 35, 100, fill = player2MouseColor, outline = "")
        infos.create_text(170, 103, fill = player2GridColor, font = "arial " + font(25) + " bold", text = "Player 2 (Arrow): ")
        infos.create_text(295, 103, fill = darkerColor(player2GridColor), font = "arial " + font(25) + " bold", text = str(player2Lines))
    elif (mouse1Canvas == "infos" and ended == True):
        infos.create_rectangle(20, 30, 50, 50, fill = "black", outline = "")
        infos.create_rectangle(25, 15, 35, 30, fill = "black", outline = "")
        infos.create_text(170, 33, fill = "black", font = "arial " + font(25) + " bold", text = "Player 1 (WASD): ")
        infos.create_text(295, 33, fill = "black", font = "arial " + font(25) + " bold", text = str(player1Lines))

        infos.create_rectangle(20, 100, 50, 120, fill = player2MouseColor, outline = "")
        infos.create_rectangle(25, 85, 35, 100, fill = player2MouseColor, outline = "")
        infos.create_text(170, 103, fill = player2GridColor, font = "arial " + font(25) + " bold", text = "Player 2 (Arrow): ")
        infos.create_text(295, 103, fill = darkerColor(player2GridColor), font = "arial " + font(25) + " bold", text = str(player2Lines))
    elif (playerTurn == "Player 2" and mouse2Canvas == "infos" and ended == False):
        infos.create_rectangle(20, 30, 50, 50, fill = player1MouseColor, outline = "")
        infos.create_rectangle(25, 15, 35, 30, fill = player1MouseColor, outline = "")
        infos.create_text(170, 33, fill = player1GridColor, font = "arial " + font(25) + " bold", text = "Player 1 (WASD): ")
        infos.create_text(295, 33, fill = darkerColor(player1GridColor), font = "arial " + font(25) + " bold", text = str(player1Lines))

        infos.create_rectangle(20, 100, 50, 120, fill = "black", outline = "")
        infos.create_rectangle(25, 85, 35, 100, fill = "black", outline = "")
        infos.create_text(170, 103, fill = "black", font = "arial " + font(25) + " bold", text = "Player 2 (Arrow): ")
        infos.create_text(295, 103, fill = "black", font = "arial " + font(25) + " bold", text = str(player2Lines))
    elif (mouse2Canvas == "infos" and ended == True):
        infos.create_rectangle(20, 30, 50, 50, fill = player1MouseColor, outline = "")
        infos.create_rectangle(25, 15, 35, 30, fill = player1MouseColor, outline = "")
        infos.create_text(170, 33, fill = player1GridColor, font = "arial " + font(25) + " bold", text = "Player 1 (WASD): ")
        infos.create_text(295, 33, fill = darkerColor(player1GridColor), font = "arial " + font(25) + " bold", text = str(player1Lines))

        infos.create_rectangle(20, 100, 50, 120, fill = "black", outline = "")
        infos.create_rectangle(25, 85, 35, 100, fill = "black", outline = "")
        infos.create_text(170, 103, fill = "black", font = "arial " + font(25) + " bold", text = "Player 2 (Arrow): ")
        infos.create_text(295, 103, fill = "black", font = "arial " + font(25) + " bold", text = str(player2Lines))
    elif ((playerTurn == "Player 1" and mouse1Canvas == "game" and ended == True) or (playerTurn == "Player 2" and mouse2Canvas == "game" and ended == True)):
        infos.create_rectangle(20, 30, 50, 50, fill = player1MouseColor, outline = "")
        infos.create_rectangle(25, 15, 35, 30, fill = player1MouseColor, outline = "")
        infos.create_text(170, 33, fill = player1GridColor, font = "arial " + font(25) + " bold", text = "Player 1 (WASD): ")
        infos.create_text(295, 33, fill = darkerColor(player1GridColor), font = "arial " + font(25) + " bold", text = str(player1Lines))

        infos.create_rectangle(20, 100, 50, 120, fill = player2MouseColor, outline = "")
        infos.create_rectangle(25, 85, 35, 100, fill = player2MouseColor, outline = "")
        infos.create_text(170, 103, fill = player2GridColor, font = "arial " + font(25) + " bold", text = "Player 2 (Arrow): ")
        infos.create_text(295, 103, fill = darkerColor(player2GridColor), font = "arial " + font(25) + " bold", text = str(player2Lines))

    infos.create_rectangle(456, 10, 656, 60, fill = "pale turquoise", outline = "")
    infos.create_text(556, 35, fill = "cadet blue", font = "arial " + font(25) + " bold", text = "Play Again")

    whosWinning()
    if (ended == True):
        if (winningPlayer == "Player 1"):
            infos.create_text(556, 80, fill = "sky blue", font = "arial " + font(18) + " bold", text = "The game has ended!")
            infos.create_text(556, 105, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Player 1 won! Better")
            infos.create_text(556, 130, fill = "sky blue", font = "arial " + font(18) + " bold", text = "luck next time, player 2!")
        elif (winningPlayer == "Player 2"):
            infos.create_text(556, 80, fill = "sky blue", font = "arial " + font(18) + " bold", text = "The game has ended!")
            infos.create_text(556, 105, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Player 2 won! Better")
            infos.create_text(556, 130, fill = "sky blue", font = "arial " + font(18) + " bold", text = "luck next time, player 1!")
        elif (winningPlayer == "Tie"):
            infos.create_text(556, 80, fill = "sky blue", font = "arial " + font(18) + " bold", text = "The game has ended!")
            infos.create_text(556, 105, fill = "sky blue", font = "arial " + font(18) + " bold", text = "It's a tie! Keep up the")
            infos.create_text(556, 130, fill = "sky blue", font = "arial " + font(18) + " bold", text = "good work, both of you!")
    elif (winningPlayer == "Player 1"):
        infos.create_text(560, 80, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Player 1 is in the lead!")
        infos.create_text(560, 105, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Can they keep it up? ")
        infos.create_text(560, 130, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Player 2, you got this!")
    elif (winningPlayer == "Player 2"):
        infos.create_text(560, 80, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Player 2 is in the lead!")
        infos.create_text(560, 105, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Can they keep it up? ")
        infos.create_text(560, 130, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Player 1, you got this!")
    elif (winningPlayer == "Tie" and player1Lines == 0 and player2Lines == 0):
        infos.create_text(556, 80, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Hmm, no one has a line")
        infos.create_text(556, 105, fill = "sky blue", font = "arial " + font(18) + " bold", text = "yet. Who would win? I'm")
        infos.create_text(556, 130, fill = "sky blue", font = "arial " + font(18) + " bold", text = "rooting for both of you!")
    elif (winningPlayer == "Tie"):
        infos.create_text(556, 80, fill = "sky blue", font = "arial " + font(18) + " bold", text = "Hmm, it seems like it's a")
        infos.create_text(556, 105, fill = "sky blue", font = "arial " + font(18) + " bold", text = "tie. Who would win? I'm")
        infos.create_text(556, 130, fill = "sky blue", font = "arial " + font(18) + " bold", text = "rooting for both of you!")
        
    infos.create_rectangle(315, 10, 445, 60, fill = "pale turquoise", outline = "")
    infos.create_text(380, 35, fill = "cadet blue", font = "arial " + font(25) + " bold", text = "Customize")
    if (ratio == 60/94):
        infos.create_text(380, 105, fill = "slate blue", font = (gentiumBookClassic, int(font(31)), "bold"), text = "eXOtended!")
    elif (ratio == 1):
        infos.create_text(380, 105, fill = "slate blue", font = (gentiumBookClassic, int(font(27)), "bold"), text = "eXOtended!")
    #infos.create_text(380, 120, fill = "slate blue", font = "arial " + font(17) + " bold", text = "TIC TAC TOE!")

def winDraw():
    game.create_rectangle(30, 208, 536, 358, fill = "DodgerBlue2", outline = "")
    game.create_text(283, 283, fill = "light sky blue", font = "arial " + font(75) + " bold", text = "GAME OVER!")
    resetInfos()
    
def darkerColor(color):
    if (color == "red"):
        return "red4"
    elif (color == "orange"):
        return "chocolate3"
    elif (color == yellow):
        if (ratio == 1 or ratio == 60/94):
            return "goldenrod"
##        elif (ratio == 60/94):
##            return "khaki4"
    elif (color == "green2"):
        return "green4"
    elif (color == "turquoise"):
        return "turquoise4"
    elif (color == "magenta"):
        return "magenta4"
    elif (color == "purple"):
        return "purple4"
    elif (color == "RosyBrown4"):
        return "gray16"
    elif (color == "gray64"):
        return "gray33"

def lighterColor(color):
    if (color == "red"):
        return "pink"
    elif (color == "orange"):
        return "bisque"
    elif (color == yellow):
        if (ratio == 1 or ratio == 60/94):
            return "khaki3"
##        elif (ratio == 60/94):
##            return "lemon chiffon"
    elif (color == "green2"):
        return paleGreen
    elif (color == "turquoise"):
        return "pale turquoise"
    elif (color == "magenta"):
        return "light pink"
    elif (color == "purple"):
        return "thistle"
    elif (color == "RosyBrown4"):
        return "Peachpuff2"
    elif (color == "gray64"):
        return "gray83"

def resetPlayerDisplay():
    playerDisplay.delete("all")
    if (playerTurn == "Player 1"):
        playerDisplay.create_rectangle(0, 0, 666, 50, fill = lighterColor(player1GridColor), outline = "")
    elif (playerTurn == "Player 2"):
        playerDisplay.create_rectangle(0, 0, 666, 50, fill = lighterColor(player2GridColor), outline = "")
    displayPlayerTurn()

def animateText(textToAni, x, y, fontSize, fgColor, bgColor, continueX, continueY, wantContinue):
    global finishedAnimate, t1, t2
    canvas_text = full.create_text(x, y, font = "arial " + font(fontSize) + " bold", fill = fgColor, text= "")
    doneText = False
    delta = 30 
    delay = 0
    shortContinue= ""
    if (wantContinue == True):
        continueText = full.create_text(continueX, continueY, font = "arial " + font(14), fill = "black", text = "Press ENTER to continue")
        shortContinue = "Press ENTER to continue"
    else:
        continueText = full.create_text(continueX, continueY, font = "arial " + font(14), fill = "black", text = "")
        shortContinue = ""
    for i in range(len(textToAni) + 1):
        s = textToAni[:i]
        update_text = lambda s=s: full.itemconfigure(canvas_text, text=s)
        if (i == len(textToAni)):
            texty = shortContinue[0:i]
        else:
            texty = ""
        displayText = lambda texty=texty: full.itemconfigure(continueText, text=texty)
        full.after(delay, update_text)
        full.after(delay, displayText)
        delay += delta
    
def resetFull():
    global colorTemp1, colorTemp2, doneMouse, doneGrid, okay1, okay2, stage, index1, index2, doneWelcome1, messageNo, justClicked, doneWelcome2, askedTutorial
    full.delete("all")

    if (doneWelcome1 == False):
        full.create_rectangle(0, 0, 666, 866, fill = "light sky blue", outline = "")
        full.create_text(333, 120, fill = "slate blue", font = (gentiumBookClassic, int(font(130)), "normal"), text = "eXOtended!")
        #full.create_text(337, 220, fill = "slate blue", font = "arial " + font(94) + " bold", text = "TIC TAC TOE!")
        full.create_rectangle(153, 500, 513, 600, fill = "DodgerBlue1", outline = "")
        full.create_text(333, 550, fill = "azure", font = "arial " + font(40) + " bold", text = "START!")
        full.create_text(333, 615, fill = "azure", font = "arial " + font(18), text = "Press ENTER to start!")
    elif (askedTutorial == False):
        full.create_rectangle(0, 0, 666, 866, fill = "light sky blue", outline = "")
        full.create_text(333, 70, fill = "slate blue", font = (gentiumBookClassic, int(font(130)), "normal"), text = "eXOtended!")
        #full.create_text(337, 170, fill = "slate blue", font = "arial " + font(94) + " bold", text = "TIC TAC TOE!")
        full.create_text(337, 270, fill = "LightCyan1", font = "arial " + font(24) + " bold", text = "Would you want to go through the tutorial of this game?")
        full.create_rectangle(153, 380, 513, 480, fill = "DodgerBlue1", outline = "")
        full.create_text(333, 430, fill = "azure", font = "arial " + font(40) + " bold", text = "Continue Tutorial")
        full.create_text(333, 495, fill = "azure", font = "arial " + font(18), text = "Press ENTER to continue the tutorial.")
        full.create_rectangle(153, 600, 513, 700, fill = "DodgerBlue1", outline = "")
        full.create_text(333, 650, fill = "azure", font = "arial " + font(40) + " bold", text = "Skip Tutorial")
        full.create_text(333, 715, fill = "azure", font = "arial " + font(18), text = "Press SHIFT to skip the tutorial.")
    elif(doneWelcome2 == False):
        full.create_rectangle(0, 0, 666, 866, fill = "DodgerBlue2", outline = "")
        full.create_text(333, 70, fill = "slate blue", font = (gentiumBookClassic, int(font(130)), "normal"), text = "eXOtended!")
        #full.create_text(337, 170, fill = "slate blue", font = "arial " + font(94) + " bold", text = "TIC TAC TOE!")
        full.create_rectangle(0, 220, 666, 320, fill = "LightCyan1", outline = "")
        if (messageNo == -1 and justClicked == False):
            justClicked = True
            messageNo = 1
            animateText("Before starting to play the game, we should learn the rules of the game.", 333, 270, 19, "turquoise", "LightCyan1", 575, 305, True)
            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            full.create_rectangle(150, 500, 516, 600, fill = "deep sky blue", outline = "")
            full.create_text(333, 550, fill = "DodgerBlue1", font = "arial " + font(50) + " bold", text = "RULES TIME!")
        elif (messageNo == 1 and justClicked == False):
            justClicked = True
            messageNo = 2
            animateText("Just like any other game, player 1 and player 2, the computer for singleplayer, switch turns throughout.", 333, 270, 12, "turquoise", "LightCyan1", 575, 305, True)
            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            full.create_rectangle(150, 500, 516, 600, fill = "deep sky blue", outline = "")
            full.create_text(333, 550, fill = "DodgerBlue1", font = "arial " + font(50) + " bold", text = "RULES TIME!")
        elif (messageNo == 2 and justClicked == False):
            justClicked = True
            messageNo = 3
            animateText('In this game, "Player 1" is the first and "Player 2" is the second player.', 333, 270, 19, "turquoise", "LightCyan1", 575, 305, True)
            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            full.create_rectangle(150, 500, 516, 600, fill = "deep sky blue", outline = "")
            full.create_text(333, 550, fill = "DodgerBlue1", font = "arial " + font(50) + " bold", text = "RULES TIME!")
        elif (messageNo == 3 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 4
            animateText("Look below at the following grid. That's the grid you're going to play on.", 333, 270, 19, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 4 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 5
            animateText("These squares will be important to understanding how the game works.", 333, 270, 19, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
                    full.create_rectangle(offsetX + 97 * i + 2, offsetY + 97 * j + 2, offsetX + 97 * i + 92 - 2, offsetY + 97 * j + 92 - 2, fill = "", outline = "magenta", width = 2)
        elif (messageNo == 5 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 6
            animateText("To illustrate how the game works, imagine player 1 put their square here.", 333, 270, 19, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
                    
            full.create_rectangle(offsetX + 0 * 31 + 2 * 97, offsetY + 1 * 31 + 2 * 97, offsetX + 0 * 31 + 2 * 97 + 30, offsetY + 1 * 31 + 2 * 97 + 30, fill = "turquoise", outline = "")
            for j in range (0, 3):
                for i in range (0, 3):
                    full.create_rectangle(offsetX + 97 * i + 2, offsetY + 97 * j + 2, offsetX + 97 * i + 92 - 2, offsetY + 97 * j + 92 - 2, fill = "", outline = "magenta", width = 2)
        elif (messageNo == 6 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 7
            animateText("Within the bordered square, player 1 put their square on the left of the middle row.", 333, 270, 16, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
                    
            full.create_rectangle(offsetX + 0 * 31 + 2 * 97, offsetY + 1 * 31 + 2 * 97, offsetX + 0 * 31 + 2 * 97 + 30, offsetY + 1 * 31 + 2 * 97 + 30, fill = "turquoise", outline = "")
            for j in range (0, 3):
                for i in range (0, 3):
                    full.create_rectangle(offsetX + 97 * i + 2, offsetY + 97 * j + 2, offsetX + 97 * i + 92 - 2, offsetY + 97 * j + 92 - 2, fill = "", outline = "magenta", width = 2)
        elif (messageNo == 7 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 8
            animateText("So, player 2 must put their choice in the big square on the left of the middle row.", 333, 270, 17, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
                            if (i == 0 and j == 1):
                               full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = khaki, outline = "")
 
                    
            full.create_rectangle(offsetX + 0 * 31 + 2 * 97, offsetY + 1 * 31 + 2 * 97, offsetX + 0 * 31 + 2 * 97 + 30, offsetY + 1 * 31 + 2 * 97 + 30, fill = "turquoise", outline = "")
            for j in range (0, 3):
                for i in range (0, 3):
                    full.create_rectangle(offsetX + 97 * i + 2, offsetY + 97 * j + 2, offsetX + 97 * i + 92 - 2, offsetY + 97 * j + 92 - 2, fill = "", outline = "magenta", width = 2)

            full.create_text(350, 750, fill = "SpringGreen3", font = "arial " + font(14), text = "The possible squares for player 2 to put in are lit up.")
        elif (messageNo == 8 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 9
            animateText("Imagine player 2 puts their square here, where can player 1 put their squares?", 333, 270, 17, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
                    
            full.create_rectangle(offsetX + 0 * 31 + 2 * 97, offsetY + 1 * 31 + 2 * 97, offsetX + 0 * 31 + 2 * 97 + 30, offsetY + 1 * 31 + 2 * 97 + 30, fill = "turquoise", outline = "")
            full.create_rectangle(offsetX + 2 * 31 + 0 * 97, offsetY + 0 * 31 + 1 * 97, offsetX + 2 * 31 + 0 * 97 + 30, offsetY + 0 * 31 + 1 * 97 + 30, fill = "red", outline = "")
            for j in range (0, 3):
                for i in range (0, 3):
                    full.create_rectangle(offsetX + 97 * i + 2, offsetY + 97 * j + 2, offsetX + 97 * i + 92 - 2, offsetY + 97 * j + 92 - 2, fill = "", outline = "magenta", width = 2)
        elif (messageNo == 9 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 10
            animateText("Exactly, player 1 is going to put their squares in one of these lit-up areas.", 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
                            if (i == 2 and j == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = khaki, outline = "")

                    
            full.create_rectangle(offsetX + 0 * 31 + 2 * 97, offsetY + 1 * 31 + 2 * 97, offsetX + 0 * 31 + 2 * 97 + 30, offsetY + 1 * 31 + 2 * 97 + 30, fill = "turquoise", outline = "")
            full.create_rectangle(offsetX + 2 * 31 + 0 * 97, offsetY + 0 * 31 + 1 * 97, offsetX + 2 * 31 + 0 * 97 + 30, offsetY + 0 * 31 + 1 * 97 + 30, fill = "red", outline = "")
            for j in range (0, 3):
                for i in range (0, 3):
                    full.create_rectangle(offsetX + 97 * i + 2, offsetY + 97 * j + 2, offsetX + 97 * i + 92 - 2, offsetY + 97 * j + 92 - 2, fill = "", outline = "magenta", width = 2)

        elif (messageNo == 10 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 11
            animateText("It seems like this part of the rule is clear, but there is one exception.", 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
                            if (i == 2 and j == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = khaki, outline = "")

                    
            full.create_rectangle(offsetX + 0 * 31 + 2 * 97, offsetY + 1 * 31 + 2 * 97, offsetX + 0 * 31 + 2 * 97 + 30, offsetY + 1 * 31 + 2 * 97 + 30, fill = "turquoise", outline = "")
            full.create_rectangle(offsetX + 2 * 31 + 0 * 97, offsetY + 0 * 31 + 1 * 97, offsetX + 2 * 31 + 0 * 97 + 30, offsetY + 0 * 31 + 1 * 97 + 30, fill = "red", outline = "")
            for j in range (0, 3):
                for i in range (0, 3):
                    full.create_rectangle(offsetX + 97 * i + 2, offsetY + 97 * j + 2, offsetX + 97 * i + 92 - 2, offsetY + 97 * j + 92 - 2, fill = "", outline = "magenta", width = 2)

        elif (messageNo == 11 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 12
            animateText("What if player 1 put their square on the one that's boxed? What should player 2 do?", 333, 270, 16, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[1, 2, 2], [2, 1, 2], [2, 2, 2]]
            F = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")

            full.create_rectangle(1 * 31 + 0 * 97 + offsetX + 2, 1 * 31 + 1 * 97 + offsetY + 2, 1 * 31 + 30 + 0 * 97 + offsetX - 2, 1 * 31 + 30 + 1 * 97 + offsetY - 2, fill = "", outline = "gold", width = 2)
        elif (messageNo == 12 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 13
            animateText("As you can see, player 1 put their square in the middle of a big square.", 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[1, 2, 2], [2, 1, 2], [2, 2, 2]]
            F = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")

            full.create_rectangle(1 * 31 + 0 * 97 + offsetX + 2, 1 * 31 + 1 * 97 + offsetY + 2, 1 * 31 + 30 + 0 * 97 + offsetX - 2, 1 * 31 + 30 + 1 * 97 + offsetY - 2, fill = "", outline = "gold", width = 2)
        elif (messageNo == 13 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 14
            animateText("So, player 2 should put their square in the big middle square, however it is full.", 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[1, 2, 2], [2, 1, 2], [2, 2, 2]]
            F = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")

            full.create_rectangle(1 * 31 + 0 * 97 + offsetX + 2, 1 * 31 + 1 * 97 + offsetY + 2, 1 * 31 + 30 + 0 * 97 + offsetX - 2, 1 * 31 + 30 + 1 * 97 + offsetY - 2, fill = "", outline = "gold", width = 2)
        elif (messageNo == 14 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 15
            animateText("So, player 2 can choose to put their square wherever they want on the grid.", 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[1, 2, 2], [2, 1, 2], [2, 2, 2]]
            F = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = khaki, outline = "")

            full.create_rectangle(1 * 31 + 0 * 97 + offsetX + 2, 1 * 31 + 1 * 97 + offsetY + 2, 1 * 31 + 30 + 0 * 97 + offsetX - 2, 1 * 31 + 30 + 1 * 97 + offsetY - 2, fill = "", outline = "gold", width = 2)
            full.create_text(350, 750, fill = "SpringGreen3", font = "arial " + font(14), text = "The possible squares for player 2 to put in are lit up.")

        elif (messageNo == 15 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 16
            animateText('Now you know the rules, but you might ask, "How can I win this game?"', 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[1, 2, 2], [2, 1, 2], [2, 2, 2]]
            F = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")

            full.create_rectangle(1 * 31 + 0 * 97 + offsetX + 2, 1 * 31 + 1 * 97 + offsetY + 2, 1 * 31 + 30 + 0 * 97 + offsetX - 2, 1 * 31 + 30 + 1 * 97 + offsetY - 2, fill = "", outline = "gold", width = 2)
        elif (messageNo == 16 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 17
            animateText('The aim of this game is to make as many three-in-a-rows of your color as you can.', 333, 270, 17, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[1, 2, 2], [2, 1, 2], [2, 2, 2]]
            F = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")

            full.create_rectangle(1 * 31 + 0 * 97 + offsetX + 2, 1 * 31 + 1 * 97 + offsetY + 2, 1 * 31 + 30 + 0 * 97 + offsetX - 2, 1 * 31 + 30 + 1 * 97 + offsetY - 2, fill = "", outline = "gold", width = 2)
        elif (messageNo == 17 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 18
            animateText('The player with the most number of "rows" wins the game.', 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[1, 2, 2], [2, 1, 2], [2, 2, 2]]
            F = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")

            full.create_rectangle(1 * 31 + 0 * 97 + offsetX + 2, 1 * 31 + 1 * 97 + offsetY + 2, 1 * 31 + 30 + 0 * 97 + offsetX - 2, 1 * 31 + 30 + 1 * 97 + offsetY - 2, fill = "", outline = "gold", width = 2)
        elif (messageNo == 18 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 19
            animateText('Now let me clearly define what a "row" is with a clear board.', 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 19 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 20
            animateText('A row is three squares next to each other in any direction that has one color, inside a big square.', 333, 270, 14, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 20 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 21
            animateText('For example, this is a row.', 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            D = [[1, 1, 1], [0, 0, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 21 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 22
            animateText('This is an example of another row.', 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            G = [[0, 2, 0], [0, 2, 0], [0, 2, 0]]
            H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")

        elif (messageNo == 22 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 23
            animateText('And this is also a row.', 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 23 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 24
            animateText('However, this is not a row because it is not all within one big square.', 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
            C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            F = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 24 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 25
            animateText('And this is not a row because it consists of different colors.', 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            B = [[2, 0, 0], [0, 1, 0], [0, 0, 1]]
            C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 25 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 26
            animateText("Now that you understand the game, let's try learning the controls of the game.", 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")

            A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # its this one thats the last where player one put their square for the demo dumbo
            E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tempArray = [[A, B, C], [D, E, F], [G, H, I]]

            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (tempArray[j][i][y][x] == 1):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "turquoise", outline = "")
                            elif (tempArray[j][i][y][x] == 2):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = "red", outline = "")
                            elif (tempArray[j][i][y][x] == 0):
                                full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 26 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 27
            animateText("In this game, there will be two virtual mouses controlled by the keyboard.", 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")
            
            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "")
        elif (messageNo == 27 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 28
            animateText("Player 1's mouse will be controlled by WASD and player 2's mouse will be controlled by arrow keys.", 333, 270, 14, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")
            
            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "") 
        elif (messageNo == 28 and justClicked == False):
            offsetX = 200
            offsetY = 450
            justClicked = True
            messageNo = 29
            animateText("With this information, you can now start playing!", 333, 270, 18, "turquoise", "LightCyan1", 575, 305, True)

            full.create_rectangle(0, 320, 666, 866, fill = "light blue", outline = "")
            
            full.create_rectangle(30 + offsetX, 0 + offsetY, 31 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(61 + offsetX, 0 + offsetY, 62 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            
            full.create_rectangle(127 + offsetX, 0 + offsetY, 128 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(158 + offsetX, 0 + offsetY, 159 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(224 + offsetX, 0 + offsetY, 225 + offsetX, 286 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(255 + offsetX, 0 + offsetY, 256 + offsetX, 286 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 30 + offsetY, 286 + offsetX, 31 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 61 + offsetY, 286 + offsetX, 62 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 127 + offsetY, 286 + offsetX, 128 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 158 + offsetY, 286 + offsetX, 159 + offsetY, fill = "gray", outline = "")

            full.create_rectangle(0 + offsetX, 224 + offsetY, 286 + offsetX, 225 + offsetY, fill = "gray", outline = "")
            full.create_rectangle(0 + offsetX, 255 + offsetY, 286 + offsetX, 256 + offsetY, fill = "gray", outline = "")
            
            # Big Lines
            full.create_rectangle(92 + offsetX, 0 + offsetY, 97 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(189 + offsetX, 0 + offsetY, 194 + offsetX, 286 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 92 + offsetY, 286 + offsetX, 97 + offsetY, fill = "blue", outline = "")
            full.create_rectangle(0 + offsetX, 189 + offsetY, 286 + offsetX, 194 + offsetY, fill = "blue", outline = "")
            
            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            full.create_rectangle(x * 31 + i * 97 + offsetX, y * 31 + j * 97 + offsetY, x * 31 + 30 + i * 97 + offsetX, y * 31 + 30 + j * 97 + offsetY, fill = defaultColor, outline = "") 
            doneWelcome2 = True
            stage = "Customization"
                            
    elif (doneMouse == False and stage == "Customization"):
        full.create_rectangle(0, 0, 666, 866, fill = "DodgerBlue2", outline = "")
        full.create_text(333, 70, fill = "slate blue", font = (gentiumBookClassic, int(font(130)), "normal"), text = "eXOtended!")
        #full.create_text(337, 170, fill = "slate blue", font = "arial " + font(94) + " bold", text = "TIC TAC TOE!")
        posX1 = 300
        posY1 = 429

        posX2 = 300
        posY2 = 683
        full.create_rectangle(0, 220, 666, 270, fill = "LightCyan1", outline = "")
        full.create_text(333, 245, fill = "turquoise", font = "arial " + font(25) + " bold", text = "Mouse Customization")

        full.create_rectangle(10, 280, 656, 350, fill = "DeepSkyBlue2", outline = "")
        full.create_text(333, 295, fill = "LightCyan1", font = "arial " + font(14), text = "For Player 1, use keys A and D from WASD to slide across to different mouses. For Player 2, use the")
        full.create_text(333, 315, fill = "LightCyan1", font = "arial " + font(14), text = "left and right arrow keys to slide across different mouses. When Player 1 is done, press the space")
        full.create_text(333, 335, fill = "LightCyan1", font = "arial " + font(14), text = "bar and the 'OK?' will be 'OK!'. Same goes to player 2, except they shall press the enter key.")

        full.create_rectangle(10, 360, 656, 598, fill = "SteelBlue2", outline = "")
        full.create_text(115, 380, fill = "steel blue", font = "arial " + font(25) + " bold", text = "Player 1's Mouse")
        full.create_rectangle(posX1 - 15, posY1 + 45, posX1 + 85, posY1 + 105, fill = colorTemp1, outline = "")
        full.create_rectangle(posX1, posY1, posX1 + 30, posY1 + 45, fill = colorTemp1, outline = "")
        if (okay1 == "OK?"):
            full.create_text(550, 479, fill = paleGreen, font = "arial " + font(60) + " bold", text = "OK?")
        elif (okay1 == "OK!"):
            full.create_text(550, 479, fill = "SpringGreen2", font = "arial " + font(60) + " bold", text = "OK!")

        full.create_rectangle(10, 608, 656, 838, fill = "SteelBlue2", outline = "")
        full.create_text(115, 628, fill = "steel blue", font = "arial " + font(25) + " bold", text = "Player 2's Mouse")
        full.create_rectangle(posX2 - 15, posY2 + 45, posX2 + 85, posY2 + 105, fill = colorTemp2, outline = "")
        full.create_rectangle(posX2, posY2, posX2 + 30, posY2 + 45, fill = colorTemp2, outline = "")
        if (okay2 == "OK?"):
            full.create_text(550, 723, fill = paleGreen, font = "arial " + font(60) + " bold", text = "OK?")
        elif (okay2 == "OK!"):
            full.create_text(550, 723, fill = "SpringGreen2", font = "arial " + font(60) + " bold", text = "OK!")

        if (okay1 == "OK!" and okay2 == "OK!"):
            pause(0.5)
            doneMouse = True
            okay1 = "OK?"
            okay2 = "OK?"
            index1 = 0
            index2 = 0
            colorTemp1 = possibleColors[0]
            colorTemp2 = possibleColors[0]
            resetFull()
    elif (doneMouse == True and doneGrid == False):
        full.create_rectangle(0, 0, 666, 866, fill = "DodgerBlue2", outline = "")
        full.create_text(333, 70, fill = "slate blue", font = (gentiumBookClassic, int(font(130)), "normal"), text = "eXOtended!")
        #full.create_text(337, 170, fill = "slate blue", font = "arial " + font(94) + " bold", text = "TIC TAC TOE!")
        posX1 = 330
        posY1 = 469

        posX2 = 330
        posY2 = 717
        full.create_rectangle(0, 220, 666, 270, fill = "LightCyan1", outline = "")
        full.create_text(333, 245, fill = "turquoise", font = "arial " + font(25) + " bold", text = "Grid Customization")

        full.create_rectangle(10, 280, 656, 350, fill = "DeepSkyBlue2", outline = "")
        full.create_text(333, 295, fill = "LightCyan1", font = "arial " + font(14), text = "For Player 1, use keys A and D from WASD to slide across to different options. For Player 2, use the")
        full.create_text(333, 315, fill = "LightCyan1", font = "arial " + font(14), text = "left and right arrow keys to slide across different options. When Player 1 is done, press the space")
        full.create_text(333, 335, fill = "LightCyan1", font = "arial " + font(14), text = "bar and the 'OK?' will be 'OK!'. Same goes to player 2, except they shall press the enter key.")

        full.create_rectangle(10, 360, 656, 598, fill = "SteelBlue2", outline = "")
        full.create_text(105, 380, fill = "steel blue", font = "arial " + font(25) + " bold", text = "Player 1's Grid")
        full.create_rectangle(242, 389, 424, 569, fill = "snow", outline = "")
        full.create_rectangle(303, 450, 363, 510, fill = colorTemp1, outline = "")     
        full.create_rectangle(posX1 - 5, posY1 + 15, posX1 + 25, posY1 + 35, fill = player1MouseColor, outline = "")
        full.create_rectangle(posX1, posY1, posX1 + 10, posY1 + 15, fill = player1MouseColor, outline = "")
        if (okay1 == "OK?"):
            full.create_text(550, 479, fill = paleGreen, font = "arial " + font(60) + " bold", text = "OK?")
        elif (okay1 == "OK!"):
            full.create_text(550, 479, fill = "SpringGreen2", font = "arial " + font(60) + " bold", text = "OK!")

        full.create_rectangle(10, 608, 656, 838, fill = "SteelBlue2", outline = "")
        full.create_text(105, 628, fill = "steel blue", font = "arial " + font(25) + " bold", text = "Player 2's Grid")
        full.create_rectangle(242, 637, 424, 817, fill = "snow", outline = "")
        full.create_rectangle(303, 698, 363, 759, fill = colorTemp2, outline = "")
        full.create_rectangle(posX2 - 5, posY2 + 15, posX2 + 25, posY2 + 35, fill = player2MouseColor, outline = "")
        full.create_rectangle(posX2, posY2, posX2 + 10, posY2 + 15, fill = player2MouseColor, outline = "")
        if (okay2 == "OK?"):
            full.create_text(550, 723, fill = paleGreen, font = "arial " + font(60) + " bold", text = "OK?")
        elif (okay2 == "OK!"):
            full.create_text(550, 723, fill = "SpringGreen2", font = "arial " + font(60) + " bold", text = "OK!")
        if (okay1 == "OK!" and okay2 == "OK!"):
            pause(0.5)
            okay1 = "OK?"
            okay2 = "OK?"
            doneGrid = True
            stage = "Starting Game"
            resetFull()
    elif (doneBeginGame == False and stage == "Starting Game"):
        full.create_rectangle(0, 0, 666, 866, fill = "DodgerBlue2", outline = "")
        full.create_text(333, 70, fill = "slate blue", font = (gentiumBookClassic, int(font(130)), "normal"), text = "eXOtended!")
        #full.create_text(337, 170, fill = "slate blue", font = "arial " + font(94) + " bold", text = "TIC TAC TOE!")
        pointX1 = 10
        pointY1 = 5

        pointX2 = 80
        pointY2 = 5
        full.create_rectangle(100, 420, 566, 470, fill = darkerColor(player1GridColor), outline = "")
        full.create_text(333, 445, fill = player1GridColor, font = "arial " + font(25) + " bold", text = "Begin Button for Player 1 to Press")

        full.create_rectangle(100, 620, 566, 670, fill = darkerColor(player2GridColor), outline = "")
        full.create_text(333, 645, fill = player2GridColor, font = "arial " + font(25) + " bold", text = "Begin Button for Player 2 to Press")
        
        full.create_rectangle(10, 220, 656, 290, fill = "DeepSkyBlue2", outline = "")
        full.create_text(333, 235, fill = "LightCyan1", font = "arial " + font(14), text = 'For Player 1, use WASD keys to move around, SPACE to "click" a button, and X to switch between')
        full.create_text(333, 255, fill = "LightCyan1", font = "arial " + font(14), text = 'areas. For Player 2, use arrow keys to move around, ENTER to "click" a button, and SHIFT to switch')
        full.create_text(333, 275, fill = "LightCyan1", font = "arial " + font(14), text = 'between areas. Please "click" the button corresponding to your role to begin. This is made for practice.')
        drawMouse1()
        drawMouse2()

        if (okay1 == "OK?"):
            full.create_text(615, 445, fill = paleGreen, font = "arial " + font(25) + " bold", text = "OK?")
        elif (okay1 == "OK!"):
            full.create_text(615, 445, fill = "SpringGreen2", font = "arial " + font(25) + " bold", text = "OK!")

        if (okay2 == "OK?"):
            full.create_text(615, 645, fill = paleGreen, font = "arial " + font(25) + " bold", text = "OK?")
        elif (okay2 == "OK!"):
            full.create_text(615, 645, fill = "SpringGreen2", font = "arial " + font(25) + " bold", text = "OK!")
        
        if (okay1 == "OK!" and okay2 == "OK!"):
            pause(0.5)
            exitFull()
            maingame()

def redraw():
    if (stage == "Game"):
        global ended
        resetPlayerDisplay()
        resetFull()
        resetInfos()
        if (ended == False):
            drawgrid()
            bigGridLightUp()
        else:
            bigGridLightUp()
            drawgrid()

        if (mouse1Canvas == "infos"):
            if (ended == True):
                winDraw()
            if (playerTurn == "Player 1" and ended == False):
                drawMouse2()
                drawMouse1()
            elif (playerTurn == "Player 2" and ended == False):
                drawMouse1()
                drawMouse2()
            elif (playerTurn == "Player 2" and ended == True):
                drawMouse2()
                game.create_rectangle(30, 208, 536, 358, fill = "DodgerBlue2", outline = "")
                game.create_text(283, 283, fill = "light sky blue", font = "arial " + font(75) + " bold", text = "GAME OVER!")
                drawMouse1()
        elif (mouse2Canvas == "infos"):
            if (ended == True):
                winDraw()
            if (playerTurn == "Player 1" and ended == False):
                drawMouse2()
                drawMouse1()
            elif (playerTurn == "Player 2" and ended == False):
                drawMouse1()
                drawMouse2()
            elif (playerTurn == "Player 2" and ended == True):
                drawMouse1()
                game.create_rectangle(30, 208, 536, 358, fill = "DodgerBlue2", outline = "")
                game.create_text(283, 283, fill = "light sky blue", font = "arial " + font(75) + " bold", text = "GAME OVER!")
                drawMouse2()
        else:
            if (playerTurn == "Player 2"):
                drawMouse1()
                drawMouse2()
            elif (playerTurn == "Player 1"):
                drawMouse2()
                drawMouse1()
            if (ended == True):
                winDraw()  
    elif (stage == "Starting Game"):
        resetFull()

def mouse1Left(event):
    if ((playerTurn == "Player 1" or (playerTurn == "Player 2" and ended == True)) or mouse1Canvas == "full"):
        global pointX1, index1, index2, colorTemp1
        if (mouse1Canvas == "game"):
            if (pointX1 >= 85):
                pointX1 -= 63
            redraw()
        elif (mouse1Canvas == "infos"):
            if (pointX1 >= 15):
                pointX1 -= 10
            redraw()
        elif (mouse1Canvas == "full" and stage != "Customization"):
            if (pointX1 >= 35):
                pointX1 -= 30
            redraw()
        elif (mouse1Canvas == "full" and stage == "Customization"):
            if (index1 <= len(possibleColors) - 1 and index1 != 0):
                index1 -= 1
                colorTemp1 = possibleColors[index1]
            resetFull()
        
def mouse1Right(event):
    if ((playerTurn == "Player 1" or (playerTurn == "Player 2" and ended == True)) or mouse1Canvas == "full"):
        global pointX1, index1, index2, colorTemp1
        if (mouse1Canvas == "game"):
            if (pointX1 <= 481):
                pointX1 += 63
            redraw()
        elif (mouse1Canvas == "infos"):
            if (pointX1 <= 631):
                pointX1 += 10
            redraw()
        elif (mouse1Canvas == "full" and stage != "Customization"):
            if (pointX1 <= 611):
                pointX1 += 30
            redraw()
        elif (mouse1Canvas == "full" and stage == "Customization"):
            if (index1 < len(possibleColors) - 1):
                index1 += 1
                colorTemp1 = possibleColors[index1]
            resetFull()

def mouse1Up(event):
    if ((playerTurn == "Player 1" or (playerTurn == "Player 2" and ended == True)) or mouse1Canvas == "full"):
        global pointY1
        if (mouse1Canvas == "game"):
            if (pointY1 >= 63):
                pointY1 -= 63
            redraw()
        elif (mouse1Canvas == "infos"):
            if (pointY1 >= 10):
                pointY1 -= 10
            redraw()
        elif (mouse1Canvas == "full" and stage != "Customization"):
            if (pointY1 >= 30):
                pointY1 -= 30
            redraw()

def mouse1Down(event):
    if ((playerTurn == "Player 1" or (playerTurn == "Player 2" and ended == True)) or mouse1Canvas == "full"):
        global pointY1
        if (mouse1Canvas == "game"):
            if (pointY1 <= 471):
                pointY1 += 63
            redraw()
        elif (mouse1Canvas == "infos"):
            if (pointY1 <= 105):
                pointY1 += 10
            redraw()
        elif (mouse1Canvas == "full" and stage != "Customization"):
            if (pointY1 <= 771):
                pointY1 += 30
            redraw()

def mouse2Left(event):
    if ((playerTurn == "Player 2" or (playerTurn == "Player 1" and ended == True)) or mouse2Canvas == "full"):
        global pointX2, colorTemp2, index1, index2
        if (mouse2Canvas == "game"):
            if (pointX2 >= 85):
                pointX2 -= 63
            redraw()
        elif (mouse2Canvas == "infos"):
            if (pointX2 >= 15):
                pointX2 -= 10 
            redraw()
        elif (mouse2Canvas == "full" and stage != "Customization"):
            if (pointX2 >= 35):
                pointX2 -= 30
            redraw()
        elif (mouse2Canvas == "full" and stage == "Customization"):
            if (index2 <= len(possibleColors) - 1 and index2 != 0):
                index2 -= 1
                colorTemp2 = possibleColors[index2]
            resetFull()

def mouse2Right(event):
    if ((playerTurn == "Player 2" or (playerTurn == "Player 1" and ended == True)) or mouse2Canvas == "full"):
        global pointX2, colorTemp2, index1, index2
        if (mouse2Canvas == "game"):
            if (pointX2 <= 481):
                pointX2 += 63
            redraw()
        elif (mouse2Canvas == "infos"):
            if (pointX2 <= 631):
                pointX2 += 10
            redraw()
        elif (mouse2Canvas == "full" and stage != "Customization"):
            if (pointX2 <= 611):
                pointX2 += 30
            redraw()
        elif (mouse2Canvas == "full" and stage == "Customization"):
            if (index2 < len(possibleColors) - 1):
                index2 += 1
                colorTemp2 = possibleColors[index2]
            resetFull()

def mouse2Up(event):
    if ((playerTurn == "Player 2" or (playerTurn == "Player 1" and ended == True)) or mouse2Canvas == "full"):
        global pointY2
        if (mouse2Canvas == "game"):
            if (pointY2 >= 63):
                pointY2 -= 63
            redraw()
        if (mouse2Canvas == "infos"):
            if (pointY2 >= 10):
                pointY2 -= 10
            redraw()
        elif (mouse2Canvas == "full" and stage != "Customization"):
            if (pointY2 >= 30):
                pointY2 -= 30
            redraw()

def mouse2Down(event):
    if ((playerTurn == "Player 2" or (playerTurn == "Player 1" and ended == True)) or mouse2Canvas == "full"):
        global pointY2
        if (mouse2Canvas == "game"):
            if (pointY2 <= 471):
                pointY2 += 63
            redraw()
        if (mouse2Canvas == "infos"):
            if (pointY2 <= 105):
                pointY2 += 10
            redraw()
        elif (mouse2Canvas == "full" and stage != "Customization"):
            if (pointY2 <= 771):
                pointY2 += 30
            redraw()

def switchCanvas1(event):
    global mouse1Canvas, pointX1, pointY1
    if ((playerTurn == "Player 1" and (mouse1Canvas == "game" or mouse1Canvas == "infos")) or (ended == True)):
        if (mouse1Canvas == "game"):
            pointX1 = 5
            pointY1 = 0
            mouse1Canvas = "infos"
            redraw()
        elif (mouse1Canvas == "infos"):
            pointX1 = 25
            pointY1 = 20
            mouse1Canvas = "game"
            redraw()

def switchCanvas2(event):
    global mouse2Canvas, pointX2, pointY2
    if (stage == "Welcomes" and messageNo == -1):
        skipTutorial()
    if ((playerTurn == "Player 2" and (mouse2Canvas == "game" or mouse2Canvas == "infos")) or (ended == True)):
        if (mouse2Canvas == "game"):
            pointX2 = 5
            pointY2 = 0
            mouse2Canvas = "infos"
            redraw()
        elif (mouse2Canvas == "infos"):
            pointX2 = 25
            pointY2 = 20
            mouse2Canvas = "game"
            redraw()

def isSquareLit(x, y):
    for i in range (0, 9):
        if (x == validGrids[i][0] and y == validGrids[i][1]):
            return True

def clickMouse1(event):
    global mouse1Canvas, mouse2Canvas, pointX1, pointY1, pointX2, pointY2, playerTurn, smallX1, smallY1, bigGrid1, bigX1, bigY1, player1Lines, freePlace, stage, okay1, index1, index2, player1MouseColor
    global possibleColors, colorTemp1, colorTemp2, player1GridColor, doneBeginGame, okay2, doneMouse, doneGrid
    if (mouse1Canvas == "game" and (playerTurn == "Player 1" or (playerTurn == "Player 2" and ended == True))):
        if (smallX1 == 3):
            bigX1 = int(pointX1 / 192)
            bigY1 = int(pointY1 / 192)

            smallX1 = int((pointX1 % 192) / 61)
            smallY1 = int((pointY1 % 192) / 61)

            bigGrid1 = grid[bigY1][bigX1]
        elif (freePlace == True):
            bigX1 = int(pointX1 / 192)
            bigY1 = int(pointY1 / 192)

            smallX1 = int((pointX1 % 192) / 61)
            smallY1 = int((pointY1 % 192) / 61)

            bigGrid1 = grid[bigY1][bigX1]
            freePlace = False
        elif (gridLetters[int(pointY1 / 192)][int(pointX1 / 192)] == validBigGridLetter):
            bigX1 = int(pointX1 / 192)
            bigY1 = int(pointY1 / 192)

            smallX1 = int((pointX1 % 192) / 61)
            smallY1 = int((pointY1 % 192) / 61)

            bigGrid1 = grid[bigY1][bigX1]

        if (smallX1 != 3):
            if (grid[bigY1][bigX1][smallY1][smallX1] == 0):
                grid[bigY1][bigX1][smallY1][smallX1] = 1
                playerTurn = "Player 2"

        player1Lines = checkLines(1)
        redraw()
    elif (mouse1Canvas == "infos"):
        if ((pointX1 >= 456 and pointX1 <= 656) and (pointY1 >= 10 and pointY1 <= 60)):
            playAgain()
        if ((pointX1 >= 315 and pointX1 <= 445) and (pointY1 >= 10 and pointY1 <= 60)):
            stage = "Customization"
            okay1 = "OK?"
            okay2 = "OK?"
            mouse2Canvas = "full"
            doneMouse = False
            doneGrid = False
            doneBeginGame = False
            pointX1 = 25
            pointY1 = 20
            pointX2 = 25
            pointY2 = 20
            mouse1Canvas = "full"
            mouse2Canvas = "full"
            index1 = 0
            index2 = 0
            possibleColors = ["red", "orange", yellow, "green2", "turquoise", "magenta", "purple", "RosyBrown4", "gray64"]
            colorTemp1 = possibleColors[index1]
            colorTemp2 = possibleColors[index2]
            createFull()
            resetFull()
    elif (mouse1Canvas == "full" and stage == "Customization"):
        if (colorTemp2 == colorTemp1):
            if (okay2 == "OK?" and okay1 == "OK?"):
                okay1 = "OK!"
                if (index2 > index1):
                    index2 -= 1
                if (doneMouse == True):
                    player1GridColor = colorTemp1
                elif (doneMouse == False):
                    player1MouseColor = colorTemp1
                possibleColors.pop(index1)
                colorTemp2 = possibleColors[index2]
                resetFull()
        elif (colorTemp2 != colorTemp1 and okay1 == "OK?"):
            okay1 = "OK!"
            if (index2 > index1):
                index2 -= 1
            if (doneMouse == True):
                player1GridColor = colorTemp1
            elif (doneMouse == False):
                player1MouseColor = colorTemp1
            possibleColors.pop(index1)
            if (okay2 == "OK!"):               
                resetFull()
                if (doneBeginGame == True):
                    mouse1Canvas = "game"
                    mouse2Canvas = "game"
                    stage = "Game"
                    pointX1 = 25
                    pointY1 = 20
                    pointX2 = 25
                    pointY2 = 20
                    exitFull()
                    maingame()
            elif (okay2 == "OK!"):
                resetFull()
            elif (okay2 == "OK?"):
                resetFull()
    elif (mouse1Canvas == "full" and stage == "Starting Game"):
        if ((pointX1 >= 100 and pointX1 <= 566) and (pointY1 >= 420 and pointY1 <= 470)):
            okay1 = "OK!"
            resetFull()
                
def clickMouse2(event):
    global mouse1Canvas, mouse2Canvas, pointX1, pointY1, pointX2, pointY2, playerTurn, smallX2, smallY2, bigGrid2, bigX2, bigY2, player2Lines, freePlace, stage, index1, index2, okay2, okay1, player2MouseColor
    global possibleColors, colorTemp1, colorTemp2, player2GridColor, doneBeginGame, doneWelcome1, justClicked, messageNo, askedTutorial, doneMouse, doneGrid, possibleColors, player1MouseColor
    if (stage == "Welcomes" and doneWelcome1 == False):
        doneWelcome1 = True
        resetFull()
    elif (stage == "Welcomes" and askedTutorial == False):
        askedTutorial = True
        resetFull()
    elif (stage == "Welcomes" and doneWelcome2 == False):
        if (messageNo == -1 or messageNo < 30):
            justClicked = False
            resetFull()
    elif (mouse2Canvas == "game" and (playerTurn == "Player 2" or (playerTurn == "Player 1" and ended == True))):
        if (smallX1 == 3):
            bigX2 = int(pointX2 / 192)
            bigY2 = int(pointY2 / 192)

            smallX2 = int((pointX2 % 192) / 61)
            smallY2 = int((pointY2 % 192) / 61)

            bigGrid2 = grid[bigY2][bigX2]
        elif (freePlace == True):
            bigX2 = int(pointX2 / 192)
            bigY2 = int(pointY2 / 192)

            smallX2 = int((pointX2 % 192) / 61)
            smallY2 = int((pointY2 % 192) / 61)

            freePlace = False
        elif (gridLetters[int(pointY2 / 192)][int(pointX2 / 192)] == validBigGridLetter):
            bigX2 = int(pointX2 / 192)
            bigY2 = int(pointY2 / 192)

            smallX2 = int((pointX2 % 192) / 61)
            smallY2 = int((pointY2 % 192) / 61)

            bigGrid2 = grid[bigY2][bigX2]

        if (smallX2 != 3):
            if (grid[bigY2][bigX2][smallY2][smallX2] == 0):
                grid[bigY2][bigX2][smallY2][smallX2] = 2
                playerTurn = "Player 1"

        player2Lines = checkLines(2)
        redraw()
    elif (mouse2Canvas == "infos"):
        if ((pointX2 >= 456 and pointX2 <= 656) and (pointY2 >= 10 and pointY2 <= 60)):
            playAgain()
        if ((pointX2 >= 315 and pointX2 <= 445) and (pointY2 >= 10 and pointY2 <= 60)):
            stage = "Customization"
            okay1 = "OK?"
            okay2 = "OK?"
            mouse2Canvas = "full"
            doneMouse = False
            doneGrid = False
            doneBeginGame = False
            pointX1 = 25
            pointY1 = 20
            pointX2 = 25
            pointY2 = 20
            mouse1Canvas = "full"
            mouse2Canvas = "full"
            index1 = 0
            index2 = 0
            possibleColors = ["red", "orange", yellow, "green2", "turquoise", "magenta", "purple", "RosyBrown4", "gray64"]
            colorTemp1 = possibleColors[index1]
            colorTemp2 = possibleColors[index2]
            createFull()
            resetFull()
    elif (mouse2Canvas == "full" and stage == "Customization"):
        if (colorTemp2 == colorTemp1 and messageNo != 30):
            if (okay1 == "OK?" and okay2 == "OK?"):
                if (justClicked == False):
                    okay2 = "OK!"
                    if (index1 > index2):
                        index1 -= 1
                    if (doneMouse == True):
                        player2GridColor = colorTemp2
                    elif (doneMouse == False):
                        player2MouseColor = colorTemp2
                    possibleColors.pop(index2)
                    colorTemp1 = possibleColors[index1]
                    resetFull()
                elif (justClicked == True):
                    justClicked = False
                    resetFull()
        elif (colorTemp2 != colorTemp1 and okay2 == "OK?"):
            if (justClicked == False):
                okay2 = "OK!"
                if (index1 > index2):
                    index1 -= 1
                if (doneMouse == True):
                    player2GridColor = colorTemp2
                elif (doneMouse == False):
                    player2MouseColor = colorTemp2
                possibleColors.pop(index2)
                if (okay1 == "OK!" and doneMouse == True):
                    resetFull()
                    if (doneBeginGame == True):
                        mouse1Canvas = "game"
                        mouse2Canvas = "game"
                        stage = "Game"
                        pointX1 = 25
                        pointY1 = 20
                        pointX2 = 25
                        pointY2 = 20
                        exitFull()
                        maingame()
                elif (okay1 == "OK!" and doneMouse == False):
                    resetFull()
                elif (okay1 == "OK?"):
                    resetFull()
            elif (justClicked == True):
                justClicked = False
                resetFull()
    elif (mouse2Canvas == "full" and stage == "Starting Game"):
        if ((pointX2 >= 100 and pointX2 <= 566) and (pointY2 >= 620 and pointY2 <= 670)):
            okay2 = "OK!"
            resetFull()
        
def bigGridLightUp():
    global grid, smallX1, smallY1, smallX2, smallY2, bigX1, bigY1, bigX2, bigY2, playerTurn, bigGrid1, bigGrid2, validGrids, validBigGridLetter, mouse1Canvas, mouse2Canvas
    global pointX1, pointY1, pointX2, pointY2, freePlace
    noLitUp = True
    if (smallX1 == 3):
        for j in range (0, 3):
            for i in range (0, 3):
                for y in range (0, 3):
                    for x in range (0, 3):
                        if (grid[j][i][y][x] == 0):
                            noLitUp = False
                            game.create_rectangle(x * 61 + i * 192 + 1, y * 61 + j * 192 + 1, x * 61 + 59 + i * 192, y*61+59+j*192,width=2,fill=khaki,outline=khaki)
                        
    if (playerTurn == "Player 2"):
        game.create_rectangle(smallX1 * 61 + bigX1 * 192+1, smallY1 * 61 + bigY1 * 192+1, smallX1 * 61 + 59 + bigX1 * 192, smallY1 * 61 + 59 + bigY1*192, width=2, fill=player1GridColor, outline="gold")
        for y in range (0, 3):
            for x in range (0, 3):
                if (grid[smallY1][smallX1][y][x] == 0):
                    noLitUp = False
                    game.create_rectangle(x * 61 + smallX1 * 192 + 1, y * 61 + smallY1 * 192 + 1, x * 61 + 59 + smallX1 * 192, y*61+59+smallY1*192,width=2,fill=khaki,outline=khaki)
                    validGrids[3 * y + x] = [x, y]
                    validBigGridLetter = gridLetters[smallY1][smallX1]

        if (noLitUp == True):
            freePlace = True
            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (grid[j][i][y][x] == 0):
                                game.create_rectangle(x * 61 + i * 192, y * 61 + j * 192, x * 61 + 60 + i * 192, y * 61 + 60 + j * 192, fill = khaki, outline = "")

    if (playerTurn == "Player 1" and smallX1 != 3):
        game.create_rectangle(smallX2 * 61 + bigX2 * 192+1, smallY2 * 61 + bigY2 * 192+1, smallX2 * 61 + 59 + bigX2 * 192, smallY2 * 61 + 59 + bigY2*192, width=2, fill=player2GridColor, outline="gold")
        for y in range (0, 3):
            for x in range (0, 3):
                if (grid[smallY2][smallX2][y][x] == 0):
                    noLitUp = False
                    game.create_rectangle(x * 61 + smallX2 * 192 + 1, y * 61 + smallY2 * 192 + 1, x * 61 + 59 + smallX2 * 192, y*61+59+smallY2*192,width=2,fill=khaki,outline=khaki)
                    validGrids[3 * y + x] = [x, y]
                    validBigGridLetter = gridLetters[smallY2][smallX2]

        if (noLitUp == True):
            freePlace = True
            for j in range (0, 3):
                for i in range (0, 3):
                    for y in range (0, 3):
                        for x in range (0, 3):
                            if (grid[j][i][y][x] == 0):
                                game.create_rectangle(x * 61 + i * 192, y * 61 + j * 192, x * 61 + 60 + i * 192, y * 61 + 60 + j * 192, fill = khaki, outline = "")


    checkFullBoard()
    if (ended == True):
        winDraw()

def checkLines(x):
    lines = 0
    for j in range (0, 3):
        for i in range (0, 3):
            array = grid[j][i]
            if (array[0][0] == array[1][1] and array[1][1] == array[2][2] and array[0][0] == x):
                lines += 1
            elif (array[0][2] == array [1][1] and array[1][1] == array[2][0] and array[0][2] == x):
                lines += 1

            for k in range (0, 3):
                if (array[0][k] == array[1][k] and array[1][k] == array[2][k] and array[0][k] == x):
                    lines += 1

            for n in range (0, 3):
                if (array[n][0] == array[n][1] and array[n][1] == array[n][2] and array[n][0] == x):
                    lines += 1

    return lines

def whosWinning():
    global winningPlayer
    if (player1Lines > player2Lines):
        winningPlayer = "Player 1"
    elif (player2Lines > player1Lines):
        winningPlayer = "Player 2"
    elif (player1Lines == player2Lines):
        winningPlayer = "Tie"

def checkFullBoard():
    global ended, grid, A, B, C, D, E, F, G, H, I
    fullGrid = True
    for y in range (0, 3):
        for x in range (0, 3):
            for j in range (0, 3):
                for i in range (0, 3):
                    array = grid[y][x]
                    if (array[j][i] == 0):
                        fullGrid = False

    ended = fullGrid

def playAgain():
    global pointX1, pointY1, pointX2, pointY2, mouse1Canvas, mouse2Canvas, playerTurn, smallX1, smallY1, smallX2, smallY2, bigX1, bigY1, bigX2, bigY2, bigGrid1, bigGrid2, validGrids, validBigGridLetter
    global player1Lines, player2Lines, winningPlayer, freePlace, ended, A, B, C, D, E, F, G, H, I, grid
    pointX1 = 25
    pointY1 = 20
    pointX2 = 25
    pointY2 = 20

    mouse1Canvas = "game"
    mouse2Canvas = "game"

    playerTurn = "Player 1"

    smallX1 = 3
    smallY1 = 3
    smallX2 = 3
    smallY2 = 3

    bigX1 = 3
    bigY1 = 3
    bigX2 = 3
    bigY2 = 3

    bigGrid1 = A
    bigGrid2 = A

    validGrids = [[], [], [], [], [], [], [], [], []]
    validBigGridLetter = ""

    gridLetters = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

    player1Lines = 0
    player2Lines = 0

    winningPlayer = "Tie"

    freePlace = False

    ended = False

    A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    H = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    I = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid = [[A, B, C], [D, E, F], [G, H, I]]
    
    redraw()

def skipTutorial():
    global stage, messageNo, doneWelcome2, askedTutorial
    if (stage == "Welcomes" and messageNo == -1):
        doneWelcome2 = True
        askedTutorial = True
        stage = "Customization"
        resetFull()

tk.bind("a", mouse1Left)
tk.bind("d", mouse1Right)
tk.bind("w", mouse1Up)
tk.bind("s", mouse1Down)
tk.bind("x", switchCanvas1)
tk.bind("<space>", clickMouse1)

tk.bind("<Left>", mouse2Left)
tk.bind("<Right>", mouse2Right)
tk.bind("<Up>", mouse2Up)
tk.bind("<Down>", mouse2Down)
tk.bind("<Shift_R>", switchCanvas2)
tk.bind("<Shift_L>", switchCanvas2)
tk.bind("<Return>", clickMouse2)

def maingame():
    global mouse1Canvas, mouse2Canvas, stage, pointX1, pointY1, pointX2, pointY2
    mouse1Canvas = "game"
    mouse2Canvas = "game"
    stage = "Game"
    resetPlayerDisplay()
    pointX1 = 25
    pointY1 = 20
    pointX2 = 25
    pointY2 = 20
    displayPlayerTurn()
    resetInfos()
    drawgrid()
    bigGridLightUp()
    drawMouse2()
    drawMouse1()

resetFull()

def quit(self):
    self.tk.destroy()
