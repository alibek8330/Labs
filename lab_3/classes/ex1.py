class Action:
    def getString(self):
        return self.str

    def printString(self):
        newStr = self.str.upper()
        return newStr


string = Action()

print(string.printString())
