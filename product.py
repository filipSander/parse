import json
from os import getcwd
import openpyxl 


class Product:
    group: str
    type: str
    mark: str
    facturer: str
    datasheet: str 
    analogs: str = []
    alldataSheet: str = ""

    count:int = 0

    def __init__(self, group:str, type:str, mark:str, facturer:str, datasheet:str):
        self.group = group
        self.type = type
        self.mark = mark
        self.facturer = facturer
        self.datasheet = datasheet
        Product.count += 1

    def __str__(self) -> str:
        return self.mark + " " + self.facturer

    def getAttr(self):
        analogsSTR = ''
        for a in self.analogs:
            analogsSTR += a + ' '
        return[ self.group, self.type, self.mark,self.facturer, self.datasheet, analogsSTR, self.alldataSheet]
        

