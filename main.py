import tkinter
from tkinter import ttk

def getY1(x, constant):
#     xRange = { #Make this its own function later
#         1: 0,
#         2: 0,
#         3: 0,
#     }
    # for x in xRange:
    #     xRange[x] = num * x
    return constant*x

def getX1():
    return int(functionEntry.get())

def plot(x, y):
    x *= 5
    y *= 5
    x += 3
    plotY = 532 - y
    x2 = x + 5
    y2 = plotY - 5
    graphCanvas.create_line(x, plotY, x2, y2, fill="red")

def graphFunction(event):
    graphCanvas.delete("all")
    constant = getX1()
    for xCoord in range(1,107):
        plot(xCoord,getY1(xCoord, constant))
    # resultLabel["text"] = getY1(getX1())

root = tkinter.Tk()
root.title("tkinterGraphing")
root.geometry("640x640")
root.resizable(0, 0)

# Create frame to manage layout
frame = tkinter.Frame(root)
frame.pack(fill="both", expand=True) # tells the frame to expand to fill the root
frame.grid_columnconfigure(3, weight=1) # tells the grid layout that column 3 can expand to fill the frame
frame.grid_rowconfigure(5, weight=1) # tells the grid layout that row 5 can expand to fill the frame


functionLabel = tkinter.Label(frame, text = "Y1 = ")
functionLabel.grid(row = 0)

functionEntry = tkinter.Entry(frame, width = 2)
functionEntry.grid(row = 0, column = 1)

functionLabel = tkinter.Label(frame, text = "x")
functionLabel.grid(row = 0, column = 2)

graphBtn = tkinter.Button(frame, text="Graph")
graphBtn.grid(row = 2, pady=5)
graphBtn.bind("<Button-1>", graphFunction)

separator = tkinter.ttk.Separator(frame, orient="horizontal")
separator.grid(row = 3, columnspan = 4, sticky="ew", pady=5)

resultLabel = tkinter.Label(frame, text = "")
resultLabel.grid(row = 4, columnspan = 4, sticky="ew")

graphCanvas = tkinter.Canvas(frame, bg="white")
graphCanvas.grid(row = 5, columnspan=4, sticky="nsew", padx=4, pady=4)

root.mainloop()