# Unit 3

# Inventory project UNIT 3

## Criteria A - Planning

### Identifying the client
The client is Christ Precieux (CP), a student attending UWC ISAK Japan. CP currently owns a collection of books, which are completely unorganised. All of his books have certain characteristics which he wants to document and categorise, such that it is easier for him to understand and be aware of his book collection at all times. At this time, there is no system in place to handle this organisation. The client wants to be able to keep track of the characteristics of books including:
* Title
* Authors
* Continent and nationality of author
* Editor
* Cover color
* Date of publication
* How many times the book has been read

No timeline has been given by the client. However, at this stage, as the developer, I have put an estimated completion date for **March 20th**. 

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


### Comprehensive criteria for success based on feedback

Success criteria in order of priority. These criterias have been consulted with and confirmed by the client.

* Secure login
  * Custom username
  * Encrypted password
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
  * One-button click
* Search for a book
  * Displaying results in less than 1 sec
  * Results in each category
  * Intuitive display of results (most important and relevant first)
    * Prioritizes Titles, authors
    * Displays most frequently read first

### TELOS Principle
TELOS is an essential fundamental principle within project management for which the feasibility of the project can be assessed. TELOS is an acronym for **T**echnical, **E**conomic, **L**egal, **O**perational and **S**cheduling. These 5 aspects are outlined and assessed below:

1. **T**echnical - The technical aspect of this project is very feasible. There is no new needed technology to create this program, as both the developer and client have the appropriate computers for this process. There will be no need for new hires to create this, with me being the only needed developer to create a finished product. A techincal concern could be the the compatibility of the program with the computer running the software (considering the Python version and packages installed). As mentioned in the justification, however, this is not a challenge because the device which will run the program already has this pre-installed.
1. **E**conomic - There are no economic limitations on this project. It requires no funding, either for development (software, hardware etc.) or hiring of new developers. As a developer I am doing this for free. The economic concerns can therefore be regarded, and in this regard the project is very feasible.
1. **L**egal - There are no legal considerations either. Such a small scale private project with no salary has no legal implications.
1. **O**perational - The operational feasibility of the project includes the consideration of implementation of the program and training of the user/client for using the new software. The implementation of the program simply requires an installation on the clients desired device. Whether this will be over the air (online download) or manual (USB drive) will be determined when the program is finished, and based on the clients wants and needs.
1. **S**cheduling - The timeline of this project is yet to be determined. An estimation of completion of the project can be set to March 20th. However, this is very uncertain and will be subject to change as a more clear deadline is identified (f.ex. from client/teacher)


## Development

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


## Evalutation

## Improvements






