from tkinter import *

root = Tk()
root.title('TicTacToe')
ROW = 0
COLUMN = 0
Num = 0
INDEX = 0
OUT = 9 * ['a']
button = []
xscore = 0
oscore = 0
#Label(root, text='TicTacToe', bg='white', fg='black',padx=73).grid(row=0, column=0, columnspan=3)
e = Label(root, bg='white', fg='black',padx=60)
e.grid(row=3, column=0, columnspan=3)
lbl =Label(root,text='Scores X :0  O :0',bg='white',fg='black',padx=52)
lbl.grid(row=4,column=0,columnspan=3)


def Restart():
    global OUT
    for i in button:
        i.config(text='')
        OUT = 9 * ['a']


def buttonClick(buttonk):
    global Num
    global xscore
    global oscore
    global button
    global OUT

    if OUT[button.index(buttonk)] == 'X' or OUT[button.index(buttonk)] == 'O':
        e.config(text='INVALID')
        return
    elif Num % 2 == 0:
        buttonk.config(text='X')
        e.config(text='Player Os turn')
        OUT[button.index(buttonk)] = 'X'
        if (OUT[0] == 'X' and OUT[1] == 'X' and OUT[2] == 'X') or (
                OUT[0] == 'X' and OUT[3] == 'X' and OUT[6] == 'X') or ( \
                        OUT[0] == 'X' and OUT[4] == 'X' and OUT[8] == 'X') or (OUT[1] == 'X' and OUT[4] == 'X' and OUT[
            7] == 'X') or (OUT[3] == 'X' and OUT[4] == 'X' and OUT[5] == 'X') or (OUT[6] == 'X' and OUT[4] == 'X' and \
                                                                                  OUT[2] == 'X') or (
                OUT[2] == 'X' and OUT[5] == 'X' and OUT[8] == 'X') or (OUT[6] == 'X' and OUT[
            7] == 'X' and OUT[8] == 'X'):
            e.config(text='Player X wins')
            xscore += 1
            lbl.config(text="Scores X :{}  O :{}".format(xscore,oscore))
            Restart()

    else:
        buttonk.config(text='O')
        e.config(text='Player Xs turn')
        OUT[button.index(buttonk)] = 'O'
        if (OUT[0] == 'O' and OUT[1] == 'O' and OUT[2] == 'O') or (
                OUT[0] == 'O' and OUT[3] == 'O' and OUT[6] == 'O') or ( \
                        OUT[0] == 'O' and OUT[4] == 'O' and OUT[8] == 'O') or (OUT[1] == 'O' and OUT[4] == 'O' and OUT[
            7] == 'O') or (OUT[3] == 'O' and OUT[4] == 'O' and OUT[5] == 'O') or (OUT[6] == 'O' and OUT[4] == 'O' and \
                                                                                  OUT[2] == 'O') or (
                OUT[2] == 'O' and OUT[5] == 'O' and OUT[8] == 'O') or (OUT[6] == 'O' and OUT[
            7] == 'O' and OUT[8] == 'O'):
            e.config(text='Player O wins')
            oscore += 1
            lbl.config(text="Scores X :{}  O :{}".format(xscore, oscore))
            Restart()

    Num += 1


def createButton():
    global INDEX
    global ROW
    global COLUMN

    button.append(Button(root, text='', bg='white', fg='black', padx=25, pady=20,borderwidth=10))
    button[INDEX].grid(row=ROW, column=COLUMN)
    INDEX += 1

    COLUMN += 1
    if COLUMN == 3:
        COLUMN = 0
        ROW += 1


for i in range(9):
    createButton()
button[0].config(command=lambda: buttonClick(button[0]))
button[1].config(command=lambda: buttonClick(button[1]))
button[2].config(command=lambda: buttonClick(button[2]))
button[3].config(command=lambda: buttonClick(button[3]))
button[4].config(command=lambda: buttonClick(button[4]))
button[5].config(command=lambda: buttonClick(button[5]))
button[6].config(command=lambda: buttonClick(button[6]))
button[7].config(command=lambda: buttonClick(button[7]))
button[8].config(command=lambda: buttonClick(button[8]))
e.config(text='Player Xs turn')


mainloop()
