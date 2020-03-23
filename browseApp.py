from tkinter import *
import tkinter.simpledialog
import tkinter.filedialog
import browser as bs
import random
from os import path
from os import mkdir

class App:
    def __init__(self, master):
        self.frame = Frame(master, padx=5, pady=5, bg="#b6b6b6")
        self.frame.pack()

        self.groupInds = []

        self.lb = Listbox(self.frame)
        self.lb.pack(side=LEFT)

        self.group = Listbox(self.frame)
        self.group.pack(side=RIGHT)

        self.buttonList = []
        self.addButton("Add to Group", self.addToGroup, TOP)
        self.addButton("Remove from Group", self.removeFromGroup, TOP)

        self.addButton("Save Group", self.saveGroup, TOP)
        self.addButton("Load Group", self.loadGroup, TOP)

        self.addButton("Select", self.select, BOTTOM)
        self.addButton("Random Choice", self.rand, BOTTOM)

        self.eL = bs.EssenceList("es.txt")
        for e in self.eL.essenceList:
            self.addOpt(e.name)

        self.oframe = Frame(master, padx=10, pady=10, bg="#a6a6a6")
        self.oframe.pack(side=BOTTOM)
        self.output = Text(self.oframe)
        self.output.pack()

        self.oText = StringVar()

        self.myPath = path.dirname(path.abspath(__file__))
        self.savesPath = path.join(self.myPath, "saves")

        if not path.exists(self.savesPath):
            mkdir(self.savesPath)


    def addButton(self, bText, bCommand, bSide):
        self.buttonList.append(Button(self.frame, text=bText, command=bCommand))
        self.buttonList[len(self.buttonList)-1].pack(side=bSide)

    def addOpt(self, opt):
        self.lb.insert(END, opt)
        #print("ADDED ", opt)

    def refresh(self):
        self.lb.pack(side=LEFT)

    def addToGroup(self):
        items = self.lb.curselection()
        selection = items[0]
        self.group.insert(END, self.eL.essenceList[selection].name)
        self.groupInds.append(selection)

    def removeFromGroup(self):
        items = self.group.curselection()
        if items:
            selection = items[0]
            self.group.delete(selection)
            self.groupInds.pop(selection)

    def saveGroup(self):
        fileStr = ""
        for gi in self.groupInds:
            fileStr += "|" + str(gi)
        fileStr = fileStr[1:]
        fileName = tkinter.simpledialog.askstring("File name", "Enter file name. Will be saved as '<file-name>.emg'.")
        fileName += ".emg"
        f = open(path.join(self.savesPath, fileName), 'w+')
        f.write(fileStr)
        f.close()

    def loadGroup(self):
        #fileName = tkinter.simpledialog.askstring("File name", "What file should be loaded?")
        fileName = tkinter.filedialog.askopenfilename(initialdir=self.savesPath, title="Select Group to be loaded")
        f = open(fileName, 'r')
        contents = f.read().split("|")
        self.group.delete(0, END)
        self.groupInds = []
        self.output.delete('1.0', END)
        for item in contents:
            ind = int(item)
            self.group.insert(END, self.eL.essenceList[ind].name)
            self.groupInds.append(ind)


    def select(self):
        items = self.lb.curselection()
        gItems = self.group.curselection()
        if items:
            selection = items[0]
            print("SELECTED ", selection)
            self.printChoice(selection)
        if gItems:
            selection = gItems[0]
            self.printChoice(self.groupInds[selection])

    def rand(self):
        choice = random.randint(0, self.eL.numEssences)
        print("SELECTED ", choice)
        self.printChoice(choice)

    def printChoice(self, ind):
        theText = self.eL.essenceList[ind].toString()
        self.oText.set(theText)
        #MESSAGE VERSION
        #self.output.configure(text=self.oText.get())
        #TEXT VERSION
        self.output.delete('1.0', END)
        self.output.insert(INSERT, theText)
