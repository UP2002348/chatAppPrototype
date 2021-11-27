from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QButtonGroup, QScrollArea, QGroupBox, QComboBox, QTabWidget, QVBoxLayout, QDialogButtonBox, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPainter, QBrush, QPen,QImage, QPalette, QImage
import sys
import random
import time, datetime
import re
import SquadChatDB
import clienttemp
import os



class Window(QWidget):#inheriting from the qtwidget class so it get the widgets such as QPushButton, etc...
	def __init__(self):
		super().__init__()
		#These attributes are the size of the window and the name of the window
		self.title = 'Login'
		self.top = 100
		self.left = 100
		self.width = 800
		self.height = 600

		self.InitWindow()#Allows the variable in this function to be instanciated

		

	def InitWindow(self):
		self.setWindowTitle(self.title)	#Assigns the window with the title attribute which was defined in the constructor
		self.setWindowIcon(QtGui.QIcon('squadchat.png')) #Puts the squadchat logo as the window icon
		self.setGeometry(self.top, self.left, self.width, self.height)#Sets the window size via the attrbutes in the constructor
		
		backImage = QImage('pamukkale.jpg')#selects the image for the background
		
		palette = QPalette()
		palette.setBrush(QPalette.Window, QBrush(backImage))#Draws the background

		self.setPalette(palette)

		font = QtGui.QFont()#Ive created a variable 'font' so I can make certain text look different
		font.setPointSize(20)#the size of the text
		font.setBold(True)#Makes the text bold
		font.setWeight(75)#varies the boldness of the text

		self.companyLogo = QtWidgets.QLabel(self) #A label which is going to display an image
		self.companyLogo.setPixmap(QtGui.QPixmap('Mehmet.png')) # The image I have selected
		self.companyLogo.setGeometry(325,40,150,250) # Where to put the image i selected
		self.companyLogo.setScaledContents(True) # makes the image not look squished or blurry as the image is being changed in size so this function maintains the quality of the image

		self.userinfo = QtWidgets.QLabel(self, text='Username')#I've creates a Label variable here so it can display 'username' 
		self.userinfo.move(230, 200)#this positions where I want the text to be displayed
		self.userinfo.setFont(QtGui.QFont('Arial', 13))# This sets the text to my desired type of font

		self.inputUsername = QtWidgets.QLineEdit(self, text='Mehmetmazi')#This gives the user the ability to input their username
		self.inputUsername.setFont(QtGui.QFont('Arial', 13))#sets the font of the text being inputted
		self.inputUsername.move(230, 230)#positions the text box
		self.inputUsername.resize(320,40)#Changes the size of the box 

		self.passwordinfo = QtWidgets.QLabel(self, text='Password')#Same process as the username 
		self.passwordinfo.setFont(QtGui.QFont('Arial', 13))
		self.passwordinfo.move(230, 280)

		self.inputPassword = QtWidgets.QLineEdit(self, text='Mehmetmazi')
		self.inputPassword.setFont(QtGui.QFont('Arial', 13))
		self.inputPassword.move(230, 310)
		self.inputPassword.resize(320, 40)
		self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)#This functions converts the inputted character into a bullet point
		

		self.unhidepwbox = QtWidgets.QCheckBox('Show Password', self)#This is a checkbox which allows the user to see their password 
		self.unhidepwbox.move(230,350)
		self.unhidepwbox.toggled.connect(self.hideshowpw)#Links the checkbox with the self.hideshowpw method


		self.staffbutton = QtWidgets.QRadioButton(self)#I used a radio button here so the user can select who they are 
		self.staffbutton.setChecked(False)			   #They can either sign in as a staff, manager or admin
		self.staffbutton.setText('staff')			   #Displays 'staff' next to the button
		self.staffbutton.value = 'staff'			   #This gives the staffbutton a value so the program identifies which radiobutton has been pressed	
		
		self.staffbutton.move(320, 370)				   #places the radio button at this location 

		self.managerbutton = QtWidgets.QRadioButton(self)#Same process as the 'staffbutton'
		self.managerbutton.setChecked(False)
		self.managerbutton.setText('manager')
		self.managerbutton.value = 'manager'
		
		self.managerbutton.move(400, 370)

		

		self.signinbutton = QtWidgets.QPushButton(self, text='Next')				#This button lets you go on the next screen 
		self.signinbutton.setStyleSheet("background-color: #2094ed; color: white")#However it will only let you go to the next screen if the username and password match with an entity in the database
		self.signinbutton.setFont(QtGui.QFont('Arial', 11))						
		self.signinbutton.move(450,400)
		self.signinbutton.clicked.connect(self.switchHomePage)#When pressed the button this method is called

		self.signupbutton = QtWidgets.QPushButton(self, text='Create account')#A create account button is displayed 
		self.signupbutton.resize(110,30)									  #in the login window if the user has not got an account
		self.signupbutton.setStyleSheet("""color: blue;	
										    border-style: outset;
										    font: bold 14px;
										    min-width: 10em;""")#This gives the button a design 
		self.signupbutton.setFont(QtGui.QFont('Arial', 8))
		self.signupbutton.move(200, 430)#positions the button
		self.signupbutton.clicked.connect(self.switchSignUpPage)#Links the button with switchSingUpPage method

		
		self.show()	#Displays the GUI

	def hideshowpw(self):#This runs when the checkbox for the password is clicked
		if self.unhidepwbox.isChecked() == True:#If the checkbox is ticked
			self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Normal)#The password inputted will be displayed 
		elif self.unhidepwbox.isChecked() == False:#If the checkbox is unticked
			self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)#The password inputted will be displayed with bullet points
	
	def paintEvent(self, e):#This function creates the white box in the middle of the screen to make the layout look nice

		painter = QPainter(self)
		painter.setPen(QPen(Qt.white, 10, Qt.SolidLine))#Creates the box in white
		painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))#Fills in the box with white
		painter.drawRect(200,110,400,350)#draws a rectangular shape


	def switchHomePage(self):
		'''if self.staffbutton.isChecked():
				print(self.staffbutton.value + ' is logged in')
			elif self.managerbutton.isChecked():
				print(self.managerbutton.value + ' is logged in')
			elif self.adminbutton.isChecked():
				print(self.adminbutton.value + ' is logged in')
			self.username = self.inputUsername.text()
			
			self.password = self.inputPassword.text()
			
			print(self.username)
			print(self.password)

			self.inputUsername.setText('')
			self.inputPassword.setText('')'''
		#Checks if the staff radio button is clicked
		if self.staffbutton.isChecked():
			for i in SquadChatDB.select_all_staff():
	#A for loop is executed so the username and password is checked in the database and they are compared against each other!"£"
				if self.inputUsername.text() == i[3] and self.inputPassword.text() == i[5]:
					self.staffDialog = StaffPage(self.inputUsername.text())
					self.staffDialog.show()
					self.hide()
		elif self.managerbutton.isChecked():#Remeber to change the manager homepage!!!
			for i in SquadChatDB.select_all_manager():
				if self.inputUsername.text() == i[3] and self.inputPassword.text() == i[5]:
					clienttemp.socket_connect(self.inputUsername.text())
					self.tabDialog = Tab(self.inputUsername.text())
					self.tabDialog.show()
					self.hide()

		self.inputUsername.setText('')
		self.inputPassword.setText('')

	def switchSignUpPage(self):#Switches to sign up page
		self.window2 = QtWidgets.QMainWindow()
		self.ui2 = Ui_signUpWindow()
		self.ui2.SignUpUI(self.window2)
		self.window2.show()
		self.close()

class Ui_signUpWindow(object):

	def SignUpUI(self, MainWindow):
		self.title = 'sign up'
		self.top = 100
		self.left = 100
		self.width = 800
		self.height = 600

		MainWindow.setWindowTitle(self.title)
		MainWindow.setGeometry(self.top, self.left, self.width, self.height)

		backImage = QImage('signupback.jpg')

		palette = QPalette()
		palette.setBrush(QPalette.Window, QBrush(backImage))#Draws the background

		MainWindow.setPalette(palette)

		font = QtGui.QFont()
		font.setPointSize(13)
		font.setBold(True)
		font.setWeight(75)

		self.FirstName = QtWidgets.QLabel(MainWindow, text='FirstName')
		self.FirstName.move(200, 70)
		self.FirstName.setFont(font)
		self.FirstName.setStyleSheet("color: white")

		self.FName = QtWidgets.QLineEdit(MainWindow)
		self.FName.setFont(QtGui.QFont('Arial', 13))
		self.FName.move(300,70)
		self.FName.resize(320, 35)

		self.LastName = QtWidgets.QLabel(MainWindow, text='LastName')
		self.LastName.move(200, 130)
		self.LastName.setFont(font)
		self.LastName.setStyleSheet("color: white")

		self.LName = QtWidgets.QLineEdit(MainWindow)
		self.LName.setFont(QtGui.QFont('Arial', 13))
		self.LName.move(300,130)
		self.LName.resize(320, 35)

		self.email = QtWidgets.QLabel(MainWindow, text='Email')
		self.email.move(220, 190)
		self.email.setFont(font)
		self.email.setStyleSheet("color: white")

		self.useremail = QtWidgets.QLineEdit(MainWindow)
		self.useremail.setFont(QtGui.QFont('Arial', 13))
		self.useremail.move(300,190)
		self.useremail.resize(320, 35)

		self.username = QtWidgets.QLabel(MainWindow, text='Username')
		self.username.resize(130, 15)
		self.username.move(200, 255)
		self.username.setFont(font)
		self.username.setStyleSheet("color: white")

		self.usernameInfo = QtWidgets.QLineEdit(MainWindow)
		self.usernameInfo.setFont(QtGui.QFont('Arial', 13))
		self.usernameInfo.move(300,250)
		self.usernameInfo.resize(320, 35)

		self.password = QtWidgets.QLabel(MainWindow, text='password')
		self.password.move(200, 305)
		self.password.setFont(font)
		self.password.setStyleSheet("color: white")

		self.passwordInfo = QtWidgets.QLineEdit(MainWindow)
		self.passwordInfo.setFont(font)
		self.passwordInfo.setEchoMode(QtWidgets.QLineEdit.Password)
		self.passwordInfo.move(300,305)
		self.passwordInfo.resize(320, 35)

		self.confirmPassword = QtWidgets.QLabel(MainWindow, text='ConfirmPassword')
		self.confirmPassword.resize(150,15)
		self.confirmPassword.move(140, 360)
		self.confirmPassword.setFont(font)
		self.confirmPassword.setStyleSheet("color: white")

		self.confirmPasswordInfo = QtWidgets.QLineEdit(MainWindow)
		self.confirmPasswordInfo.setFont(font)
		self.confirmPasswordInfo.setEchoMode(QtWidgets.QLineEdit.Password)
		self.confirmPasswordInfo.move(300,355)
		self.confirmPasswordInfo.resize(320, 35)

		self.unhidepwbox = QtWidgets.QCheckBox('Show Password', MainWindow)
		self.unhidepwbox.move(320,410)
		self.unhidepwbox.setStyleSheet("color: white")
		self.unhidepwbox.toggled.connect(self.hideshowpw)

		self.staffoption = QtWidgets.QRadioButton(MainWindow,text='Staff')
		self.staffoption.option = 'Staff'
		self.staffoption.setChecked(False)	
		self.staffoption.setFont(QtGui.QFont('Arial', 12))
		self.staffoption.setStyleSheet("color: white")
		self.staffoption.move(350,450)


		self.manageroption = QtWidgets.QRadioButton(MainWindow,text='Manager')
		self.manageroption.option = 'Manager'
		self.manageroption.setChecked(False)
		self.manageroption.setFont(QtGui.QFont('Arial', 12))
		self.manageroption.setStyleSheet("color: white")
		self.manageroption.move(450,450)

		self.createAccount = QtWidgets.QPushButton(MainWindow, text='Create Account')
		self.createAccount.move(380,500)
		self.createAccount.setStyleSheet("""color: white;
										    border-style: outset;
										    border-width: 2px;
										    border-radius: 10px;
										    border-color: beige;
										    font: bold 14px;
										    min-width: 10em;
										    padding: 6px;""")
		self.createAccount.clicked.connect(lambda: self.checkpassword(MainWindow))


	def hideshowpw(self):
		if self.unhidepwbox.isChecked() == True:
			self.passwordInfo.setEchoMode(QtWidgets.QLineEdit.Normal)
			self.confirmPasswordInfo.setEchoMode(QtWidgets.QLineEdit.Normal)
		elif self.unhidepwbox.isChecked() == False:
			self.passwordInfo.setEchoMode(QtWidgets.QLineEdit.Password)
			self.confirmPasswordInfo.setEchoMode(QtWidgets.QLineEdit.Password)

	def checkpassword(self, MainWindow):
		print(self.passwordInfo.text(), self.confirmPasswordInfo.text())
		passwordStrength = 0
		passwordValid = False
		invChar = False
		if self.FName.text() != '' and self.LName.text() != '' and self.useremail.text() != '' and self.usernameInfo.text() != '' and (self.staffoption.isChecked() or self.manageroption.isChecked()):
			if  len(self.passwordInfo.text()) >= 8 and len(self.passwordInfo.text()) <= 16:
				if self.passwordInfo.text() != self.confirmPasswordInfo.text():
					msg = QMessageBox()
					msg.setWindowTitle('Password invalid')
					msg.setText("Password does not match")
					msg.setStandardButtons(QMessageBox.Ok)
					x = msg.exec_()		
					self.passwordInfo.setText('')
					self.confirmPasswordInfo.setText('')
				else:	
					for letter in self.passwordInfo.text():
						if not re.search('[a-zA-Z0-9!"£$%^&*()_+=]', letter):
							self.show_popup()
							invChar = True
							self.passwordInfo.setText('')
							self.confirmPasswordInfo.setText('')
							break

					if not invChar:
						found = False
						if self.staffoption.isChecked():			    #If staff radiobutton is pressed then the program looks into  
							for row in SquadChatDB.select_all_staff():  #the staff table in the database
								if self.usernameInfo.text() in row[3]:	#It checks here each row if the username inputted is already used
									found = True						#if it is already taken then found is equaled to True 
									self.usernameused() 				#A pop message is displayed stating username already used
									
						elif self.manageroption.isChecked():			#Does the same thing with above(staffoption) but this time for the manager
							for row in SquadChatDB.select_all_manager():
								if self.usernameInfo.text() in row[3]:
									self.usernameused()
									found = True

						if found == False:							  #If the username inputted is not used the this statement is executed
							passwordValid = True					  
										
					if passwordValid and self.staffoption.isChecked():#If the above statement is executed and the staff button selected then
						for row in SquadChatDB.select_all_staff():	  #The program creates an ID for the new account
							ID = SquadChatDB.generateID(str(random.randint(0,9)))#The id is a random 4 digit number, which is made in the 
																				 #generateID function in the SquadChatDB module
							while ID in row[0]:						  #This looks if the ID is already used
								ID = SquadChatDB.generateID(str(random.randint(0,9)))#If it is then the generateID function is called again
																					 #Until a new ID is created within the Database

						SquadChatDB.insertStaff(ID, self.FName.text(), self.LName.text(), self.passwordInfo.text(), self.useremail.text(), self.usernameInfo.text())
						#Once the ID is created then the insertStaff function is executed which is in the SquadChatDB module
						self.ui = Window()#Finally the program redirects the user into the login page where they have to retype their 
										  #Username and password

					elif passwordValid and self.manageroption.isChecked():#Does the same thing with above(staffoption) but this time for the manager
						for row in SquadChatDB.select_all_manager():
							ID = SquadChatDB.generateID(str(random.randint(0,9)))
							while ID in row[0]:
								ID = SquadChatDB.generateID(str(random.randint(0,9)))

						SquadChatDB.insertManager(ID, self.FName.text(), self.LName.text(), self.usernameInfo.text(), self.useremail.text(), self.passwordInfo.text())
						self.ui = Window()
			else:
				self.show_popup()
		else:
			self.show_popup()
		self.passwordInfo.setText('')
		self.confirmPasswordInfo.setText('')
		
		#Here the database is inserting the required information into the database(so FirstName, Surname, etc.)		
	def usernameused(self):
		msg = QMessageBox()
		msg.setWindowTitle('Error')
		msg.setText('Username already used')
		msg.setStandardButtons(QMessageBox.Ok)
		msg.exec_()

	def show_popup(self):
		msg = QMessageBox()
		msg.setWindowTitle('Password invalid')
		msg.setText('The Password Has To Be Between 8 and 16, and must contain the following characters: a-z, A-Z, 0-9, !"£$%^&*()_+= \n All fields must be used*')
		msg.setStyleSheet('color: red;')
		msg.setStandardButtons(QMessageBox.Ok)
		x = msg.exec_()

class StaffPage(QDialog):
	def __init__(self, username):
		super().__init__()
		self.connects = clienttemp
		self.connects.socket_connect(username)

		self.top = 100
		self.left = 100
		self.width = 800
		self.height = 600

		self.setGeometry(self.top, self.left, self.width, self.height)
		

		self.setWindowTitle('Squadchat')




		vbox = QtWidgets.QVBoxLayout()
		tabWidget = QtWidgets.QTabWidget()

		logoutbutton = QtWidgets.QPushButton(text='Logout')
		logoutbutton.clicked.connect(self.logout)


		font = QtGui.QFont()#Ive created a variable 'font' so I can make certain some text look different
		font.setPointSize(20)#the size of the text
		font.setBold(True)#Makes the text bold
		font.setWeight(75)

		tabWidget1 = tabWidget.addTab(HomePage(), "Home Page")
		tabWidget.setStyleSheet("QTabBar::tab { height: 50px; width: 100px; font: bold;}")
		tabWidget2 = tabWidget.addTab(contacts(username), "Chats")
		tabWidget.setTabPosition(QTabWidget.South)

		
		vbox.addWidget(tabWidget)
		vbox.addWidget(logoutbutton)


		self.setLayout(vbox)

	def logout(self):
		self.close()#Closes the window, so logouts
		os.startfile('FullProgram.py')#re-runs the program

class HomePage(QWidget):
	def __init__(self):
		super().__init__()

		hbox = QHBoxLayout()

		groupBox = QtWidgets.QGroupBox("Coming Soon")

		mes = QtWidgets.QLabel(self, text='hello')

		another = QtWidgets.QPushButton(self, text='press me')
		another1 = QtWidgets.QPushButton(self, text='press me')

		hbox.addWidget(mes)
		hbox.addWidget(another)
		hbox.addWidget(another1)

		

		self.setLayout(hbox)
		

class contacts(QWidget):
	def __init__(self, username):
		super().__init__()
		self.username = username
		self.scrollArea = QScrollArea()
		self.Chatss = QtWidgets.QLabel(self)
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QWidget()
		self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
		self.names = {}
		self.buttongroup = QtWidgets.QButtonGroup()
		self.buttongroup.setExclusive(True)
		staffmanager = SquadChatDB.select_all_staff() + SquadChatDB.select_all_manager()
		self.staffID = SquadChatDB.select_staff(self.username)[0][0]

		for i in staffmanager:
		    self.names[i[3]] = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
		    self.names[i[3]].setText(i[3])
		    self.names[i[3]].setFont(QtGui.QFont('Arial', 20))

		    self.buttongroup.addButton(self.names[i[3]])
		    self.verticalLayout.addWidget(self.names[i[3]])
		self.buttongroup.buttonClicked.connect(self.buttonpressed)

		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		#self.scrollArea.setStyleSheet('background-color: red')
		mainLayout = QtWidgets.QVBoxLayout()
		mainLayout.addWidget(self.scrollArea)
		self.setLayout(mainLayout)
		self.hide()

	def buttonpressed(self, Contact):
		flag = False
		status = ''
		for index in SquadChatDB.select_all_staff():#Looks if the contact is a staff
			if Contact.text() == index[3]:
				status = SquadChatDB.select_staff(Contact.text())[0][0]
		if status == '':#If the contact is not a staff then they are a manager
			status = SquadChatDB.select_manager(Contact.text())[0][0]
			
		for x in SquadChatDB.select_messages():
#Here the program responds to the correspoding table, so if the user is messaging a manager the program will look if the user has previous
#messages with the manager, if they don't then a new file will be created and the messages will be saved in that file, if they are a staff
#vice versa
			if self.staffID in x and status in x:#
				flag = True
				print('found')
		#if there is no previous messages then a new a text file is created
		if flag == False:
			#the file name is named by their usernames
			fileName = self.username+Contact.text()+'.txt'
			with open(fileName, 'w'):
				pass#This just creates the file
			#Here a new record is created in the Message table in the database for the two clients  
			SquadChatDB.insertMessage(SquadChatDB.generateID(str(random.randint(0,9))), SquadChatDB.select_staff(self.username)[0][0], status, fileName, 0)

		
		#The chat window is opened when the user clicks on a contact
		self.ChatWindow = QtWidgets.QMainWindow()
		self.uiChat = ChatPage(self.ChatWindow, self.username, Contact.text(), status)
		



class Worker(QtCore.QObject):
    messagereceived = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.threadactive = True


    @QtCore.pyqtSlot()
    def run(self):
        global message
        while self.threadactive:
        # your logic here
            try:
                message = clienttemp.receiveMessages()
                if message:
                    self.messagereceived.emit(message)
            except Exception as e:
                print(e)


class ChatPage(object):
    

    def __init__(self, MainWindow, username, Contact, status):

        global message
        super().__init__()
        self.username = username
        self.Contact = Contact
        self.status = status
        self.fileName = SquadChatDB.select_messageFile(SquadChatDB.select_staff(self.username)[0][0], self.status)[0]

        self.worker = Worker()
        self.workerthread = QtCore.QThread()
        self.workerthread.started.connect(self.worker.run)
        self.worker.messagereceived.connect(lambda: self.messagereceived(message))

        self.worker.moveToThread(self.workerthread)
        self.workerthread.start()
        self.setupUi2(MainWindow)
        
        


    def setupUi2(self, MainWindow):
       
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(15)

        backImage = QImage('whatsapp.png')
        palette = QPalette()

        palette.setBrush(QPalette.Window, QBrush(backImage))
        MainWindow.setPalette(palette)
        
        self.timespent = datetime.datetime.now().minute # remember to add seconds as well

        self.ChatInput = QtWidgets.QTextEdit(MainWindow)
        self.ChatInput.setGeometry(QtCore.QRect(20, 490, 651, 71))

        font = QtGui.QFont()
        font.setPointSize(18)

        self.ChatInput.setFont(font)
        self.ChatInput.setObjectName("ChatInput")

        self.SendButton = QtWidgets.QPushButton(MainWindow)
        self.SendButton.setGeometry(QtCore.QRect(690, 500, 101, 51))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.SendButton.setFont(font)
        self.SendButton.setObjectName("SendButton")
        self.SendButton.clicked.connect(self.sendPressed)

        
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.move(350, 20)
        self.label.setStyleSheet('font: 13pt; border: 3px solid ;')
        #


        MainWindow.setWindowTitle("SquadChat")
        self.ChatInput.setHtml('Enter here')
        self.ChatInput.setStyleSheet("border: 1px solid; border-radius:10px; background-color: palette(base); ")
        self.SendButton.setText("Send")
        self.label.setText(self.Contact)


        self.displaytextagain(MainWindow)
        

        self.back = QtWidgets.QPushButton(MainWindow, text='Back')
        self.back.clicked.connect(lambda: self.backtocontact(MainWindow))
        self.f = open(self.fileName, 'a')

        MainWindow.show()
        

    def backtocontact(self, MainWindow):
    	self.timespent = datetime.datetime.now().minute - self.timespent
    	print(self.timespent)
    	self.f.close()
    	MainWindow.close()
    	

    def displaytextagain(self, MainWindow):
    	#The text file between the two clients are opened so the program van display the previous messages(history)
    	with open(self.fileName, 'r') as contents:
    		History = contents.read()

    	self.DisplayText = QtWidgets.QTextEdit(MainWindow)
    	self.DisplayText.setGeometry(QtCore.QRect(20, 70, 771, 381))
    	self.DisplayText.setObjectName("DisplayText")
    	self.DisplayText.setReadOnly(True)
    	self.DisplayText.setStyleSheet('color: black; background-image: url(whatsapp.png); background-color: white; font: 18pt; border: 0')
    	self.DisplayText.setText(History)

    def sendPressed(self):#When pressed the send button this method gets called

        message = self.ChatInput.toPlainText()
        self.DisplayText.append(f'{self.username}> {message}')
        clienttemp.sendMessage(self.Contact, message)
        self.ChatInput.setHtml('')
        self.f.write(message+'\n')
        

    def messagereceived(self, message):
        if message:
            self.DisplayText.append(message)
            try:
            	self.f.write(message+'\n')
            except ValueError:
            	pass
        else:
            pass

    
        

app = QtWidgets.QApplication(sys.argv)
window = Window()#opens the GUI "Window" page which is the login page
sys.exit(app.exec_())#this allows the user to close the application