

class Product:
    group: str
    type: str
    mark: str
    facturer: str
    datasheet: str 
    analogs: str
    alldataSheet: str = ""

    count = 0

    def __init__(self, group:str, type:str, mark:str, facturer:str, datasheet:str, analogs:str):
        self.group = group
        self.type = type
        self.mark = mark
        self.facturer = facturer
        self.datasheet = datasheet
        self.analogs = analogs
        Product.count += 1


    def getAttr(self):
        return [self.group, self.type, self.mark, self.facturer, self.datasheet, self.analogs, self.alldataSheet]
