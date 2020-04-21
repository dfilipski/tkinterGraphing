import tkinter
from tkinter import ttk

def getY1(int):
    xRange = { #Make this its own function later
        1: 0,
        2: 0,
        3: 0,
    }
    for x in xRange:
        xRange[x] = int * x
    return xRange

def getX1():
    return int(functionEntry.get())

def graphFunction(event):
    resultMessage["text"] = getY1(getX1())


root = tkinter.Tk()
root.title("tkinterGraphing")
root.geometry("640x640")
root.resizable(0, 0)

#Create frame to display function imput
inputFrame = tkinter.Frame(height = 60, width = 640)
inputFrame.grid()

functionLabel = tkinter.Label(inputFrame, text = "Y1 = ")
functionLabel.grid(row = 0)

functionEntry = tkinter.Entry(inputFrame, width = 2)
functionEntry.grid(row = 0, column = 1)

functionLabel = tkinter.Label(inputFrame, text = "x")
functionLabel.grid(row = 0, column = 2)

graphBtn = tkinter.Button(inputFrame, text="Graph")
graphBtn.grid(row = 2)
graphBtn.bind("<Button-1>", graphFunction)

separator = tkinter.ttk.Separator(inputFrame, orient="horizontal")
separator.grid(row = 3, columnspan = 3, sticky="ew")

resultMessage = tkinter.Message(inputFrame, text = "")
resultMessage.grid(row = 4, columnspan = 3)

root.mainloop()