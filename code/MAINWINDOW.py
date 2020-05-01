import sys
import csv

from myLib import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QTableWidgetItem, QMessageBox
from PyQt5 import QtGui

from loginTemplate import LoginPage
from homePageTemplate import MainWindow
from registerTemplate import RegisterPage
from addBookTemplate import AddBookPage

class HomeWindow(QMainWindow, MainWindow):

    def __init__(self, parent=None):
        super(HomeWindow, self).__init__(parent)
        self.setupUi(self)

        self.log = LoginWindow(self, self)
        self.log.show()

        self.sessionEmail = ""

        print("INITIATING DATA")
        #self.data = self.load_data()
        self.data = []

        self.tableBooks.cellChanged.connect(self.activateButtons)
        self.tableBooks.cellClicked.connect(self.activateRemoveButton)
        self.revertChangeButton.clicked.connect(self.revertChange)
        self.saveChangeButton.clicked.connect(self.saveChange)
        self.removeBookButton.clicked.connect(self.removeBook)
        self.addBookButton.clicked.connect(self.openAddBook)
        self.searchField.textChanged.connect(self.search)

    
    def load_data(self):
        print("LOADING DATA")
        dataList = []
        self.tableBooks.clearContents()
        # Here we read the db.csv file
        with open(f"{self.sessionEmail}_db.csv") as dataBase:
            file = csv.reader(dataBase, delimiter=",")
            for i, row in enumerate(file): # Gets all the rows, with index 0
                for j, col in enumerate(row):
                    dataList.append([i,j,col]) # Creates a data-matrix that can be edited later
                    self.tableBooks.setItem(i,j,QTableWidgetItem(col)) # Append to the table at index i, j
        self.data = dataList
        return self.data
    

    def activateButtons(self):
        self.revertChangeButton.setEnabled(True)
        self.saveChangeButton.setEnabled(True)
        try:
            self.tableBooks.item(self.tableBooks.currentRow(), self.tableBooks.currentColumn()).setBackground(QtGui.QColor(255, 249, 141))
        except:
            pass


    def revertChange(self):

        # Restart table using the self.data list
        self.tableBooks.clearContents()
        for cell in self.data:
            self.tableBooks.setItem(cell[0], cell[1], QTableWidgetItem(cell[2]))

        self.revertChangeButton.setEnabled(False)
        self.saveChangeButton.setEnabled(False)

        print("SUCCESSFULLY REVERTED CHANGES")

    def saveChange(self):

        # Get table data and save in self.data
        tempData = []
        for i in range(int(len(self.data)/8)):
            for j in range(self.tableBooks.columnCount()):
                try:
                    tempData.append([i,j,self.tableBooks.item(i,j).text()])
                except:
                    pass
        self.data = tempData
        
        
        # REMOVE BLANK ROWS IN DATA
        rowNum = 0
        for i in range(len(self.data)):
            self.data[i][0] = rowNum
            if self.data[i][1] == 7:
                rowNum += 1
        


        with open(f"{self.sessionEmail}_db.csv", "w") as dataBase:
            file = csv.writer(dataBase, delimiter=",")

            # Range the indexes of the rows
            for i in range(int(len(self.data)/8)):
                row = [] # Save the row to be stored as a list
                for j in self.data:
                    if j[0] == i: # Check if row matches
                        row.append(j[2]) # Append the data point to row
                #print("WRITING:", row)
                file.writerow(row)
        
        self.tableBooks.clearContents()
        for cell in self.data:
            self.tableBooks.setItem(cell[0], cell[1], QTableWidgetItem(cell[2]))
        
        self.revertChangeButton.setEnabled(False)
        self.saveChangeButton.setEnabled(False)

        print("SUCCESSFULLY SAVED CHANGES")


    def activateRemoveButton(self):
        self.removeBookButton.setEnabled(True)
    

    def removeBook(self):

        row = self.tableBooks.currentRow()

        self.tableBooks.clearContents()
        for cell in self.data:
            if cell[0] != row:
                self.tableBooks.setItem(cell[0], cell[1], QTableWidgetItem(cell[2]))

        self.revertChangeButton.setEnabled(True)
        self.saveChangeButton.setEnabled(True)
        self.removeBookButton.setEnabled(False)

        print("SUCCESSFULLY DELETED BOOK")


    def openAddBook(self):

        self.addB = AddBookWindow(self)
        self.addB.show()


    def search(self):

        print("SEARCHED", self.searchField.text())
        self.text = self.searchField.text().lower()

        self.filteredData = []

        
        for i in self.data:
            if self.text in i[2].lower(): # Checks to find a row with text
                # Stores entire row in filteredData
                row = i[0] 
                for j in self.data: # Loops through self.data and adds all items from that row
                    if j[0] == row:
                        self.filteredData.append(j)
        

        self.tableBooks.clearContents()

        for cell in self.filteredData:
            self.tableBooks.setItem(cell[0], cell[1], QTableWidgetItem(cell[2]))
            if self.text == "":
                if cell[0] % 2 != 0:
                    self.tableBooks.item(cell[0], cell[1]).setBackground(QtGui.QColor(244, 245, 245))
                else:
                    self.tableBooks.item(cell[0], cell[1]).setBackground(QtGui.QColor(255, 255, 255))
                
            else:
                self.tableBooks.item(cell[0], cell[1]).setBackground(QtGui.QColor(183, 227, 232))



class LoginWindow(LoginPage):
    def __init__(self, referenceMainWindow, parent=None): # referenceMainWindow -> home screen
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)

        self.exitButton.clicked.connect(self.exitApp)
        self.registerButton.clicked.connect(self.openRegister)
        self.loginButton.clicked.connect(self.try_login)

        self.homeWindow = referenceMainWindow # Creating an instance of the home window, to access methods

    def exitApp(self):
        sys.exit(0)

    def openRegister(self):
        self.reg = RegisterWindow(self)
        self.reg.show()

    def try_login(self):
        email = self.emailInput.text()
        password = self.passwordInput.text()
        with open("passwords.txt", "r") as passwordFile:
            for storedPassword in passwordFile:
                if verify_password(storedPassword, email + password):
                    print("CORRECT PASSWORD -----------------------------------------------")
                    self.close()

                    # Load data from specific user
                    self.homeWindow.sessionEmail = email
                    self.homeWindow.load_data()

                    return
            QMessageBox.about(self, "Error", "Error: Wrong password")
            self.emailInput.clear()
            self.passwordInput.clear()

class RegisterWindow(RegisterPage):
    def __init__(self, parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)

        self.registerButton.clicked.connect(self.try_register)
        self.exitButton.clicked.connect(self.close)

    def try_register(self):
        if self.validate_registration():
            self.store()

    def store(self):
        email = self.emailInput.text()
        password = self.passwordInput.text()
        print("hashing", email + password)
        msg = hash_password(email + password)
        with open("passwords.txt", "a") as output_file:
            output_file.write("{}\n".format(msg))
        self.close()

        with open(f"{email}_db.csv", "wb") as db:
            file = csv.writer(db, delimiter=",")

    def validate_registration(self):
        email = self.validate_email()
        username = self.validate_username()
        password = self.validate_password()
        return email and username and password

    def validate_email(self):
        email = self.emailInput.text()
        if "@" not in email:
            self.emailInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            self.warningEmail.setStyleSheet("color: red")
            return False
        self.emailInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        return True

    def validate_username(self):
        username = self.usernameInput.text()
        if username.isalpha() and len(username) > 5:
            self.usernameInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
            return True
        self.usernameInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
        self.warningUsername.setStyleSheet("color: red")
        return False

    def validate_password(self):
        password = self.passwordInput.text()
        password_c = self.verifyPasswordInput.text()
        if password != password_c or len(password) < 5:
            self.passwordInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            self.verifyPasswordInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            self.warningPassword.setStyleSheet("color: red")
            return False
        self.passwordInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        self.verifyPasswordInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        return True



class AddBookWindow(AddBookPage):
    def __init__(self, referenceMainWindow, parent=None):
        super(AddBookWindow, self).__init__(parent)
        self.setupUi(self)

        self.firstWindow = referenceMainWindow

        self.cancelButton.clicked.connect(self.close)
        self.addButton.clicked.connect(self.try_addBook)

    def try_addBook(self):
        if self.validateBookInputs():
            self.addBookToDB()

    def validateBookInputs(self):
        self.getInputText()
        correctInput = True

        # Title
        if self.title != "":
            self.titleInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        else:
            self.titleInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            correctInput = False

        # Author
        if self.author != "":
            self.authorInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        else:
            self.authorInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            correctInput = False

        # Editor
        if self.editor != "":
            self.editorInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        else:
            self.editorInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            correctInput = False

        # Continent
        if self.continent != "":
            self.continentInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        else:
            self.continentInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            correctInput = False

        # Cover Color
        if self.coverColor != "":
            self.coverColorInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        else:
            self.coverColorInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            correctInput = False

        # Nationality
        if self.nationality != "":
            self.nationalityInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        else:
            self.nationalityInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            correctInput = False

        # Publication date
        if self.publicationDate != "":
            print("publicationDate:", self.publicationDate)
            self.dateEdit.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        else:
            self.dateEdit.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            correctInput = False

        # Num of times read
        if self.numTimesRead != "":
            self.readInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
        else:
            self.readInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
            correctInput = False


        return correctInput
        

    def getInputText(self):
        self.title = self.titleInput.text()
        self.author = self.authorInput.text()
        self.editor = self.editorInput.text()
        self.continent = self.continentInput.text()
        self.coverColor = self.coverColorInput.text()
        self.nationality = self.nationalityInput.text()
        self.publicationDate = self.dateEdit.date().toPyDate()
        self.numTimesRead = self.readInput.text()

        self.allInputs = [self.title, self.author, self.editor, self.nationality, self.continent, self.publicationDate, self.coverColor, self.numTimesRead]


    def addBookToDB(self):
        with open(f"{self.firstWindow.sessionEmail}_db.csv", "a+") as dataBase:
            file = csv.writer(dataBase, delimiter=",")
            file.writerow(self.allInputs)

        self.firstWindow.data = self.firstWindow.load_data()
        self.close()


app = QApplication(sys.argv)
form = HomeWindow()
form.show()
app.exec_()


