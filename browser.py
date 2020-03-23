from tkinter import *
import browseApp as ba

PREFIX_CONST = 15
U_PREFIX_CONST = 11

class Essence:
    def __init__(self, tname):
        self.name = tname
        self.description = ""
        self.genre = ""
        self.effs = []

    def addEff(self, eff):
        self.effs.append(eff)

    # NOTE: Optional
    def addDesc(self, desc):
        self.description = desc

    def addGenre(self, genre):
        self.genre = genre

    def toString(self):
        returner = "Essence of the " + self.name
        returner += "\nEffects of this essence are as follows:"
        for e in self.effs:
            returner += "\n" + e
        return returner

class EssenceList:
    def __init__(self, fname):
        self.essenceList = self.loadEssences(fname)
        self.numEssences = len(self.essenceList)

    def decodeName(self, nameLine):
        trueLine = ""
        if nameLine.lower().startswith("essence of the "):
            trueLine = nameLine[PREFIX_CONST:]
        else:
            trueLine = nameLine[U_PREFIX_CONST:]
        replacers = ['.', ':']
        for r in replacers:
            trueLine = trueLine.replace(r, "")
        trueLine = trueLine[0].upper() + trueLine[1:]
        if trueLine.find(' - ') == -1:
            return trueLine, ""
        else:
            pac = trueLine.split('-')
            return pac[0], pac[1]


    def startEssence(self, startingLine):
        name, desc = self.decodeName(startingLine)
        tempEssence = Essence(name)
        if len(desc) > 0:
            tempEssence.addDesc(desc)
        return tempEssence


    def parseEssence(self, strList):
        tempEssence = self.startEssence(strList[0])
        for d in strList[1:]:
            tempEssence.addEff(d)
        return tempEssence


    def loadEssences(self, fname):
        midEss = False
        curNormal = True
        essenceList = []
        file = open(fname, mode='r', encoding='utf8')
        curStrList = []
        curEssence = None
        for line in file:
            if line.startswith("Essence of "):
                if midEss:
                    thisEssence = self.parseEssence(curStrList)
                    essenceList.append(thisEssence)
                    curStrList = []
                else:
                    midEss = True
            if midEss:
                curStrList.append(line)

        if len(curStrList) > 0:
            essenceList.append(self.parseEssence(curStrList))
        return essenceList



if __name__ == "__main__":
    eL = EssenceList("es.txt")
    # print("NAMES:")
    # for e in eL.essenceList:
    #     print(e.name)
    # print("ESSENCES LOADED: ", str(len(eL.essenceList)))

    root = Tk()
    root.geometry("500x500")
    w = ba.App(root)

    #w.refresh()
    root.mainloop()
    #root.destroy()
