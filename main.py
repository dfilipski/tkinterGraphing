import tkinter

root = tkinter.Tk()
root.title("tkinterGraphing")
root.geometry("640x640")
root.resizable(0, 0)

#Create frame to display function imput
inputFrame = tkinter.Frame(height = 60, width = 640)
inputFrame.grid()

functionLabel = tkinter.Label(inputFrame, text = "Y1")
functionLabel.grid(row = 0)

functionEntry = tkinter.Entry(inputFrame)
functionEntry.grid(row = 0, column = 1)

graphBtn = tkinter.Button(inputFrame, text="Graph")
graphBtn.grid(row = 0, column = 2)

root.mainloop()