


class Productlinq():
    group: str
    type: str
    linq: str

    count = 0

    def __init__(self, group:str, type:str, linq:str):
        self.group = group
        self.type = type
        self.linq = linq
        Productlinq.count += 1

    def getAttr(self):
        return [self.group, self.type, self.linq]
    
    def __str__(self) -> str:
        return 'group: ' + self.group + ', type: ' + self.type + ', linq: ' + self.linq
