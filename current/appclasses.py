import requests
import subprocess
import webbrowser

class website:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    
    @name.setter
    def name(self, sname):
        self.__name = sname
    

    def check(self):
        try:
            requests.get("www." + self.name)
        except:
            raise Exception

    def start(self):
        try:
            webbrowser.open("www." + self.name)
        except:
            raise Exception


class program:
    def __init__(self, path):
        self.path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, spath):
        self.__path = spath

    def start(self):
        subprocess.call([self.path])

def getPrograms(): 
    programDictionary = {}
    paths = open("apppaths.txt", "r")
    for PCF in paths:
        PCFs = PCF.split("=")
        programDictionary[PCFs[0]] = program(PCFs[1])
    return programDictionary

def getSites():
    siteDictionary = {}
    names = open("websites.txt", "r")
    for WCF in names:
        WCFs = WCF.split("=")
        siteDictionary[WCFs[0]] = website(WCFs[1])
    return siteDictionary

def getAll():
    Dictionary = {}
    paths = open("apppaths.txt", "r")
    wnames = open("websites.txt", "r")
    for PCF in paths:
        PCFs = PCF.split("=")
        Dictionary[PCFs[0]] = program(PCFs[1])
    for WCF in wnames:
        WCFs = WCF.split("=")
        Dictionary[WCFs[0]] = website(WCFs[1])
    return Dictionary