from pathlib import Path
from tkinter import Tk, Button, PhotoImage, Frame, Label, messagebox
from sys import exit
from random import choice
from getpass import getuser
user = getuser()
file = open(rf"C:\Users\{user}\AppData\Local\Programs\abbas\config.txt", "r")
stuff = file.readlines()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH0 = OUTPUT_PATH / Path(rf"C:\Users\{user}\AppData\Local\Programs\abbas\frame0")
ASSETS_PATH1 = OUTPUT_PATH / Path(rf"C:\Users\{user}\AppData\Local\Programs\abbas\frame2")
ASSETS_PATH2 = OUTPUT_PATH / Path(rf"C:\Users\{user}\AppData\Local\Programs\abbas\frame1")
ASSETS_PATH3 = OUTPUT_PATH / Path(rf"C:\Users\{user}\AppData\Local\Programs\abbas\frame3")
global mypoints, botpoints, wincount, losscount, drawcount, wickets, turn, started, startingwicket, mychoice, botchoice, won, draw
mypoints= 0
botpoints= 0
wincount = int(stuff[0])
losscount = int(stuff[1])
drawcount = int(stuff[2])
wickets = 0
turn = False
started = False
startingwicket = 0
mychoice = 1
botchoice = 1
won = False
draw = False
file.close
def main(a, b: int):
    global mypoints, botpoints, wincount, losscount, drawcount, wickets, turn, started, startingwicket, mychoice, botchoice, won, draw
    if a == "play" and b == 0:
        playframe.pack()
        mainframe.pack_forget()
    elif a == "stats" and b == 0:
        statsframe.pack()
        mainframe.pack_forget()
    elif a == "instructions" and b == 0:
        instructionframe.pack()
        mainframe.pack_forget()
    elif a == "main":
        try:
            instructionframe.pack_forget()
        except:
            pass
        try:
            statsframe.pack_forget()
        except:
            pass
        try:
            playframe.pack_forget()
        except:
            pass
        if b == 3:
            button_4_3.place(x=306, y=321)
            button_5_3.place(x=367, y=321)
            button_6_3.place(x=428, y=321)
            wickets = 0
            mypoints = 0
            botpoints = 0
            if started == True:
                losscount = losscount + 1
            update()
        mainframe.pack()
    elif a == "kill":
        save = open("config.txt", "w")
        save.write(str(wincount))
        save.write("\n")
        save.write(str(losscount))
        save.write("\n")
        save.write(str(drawcount))
        save.close()
        exit(1)
    elif a == "wicket":
        wickets = b
        startingwicket = b
        print(wickets)
        print(startingwicket)
        started = True
        button_4_3.place_forget()
        button_5_3.place_forget()
        button_6_3.place_forget()
        update()
    elif a == "point":
        if started != True:
            messagebox.showerror("Wickets", "Please select the amount of wickets first")
        else:
            choices = [1,2,3,4,5,6,10]
            botchoice = choice(choices)
            if botchoice != b:
                if turn == True:
                    botpoints = botpoints + botchoice
                    mychoice = b
                else:
                    if b == 1:
                        mypoints = mypoints + 1
                        mychoice = b
                    elif b == 2:
                        mypoints = mypoints + 2
                        mychoice = b
                    elif b == 3:
                        mypoints = mypoints + 3
                        mychoice = b
                    elif b == 4:
                        mypoints = mypoints + 4
                        mychoice = b
                    elif b == 5:
                        mypoints = mypoints + 5
                        mychoice = b
                    elif b == 6:
                        mypoints = mypoints + 6
                        mychoice = b
                    elif b == 10:
                        mypoints = mypoints + 10
                        mychoice = b
            else:
                wickets = wickets - 1
                if wickets == 0:
                    if turn == True:
                        if mypoints > botpoints:
                            wincount = wincount + 1
                            won = True
                        elif botpoints > mypoints:
                            losscount = losscount + 1
                            won = False
                        elif botpoints == mypoints:
                            drawcount = drawcount + 1
                            draw = True
                        started = False
                        print(wincount, losscount, drawcount)
                        if draw == True:
                            messagebox.showerror("Draw", "You drawed with the bot")
                        elif won == True:
                            messagebox.showinfo("Won", "You won with the bot")
                        else:
                            messagebox.showerror("Lost", "You lost to the bot")
                        playframe.pack_forget()
                        mainframe.pack()

                if turn == False and wickets == 0:
                    messagebox.showerror("Turn", "It is now the bot's turn")
                    wickets = startingwicket
                    turn = True
                    print(912)
                    
                
            update()
def update():
    global mypoints, botpoints, wincount, losscount, drawcount, wickets
    mypoints_.config(text=f"Your Points: {mypoints}")
    botpoints_.config(text=f"Bot's Points: {botpoints}")
    Wickets_.config(text=f"Wickets Left: {wickets}")
    losscount_.config(text=losscount)
    wincount_.config(text=wincount)
    drawcount_.config(text=drawcount)
    myturn.config(text=mychoice)
    botturn.config(text=botchoice)


def relative_to_assets(path: str, a: int) -> Path:
    if a == 0:
        return ASSETS_PATH0 / Path(path)
    elif a == 1:
        return ASSETS_PATH1 / Path(path)
    elif a == 2:
        return ASSETS_PATH2 / Path(path)
    elif a ==3:
        return ASSETS_PATH3 / Path(path)

window = Tk()
window.title("Odd or Even")
window.geometry("510x466")
window.configure(bg = "#00A3FF")
mainframe = Frame(window, bg="#00A3FF", width=510, height=466)
#MAINFRAME AKA LAUNCH FRAME
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png", 0))
image_1_0 = Label(
    image=image_image_1,
    relief="solid",
    bg="#00A3FF",
    borderwidth=0,
    master=mainframe
)
image_1_0.place(x=24, y=33)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png", 0))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("kill", 0),
    relief="solid",
    bg="#00A3FF",
    master=mainframe
)
button_1.place(
    x=140.0,
    y=386.0,
    width=229.0,
    height=57.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png", 0))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("stats", 0),
    relief="solid",
    bg="#00A3FF",
    master=mainframe
)
button_2.place(
    x=140.0,
    y=240.0,
    width=229.0,
    height=57.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png", 0))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("instructions", 0),
    relief="solid",
    bg="#00A3FF",
    master=mainframe
)
button_3.place(
    x=140.0,
    y=313.0,
    width=229.0,
    height=57.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png", 0))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("play", 0),
    relief="solid",
    bg="#00A3FF",
    master=mainframe
)
button_4.place(
    x=140.0,
    y=167.0,
    width=229.0,
    height=57.0
)
#####
#####
##### instructions page
instructionframe = Frame(window, bg="#00A3FF", width=510, height=466)
image_image_1_1 = PhotoImage(
    file=relative_to_assets("image_1.png", 1))
image_1_1 = Label(
    borderwidth = 0,
    relief="solid",
    bg="#00A3FF",
    master=instructionframe,
    image=image_image_1_1
)
image_1_1.place(x=2, y=0)
button_image_1_1_9 = PhotoImage(
    file=relative_to_assets("button_1.png", 1))
button_1_1_0 = Button(
    image=button_image_1_1_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("main", 131),
    relief="solid",
    bg="#00A3FF",
    master=instructionframe
)
button_1_1_0.place(
    x=351.0,
    y=407.0,
    width=146.0,
    height=47.0
)
##stats frame
statsframe = Frame(window, bg="#00A3FF", width=510, height=466)
image_image_1_2 = PhotoImage(
    file=relative_to_assets("image_1.png", 2))
image_1_2 = Label(
    relief="solid",
    bg="#00A3FF",
    master=statsframe,
    image=image_image_1_2,
    borderwidth = 0
)
image_1_2.place(x=32,y=17)
wincount_ = Label(
    text=wincount,
    borderwidth=0,
    bg="#FFFFFF",
    font=("IrishGrover Regular", 25 * -1),
    master=statsframe
)
wincount_.place(x=113,y=178)
losscount_ = Label(
    text = losscount,
    borderwidth = 0,
    bg="#FFFFFF",
    font=("IrishGrover Regular", 25 * -1),
    master=statsframe
)
losscount_.place(x=394, y=178)
drawcount_ = Label(
    text = drawcount,
    borderwidth = 0,
    bg="#FFFFFF",
    font=("IrishGrover Regular", 25 * -1),
    master=statsframe
)
button_image_1_2 = PhotoImage(
    file=relative_to_assets("button_1.png", 2))
button_1_2 = Button(
    image=button_image_1_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("main", 11),
    relief="solid",
    bg="#00A3FF",
    master=statsframe
)
button_1_2.place(
    x=356.0,
    y=411.0,
    width=146.0,
    height=47.0
)
drawcount_.place(x=247,y=348)

#PLAYING FRAME
playframe = Frame(window, bg="#00A3FF", width=510, height=466)
button_image_1_3 = PhotoImage(
    file=relative_to_assets("button_1.png", 3))
button_1_3 = Button(
    image=button_image_1_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("point", 1),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_1_3.place(
    x=24.0,
    y=272.0,
    width=48.0,
    height=48.0
)

button_image_2_3 = PhotoImage(
    file=relative_to_assets("button_2.png", 3))
button_2_3 = Button(
    image=button_image_2_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("point", 2),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_2_3.place(
    x=85.0,
    y=272.0,
    width=48.0,
    height=48.0
)

button_image_3_3 = PhotoImage(
    file=relative_to_assets("button_3.png", 3))
button_3_3 = Button(
    image=button_image_3_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("point", 3),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_3_3.place(
    x=146.0,
    y=272.0,
    width=48.0,
    height=48.0
)

button_image_4_3 = PhotoImage(
    file=relative_to_assets("button_4.png", 3))
button_4_3 = Button(
    image=button_image_4_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("wicket", 1),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_4_3.place(
    x=306.0,
    y=321.0,
    width=48.0,
    height=48.0
)

button_image_5_3 = PhotoImage(
    file=relative_to_assets("button_5.png", 3))
button_5_3 = Button(
    image=button_image_5_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("wicket", 2),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_5_3.place(
    x=367.0,
    y=321.0,
    width=48.0,
    height=48.0
)

button_image_6_3 = PhotoImage(
    file=relative_to_assets("button_6.png", 3))
button_6_3 = Button(
    image=button_image_6_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("wicket", 3),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_6_3.place(
    x=428.0,
    y=321.0,
    width=48.0,
    height=48.0
)

button_image_7_3 = PhotoImage(
    file=relative_to_assets("button_7.png", 3))
button_7_3 = Button(
    image=button_image_7_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("point", 6),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_7_3.place(
    x=146.0,
    y=330.0,
    width=48.0,
    height=48.0
)

button_image_8_3 = PhotoImage(
    file=relative_to_assets("button_8.png", 3))
button_8_3 = Button(
    image=button_image_8_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("point", 4),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_8_3.place(
    x=24.0,
    y=330.0,
    width=48.0,
    height=48.0
)

button_image_9_3 = PhotoImage(
    file=relative_to_assets("button_9.png", 3))
button_9_3 = Button(
    image=button_image_9_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("point", 5),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_9_3.place(
    x=85.0,
    y=330.0,
    width=48.0,
    height=48.0
)

button_image_10_3 = PhotoImage(
    file=relative_to_assets("button_10.png", 3))
button_10_3 = Button(
    image=button_image_10_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("point", 10),
    relief="solid",
    bg="#00A3FF",
    master = playframe
)
button_10_3.place(
    x=85.0,
    y=388.0,
    width=48.0,
    height=48.0
)
image_image_1_3 = PhotoImage(
    file=relative_to_assets("image_1.png", 3))
image_1_3 = Label(
    borderwidth= 0,
    relief="solid",
    bg="#00A3FF",
    image=image_image_1_3,
    master = playframe
)
image_1_3.place(x=24,y=63)
mypoints_ = Label(
    master= playframe,
    text=f"Your Point: {mypoints}",
    bg="#00A3FF",
    font=("IrishGrover Regular", 25 * -1)
)
mypoints_.place(x=23,y=33)
botpoints_ = Label(
    master=playframe,
    text=f"Bot’s Points : {botpoints}",
    bg="#00A3FF",
    font=("IrishGrover Regular", 25 * -1)
)
botpoints_.place(x=306,y=33)
Wickets_ = Label(
    master=playframe,
    text=f"Wickets Left: {wickets}",
    bg="#00A3FF",
    font=("IrishGrover Regular", 25 * -1)
)
Wickets_.place(x=319,y=284)
myturn =Label(
    master=playframe,
    text=mychoice,
    borderwidth=0,
    bg="#FFFFFF",
    relief="solid",
    font=("IrishGrover Regular", 25 * -1)
)
myturn.place(x=87,y=129)
botturn =Label(
    master=playframe,
    text=botchoice,
    borderwidth=0,
    bg="#FFFFFF",
    relief="solid",
    font=("IrishGrover Regular", 25 * -1)
)
botturn.place(x=368,y=129)
button_image_1_1 = PhotoImage(
    file=relative_to_assets("button_1.png", 1))
button_1_1_3 = Button(
    image=button_image_1_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main("main", 3  ),
    relief="solid",
    bg="#00A3FF",
    master=playframe
)
button_1_1_3.place(
    x=351.0,
    y=407.0,
    width=146.0,
    height=47.0
)
mainframe.pack()
window.resizable(False, False)
window.mainloop()

