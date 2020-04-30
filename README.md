# Unit 3

# Inventory project UNIT 3

## Contents
  1. [Planning](#planning)
  1. [Design](#design)
  1. [Development](#development)
  1. [Evaluation](#evaluation)
  1. [Improvements](#improvements)

Planning
---------------

### Identifying the client
The client is Christ Precieux (CP), a student attending UWC ISAK Japan. CP currently owns a collection of books, which are completely unorganised. All of his books have certain characteristics which he wants to document and categorise, such that it is easier for him to understand and be aware of his book collection at all times. Currently, there is no system in place to handle this organisation. The client wants to be able to keep track of the characteristics of books including:
* Title
* Authors
* Continent and nationality of author
* Editor
* Cover color
* Date of publication
* How many times the book has been read

The client also wants to be able to search for books based on the categories above. A search algorithm must be implemented, which quickly displays the most relevant results divided into each individual category, based on a given search term. 

No timeline has been given by the client. However, at this stage, as the developer, I have put an estimated completion date for **April 30th**. 

### Table of planning
This table shows completed and planned tasks which are of significant importance. This includes for example consultations with the client and development milestones:
| Task No | Planned Action                                      | Expected outcome                       | Time   | Target completion | Evidence        |
|---------|-----------------------------------------------------|----------------------------------------|--------|-------------------|-----------------|
| 1       | Planning: Meeting with client                       | Identify the client requirements       | 30 min | 12. Feb 2020      | Email exchange  |
| 2       | Development: Create a secure login system in Python | Finished login program                 | 20 min | 13. Feb 2020      | Program         |
| 3       | Planning: Confirming success criteria               | Confirm success criteria by the client | 10 min | 14. Feb 2020      | Voice recording |

### Explicit consultation with client (reference appendix)
See the link below to read the explicit consultation with the client. This section is located beneath the heading *"My role as a developer"*.

[Client Requirements and Design Brief](clientRequirementsAndDesignBrief.md)

The success criteria of the project was confirmed by the client on 14. Feb. Evidence of this discussion can be found through this voice recording of the interview:

[Confirming success criteria - An interview](successCriteria.m4a)


### Choose and justify a solution
My solution will be an **offline graphical user interface (GUI) software program built in Python**. Following are points explaining and justifying the main characteristics of my solution:
* Offline - It will be locally accessible on one computer/device, with no server/host interraction needed. I chose this because of the added security this entails, and because there is no need. Server requirement was not specified by client, thus there is no demand. 
* Graphical User Interface - The program will **not** be terminal based as used previously, but rather with a visual display. There will for example be buttons instead of commands, easier input of information (with text input fields) and graphical pictures of book covers etc. A simple but efficient user interface is a significant improvement of the usability of the program for the user, compared to a terminal-based program.
* Python - I will be building this project in Python. The reason for this is purely preferential, in addition to the requirement of the assignment. Python has libraries very suitable for GUI programs, in addition to very efficient and easy-to-use data handling techniques. This choice results in an easier job for me, the developer, in contrast to using other lower-level languages. However, an argument against this choice would be that the device running the program (the client) is required to have python 3.x and every library needed pre-installed. This is a clear disadvantage. However, as a developer with the knowledge of my clients hardware/software situation, I know that the receiving device (the computer which will run the program) has all of this already installed. 

**The program will have the following functionality:**
* Adding books
  * Creating a new book
  * Getting the information in the different categories through user input
* Removing books
  * Deleting a book
* Editing books
  * Changing information about a book
* Searching for books
  * Giving results based on an inputed search term
  * Separated and sorted based on the categories
  * Relevance is prioritised


### Criteria for success based on feedback

Success criteria in order of priority. These criterias have been consulted with and confirmed by the client.

* Secure login
* Register new users
  * Stores encrypted email, username and password
* Having categories for book characteristics
  * Title
  * Authors
  * Continent and nationality of author
  * Editor
  * Cover color
  * Date of publication
  * How many times the book has been read
* Adding books
  * Easy input within GUI
* Removing books
  * One-button click (with a yes/no confirmation)
* Editing books
  * Changing individual characteristics of books
* Editing and removing books can be reverted (cancelled)
* Search for a book
  * Displaying results in less than 1 sec
  * Intuitive display of results

### TELOS Principle

The feasibility report based on the TALOS principles can be found in the TELOS.md file.

It can be found here: 

[TELOS feasibility report](TELOS.md)

### System design diagram
Below is the system design diagram, including all the main components that will collectively become a working application. Each box is a separate window that the user interacts with through the buttons and input fields (outlined in the diagram). The databases are shown as well, and the single-lined arrows indicate the dataflow; what data is transferred and used where. Sme of the main processes, such as user authentication, revert, save, adding a book and search, are also included. This is only intended to represent a surface picture of the system. For detailed description of individual components, visit the [Design](#design) and [Development](#development) pages.


![systemDiagram](flowcharts/systemDiagram.png)



Design
---------------

### Early design and mocks
Early designs are important to get the clients feedback and for the developer to create an idea of the components required. Putting ideas down visually is crucial. Below is a very early sketch of the designs:
![designSketches](designSketches.png)


### Design of the UI
The design of the User Interface was created in the program QtDesigner, an application that assist in visualizing the components and layout of the PyQt5 python library. The program ensures that making dynamic and beautiful applications easier.

Multiple designs were required for my program, with the different windows outlined in the list below:
* Homescreen - overview over book collection and access to other pages (via buttons)
* Login page - user enters credentials and is either granted or refused access into the system (this is the first page the user encounters, because a login is always required)
* Register page - allows the user to add his/her personal details the first time the program is used
* Add book page - user can add a book
* Remove book page - user can remove a book
* Search page - user can sort through the collection to find a specific book using a keyword

It is also important to understand that the designing process is continous, which is especially something I've learned throughout this process. As can be seen below, the designs of the program went through an iterative process - refining the UI with every refresh. Below is the first version (the prototype) and the final version (finished product). It is crucial to note the differences, especially in regard to the aestetics. A much more pleasing visual interface leads to a more intuitive experience for the user. This is done by for example color coding, using green buttons for actions like save or login and red buttons for cancel and revert. A neutral background color keeps the design clean and focused. It is also important to note the consistency, the exact same RBG colors are ued throughout the entire program for every screen and button.

**All the designs are shown below, in the same order as mentioned above. Every page includes a picture of the protoype and final design.**

### Homescreen
The homescreen has 
* 1 title
* 1 main table with all the books 
* 4 buttons
  * Add book
  * Remove book
  * Revert changes
  * Save Changes
* 1 searchbar (for input)

<img src="designs/allBooksPage.png" width="500">

#### Reworked home page:

<img src="designs/NEWmainPage.png" width="500">

<br>

### Login Page
The login page has 
* One title 
* 2 input fields for 
  * Username 
  * Password
* 3 buttons
  * Login (Closes login window)
  * Register (Opens register window)
  * Exit (Closes entire application)


<img src="designs/loginPage.png" width="500">

#### Reworked login page:

<img src="designs/NEWloginPage.png" width="500">

<br>

### Register Page
The register page has
* 1 title
* 4 input fields for
  * Email
  * Username
  * Password
  * Verify password
* 2 buttons
  * Register (Validating and adding the user information to database)
  * Exit (Close the window)


<img src="designs/registerPage.png" width="500">

#### Reworked register page:

<img src="designs/NEWregisterPage.png" width="500">

<br>

### Add book Page
The add book page has
* 1 title and 1 subtitle
* 8 input fields
  * Title
  * Author
  * Editor
  * Continent
  * Cover color
  * Nationality
  * Publication date
  * Number of times read
* 2 buttons
  * Add the book (Validate input, add to database, close window)
  * Cancel (Close window)

<img src="designs/addBookPage.png" width="500">

#### Reworked Add Book page:

<img src="designs/NEWaddBookPage.png" width="500">

<br>



Development
---------------

### Secure login program
An essential part of the program, and the top priority on the success criteria list, is implementing a secure login method. As mentioned previously the client is the only one with access to this program, and therefore an encrypted and secure password lock is crucial. Below are the most important and relevant parts of the code needed to accomplish this, including explanations.

**Getting a password, and confirming it**
When signing up, the user picks a password. To ensure that no typos occured, the user must re-enter the password to verify it. 
```.py
confirmed = False
while not confirmed:
    password = input("Enter password: ")
    c_password = input("Confirm your password: ")
    confirmed = True if password == c_password else False
print("Password confirmed")
```
*Note the last line, in which a **Pythonic** practice is used - meaning - efficient compression of code into fewer lines. The boolean `confirmed` is only changed to true if the `if` statement is met. `Else`, it is not changed. The loop continues until the password is confirmed.*

**Encrypting the password string**
```.py
import os
import hashlib

salt = os.urandom(32) # this creates a 32 bytes
key = hashlib.pbkdf2_hmac("sha256", str(password).encode("utf-8"), salt, 1000)
```
To encrypt the password string both libraries `os` and `hashlib` must be imported.
`salt` is assigned as a string of size random bytes suitable for cryptographic use. More information can be found [here](https://www.geeksforgeeks.org/python-os-urandom-method/). In this example, the random string is 32 bytes.
`key` holds the encrypted password. The module `hashlib.pbkdf2_hmac()` is used with the secure hash algorithm SHA256. More information about this library and module can be found [here](https://docs.python.org/3/library/hashlib.html).

To display the encrypted password as a hexadecimal value, one must simply do as follows:
```.py
import binascii
print(binascii.hexlify(key))
```
The `binascii` library is capable of translating the key to hexadecimals.


### Logging a user in
To log a user in, the user must provide an email and password which will be checked against the database of user credentials. The database of user credentials is saved as `passwords.txt`, and includes all of the users' encrypted credentials.

The code is explained below:

1. The inputted email and password are stored
1. The `passwords.txt` file is opened and a for-loop iterates through the encrypted credentials
1. The `verify_password()` function is used to compare every stored password in the text file to the inputted `email + password`
1. If they are equal, the window closes (thus the user gains access to the main window) and they are logged in. The user's book database is loaded
1. If no credentials match, a pop-up is displayed showing an error message, and inputs are cleared

```.py
def try_login(self):
    email = self.emailInput.text()
    password = self.passwordInput.text()
    with open("passwords.txt", "r") as passwordFile:
        for storedPassword in passwordFile:
            if verify_password(storedPassword, email + password):
                self.close()

                # Load data from specific user
                self.homeWindow.sessionEmail = email
                self.homeWindow.load_data()

                return
        QMessageBox.about(self, "Error", "Error: Wrong password")
        self.emailInput.clear()
        self.passwordInput.clear()
```

The flowchart for this code can be seen below:
![tryLoginFlowchart](flowcharts/tryLoginFlowchart.png)


### Registering a user
Both when the user first starts the program and when new users want to create an account, the registration of login credentials are required. These variables are given by the user and outlined below, along with the necessary requirements and constraints on the inputs themselves
* Email
  * Must include a "@" to be confirmed as an email address
* Username
  * Must only be letters and have a length greater than 5
* Password
  * Must be greater than 5 characters and equal to the verification field below
* Verifying password
  * Another input of the password, to verify that the user knows his/her password. Both must be equal
  
**All 3 of these parameters (email, username and password) must be confirmed and within the requirements before the information is stored. **

However, the user is given more tries. When an input is wrong, the UI gives a visual response in the form of changing the color of the border of the input field. For example, in the method `validate_email()`:
```.py
if "@" not in email:
    self.emailInput.setStyleSheet("border: 1px solid red") # Changes the border
    return False
```
Similar tests and visual altercations are used for the other inputs.

The most important method in this process is `store()`. This method is shown below with explanations and information on its functionality.

1. The email and password from their separate input fields (referenced using the ID of the fields, `emailInput` and `passwordInput`) are collected and stored in variables.
1. The email and password are hashed (encrypted) together using the `hash_password` function. Both the email and password are passed in because the application will later check if the login information (an email and password) match the registration information. The combined hash is stored in the variable `msg`
1. All encrypted user credentials are stored in a text file named `passwords.txt`. That file is opened and the `msg` is written to a new line.
1. The registration window closes with the `self.close()` method
1. A database (for books) is created, with the name `{EMAIL}_db.csv` containing the user email


The full code is shown here:
```.py
email = self.emailInput.text()
password = self.passwordInput.text()
print("hashing", email + password) 
msg = hash_password(email + password) # Encrypting the password
with open("passwords.txt", "a") as output_file: # "a" - appending to a file
    output_file.write("{}\n".format(msg))
self.close() # Closing window

# CREATE DATABASE OF BOOKS
with open(f"{email}_db.csv", "wb") as db:
    file = csv.writer(db, delimiter=",")
```




### Integrating a Database
A key component of the book inventory system is that it stores information on each book. This has to be achieved through a database, such that the information can be kept between user sessions. While database solutions such as SQL and SQLite could be chosen, a more practical and lightweight solution will be suitable for such a small-scale project. Thus, a `.csv` file is used to store the data, which can be accessed through the `csv` library in python (`import csv`).

For every user, there is a separate database. This way, all the data remains individual and private. This separation of databases is done by creating a .csv database for every user upon registration. The databases are named using the user's email, in the format `USEREMAIL_db.csv`. Upon a successful login, the email of the user is saved in the variable `sessionEmail`. Thus, every time an interaction with the database is required, this user-specific file is accessed.

The data must be loaded into the table on the main page. Below is a code snippet showing how the data is stored for later use and how the table is filled out:
```.py
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
```
*Note: The `csv.reader()` method is essential here. It is important to note how this is used. While it returns a iterable (saved as `file`), this is not a list. It cannot be sliced using `[1:5]`, for example.*

The `enumerate(ITERABLE)` function returns both the iterable, combined with the index of that value. In `for i, row in enumerate(row):`, the index is stored in `i`, and the value in `row`.

#### Writing to the database
After changes to the table is made by the user, either by manually editing cells or by removing a book (an entire row), the option to save the current table data to the database must be an option. Many steps are involved in this process. These are outlined below.

Firstly, the `self.data` list must be updated with the edited table, because it is used later for writing to the database.
The codesnippet below retrieves the content of the table in each individual cell, and creates a data matrix in `self.data`.
```.py
# Get table data and save in self.data
    tempData = []
    for i in range(int(len(self.data)/8)):
        for j in range(self.tableBooks.columnCount()):
            try:
                tempData.append([i,j,self.tableBooks.item(i,j).text()])
            except:
                pass
    self.data = tempData
```
*Note 1: Here the `try` and `except` keywords are used. As mentioned in the comments, this is for the purpose of avoiding errors caused by empty cells (e.g. when a book is removed). The cells which are empty are not added to `tempData`*

*Note 2: In the first `for` loop, the range of `ìnt(len(self.data)/8)` is used. This is a simple way to get the row count. The length of the `self.data` list is always multiples of 8, since every row always includes 8 items.*

**Next, it is essential to adjust `self.data` to account for the missing rows.** This is for keeping the database clean and without blank lines (which leads to blank rows in the database). This is done by simply change the row values of the appropriate values of `self.data`. The code is shown below:
```.py
# REMOVE BLANK ROWS IN DATA
rowNum = 0
for i in range(len(self.data)):
    self.data[i][0] = rowNum
    if self.data[i][1] == 7:
        rowNum += 1
```
When the 8th column is reached (7th index), the program accounts for the row change as well by incrementing `rowNum` by 1.

The last part of this process in outlined in the flowchart below. The purpose is to save the data in the table to the .csv database.

![writeToDBflowchart](flowcharts/writeToDB.png)

The very last step is updating the table with the new information, done with:
```.py
self.tableBooks.clearContents() # Empty the table
for cell in self.data:
    self.tableBooks.setItem(cell[0], cell[1], QTableWidgetItem(cell[2])) # Inserts data into the cells
```

#### Adding a book
A core functionality of the system is giving the user the opportunity to add new books. This is needed to keep the inventory system up to date with the client's book collection. The process of appending a book to a database is fairly simple, following these steps:
1. Opening the add book window
1. Get the inputs from the user
1. Validate all inputs
1. If inputs are valid, append the information to the database
1. Close add book window
1. Update table on main window

There are 8 inputs, as mentioned in the design section (as a reminder, they are Title, Author, Editor, Continent, Cover color, Nationality, Publication date and Number of times read). Each one of these are validated. Being valid means not being left empty. This check is done as follows:
```.py
# Title
if self.title != "": # not empty
    self.titleInput.setStyleSheet("background-color: rgb(137, 255, 128); border: 1px solid green")
else: # empty
    self.titleInput.setStyleSheet("background-color: rgb(246, 156, 167); border: 1px solid red")
    correctInput = False
```
If the field is **not empty**, the `setStyleSheet()` method is used to change the field's border and fill color to green. 
If the field is **empty**, the field's border and fill color to red, and `correctInput` is set to `False`.

Finally, `correctInput` is returned. If one or more fields are invalid, the book will not be added.

However, in the case that all fields are valid, the `addBookToDB()` method is called. The code for this is below, with explanations following.
```.py
with open(f"{self.firstWindow.sessionEmail}_db.csv", "a+") as dataBase: # "a+" - append
    file = csv.writer(dataBase, delimiter=",")
    file.writerow(self.allInputs) # allInputs -> list of all inputs

self.firstWindow.data = self.firstWindow.load_data() # Reload data
self.close() # Close window
```
In this code snippet, step number 4, 5 and 6 are completed. The comments explain the functionality.


#### Searching for a book
The ability to search for a book becomes vital when the book collection grows. The search-algorithm I chose to use is fairly straight forward, and based upon the idea of filtering what is shown in the table. Thus, every search result is clearly distinguished with a color (light blue). The search is instant, and the table is updated in real-time. The code-snippet for the algorithm used and the corresponding flowchart is shown below:
```.py
self.text = self.searchField.text().lower() # Text is retrieved
self.filteredData = [] # New list is created every time text changes

for i in self.data:
    if self.text in i[2].lower(): # Checks to find a row with text
        # Stores entire row in filteredData
        row = i[0] 
        for j in self.data: # Loops through self.data and adds all items from that row
            if j[0] == row:
                self.filteredData.append(j)
```
*Note: Two for loops are used. The reason for this is that first loop is for checking if the value is in any cell. The second is for looping through the `self.data` list again and appending all the values with a row value equal to `row` to the `self.filteredData` list.*

The flowchart is as follows:
![searchFlowchart](flowcharts/searchFlowchart.png)

As can be seen, the table is updated after every change to the search inquiry. While the table is updated with the `self.filteredData` list, every cell than contains something (is in the `self.filteredData` list), changes color to blue. This is for better visualising the results. 






Evaluation
---------------




Improvements
---------------






