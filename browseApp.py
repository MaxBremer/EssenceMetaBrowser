from tkinter import *
import browser as bs
import random

class App:
    def __init__(self, master):
        self.frame = Frame(master, padx=5, pady=5, bg="#b6b6b6")
        self.frame.pack()

        self.groupInds = []

        self.lb = Listbox(self.frame)
        self.lb.pack(side=LEFT)

        self.group = Listbox(self.frame)
        self.group.pack(side=RIGHT)

        self.bAdd = Button(self.frame, text="Add to Group", command=self.addToGroup)
        self.bAdd.pack(side=TOP)
        self.bRemove = Button(self.frame, text="Remove from Group", command=self.removeFromGroup)
        self.bRemove.pack(side=TOP)
        self.bSel = Button(self.frame, text="Select", command=self.select)
        self.bSel.pack(side=BOTTOM)
        self.bRand = Button(self.frame, text="Random Choice", command=self.rand)
        self.bRand.pack(side=BOTTOM)

        self.eL = bs.EssenceList("es.txt")
        for e in self.eL.essenceList:
            self.addOpt(e.name)

        self.oframe = Frame(master, padx=10, pady=10, bg="#a6a6a6")
        self.oframe.pack(side=BOTTOM)
        self.output = Text(self.oframe)
        self.output.pack()

        self.oText = StringVar()


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
