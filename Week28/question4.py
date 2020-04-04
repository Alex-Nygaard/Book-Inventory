class StringProcessing():
    def __init__(self):
        pass

    def getString(self):
        self.string = input("Please enter a string: ")
    
    def printString(self):
        print(self.string.upper())


testingString = StringProcessing()

testingString.getString()
testingString.printString()
