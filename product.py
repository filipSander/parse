

class Product :
    group = ''
    type = ''
    mark = ''
    facturer = ''
    datasheet = '' 
    analogs = ''
    alldataSheet = ''

    def __init__(self, group, type, mark, facturer, datasheet, analogs, alldataSheet):
        self.group = group
        self.type = type
        self.mark = mark
        self.facturer = facturer
        self.datasheet = datasheet
        self.analogs = analogs
        self.alldataSheet = alldataSheet
    
    def getAttr(self):
        return [self.group, self.type, self.mark, self.facturer, self.datasheet, self.analogs, self.alldataSheet]
