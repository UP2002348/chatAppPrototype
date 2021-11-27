import sqlite3
from sqlite3 import Error
import random


conn = sqlite3.connect('SquadChat.db')

c = conn.cursor()

def create_table():
	with conn:
		c.execute("""CREATE TABLE Manager (
				ManagerID VARCHAR(4) PRIMARY KEY,
				firstName text NOT NULL,
				surName	text NOT NULL,
				username text NOT NULL,
				email text NOT NULL,
				password text NOT NULL
				)""")

		

		c.execute("""CREATE TABLE Staff (
				StaffID VARCHAR(4) PRIMARY KEY,
				firstName text NOT NULL,
				surName	text NOT NULL,
				username text NOT NULL,
				email text NOT NULL,
				password text NOT NULL
				)""")
		c.execute("""CREATE TABLE Message(	
				MessageID VARCHAR(4) PRIMARY KEY,
				MessageFrom text NOT NULL,
				MessageTo text NOT NULL,
				messageFile text NOT NULL,
				timeSpent real NOT NULL,
				FOREIGN KEY (MessageFrom) REFERENCES staff (StaffID),
				FOREIGN KEY (MessageTo) REFERENCES staff (StaffID)
				)""")

		c.execute("""CREATE TABLE Task(
				TaskID VARCHAR(4) PRIMARY KEY,
				TaskCompleted text,
				TaskIncomplete text,
				TaskSetTo text NOT NULL
				TaskSetBy
				)""")
		

#create_table()


	

"""----manager----"""

def insertManager(managerID, first, surname, username, email, password):
	with conn:
		c.execute("INSERT INTO Manager VALUES (:managerID, :firstName, :surname, :username, :email, :password)", {'managerID': managerID, 'firstName': first, 'surname':surname,'username':username, 'email': email, 'password': password})

def select_manager(username):
	c.execute("SELECT * FROM Manager WHERE username = :username", {'username': username})
	return c.fetchall()

def select_all_manager():
	c.execute("SELECT * FROM Manager")
	return c.fetchall()



"""----staff----"""
def insertStaff(staffID, first, surname, username, email, password):
	with conn:
		c.execute("INSERT INTO Staff VALUES (:staffID, :firstName, :surname, :password, :email, :username)", {'staffID': staffID, 'firstName': first, 'surname':surname, 'password': password, 'email': email, 'username': username})

def select_staff(username):
	c.execute("SELECT * FROM Staff WHERE username = :username", {'username': username})
	return c.fetchall()

print(select_staff('3'))

def select_all_staff():
	c.execute("SELECT * FROM Staff")
	return c.fetchall()


def insertMessage(MessageID, MessageFrom, MessageTo, fileName, timeSpent):
	with conn:
		c.execute("INSERT INTO Message VALUES (:MessageID, :MessageFrom, :MessageTo, :fileName, :timeSpent)", {'MessageID': MessageID, 'MessageFrom': MessageFrom, 'MessageTo': MessageTo, 'fileName': fileName, 'timeSpent': timeSpent})


def select_messages():
	c.execute("SELECT MessageFrom, MessageTo From Message")
	return c.fetchall()

def select_messageFile(MessageFrom, MessageTo):
	c.execute("SELECT messageFile FROM Message WHERE MessageFrom = :MessageFrom and MessageTo = :MessageTo" , {'MessageFrom': MessageFrom, 'MessageTo': MessageTo})
	return c.fetchone()


print(select_messageFile(4269, 1)[0])

print(select_staff('Mehmetmazi')[0][0])

for index in select_all_staff()+select_all_manager():
	if 'brandonbiba' == index[3]:
		print('staff')
		

def generateID(newID):		
	if len(newID) < 4:					#This part checks if the id is 4 characters long
		newID += str(random.randint(1,9))#If its not a random number is generated and added to the string(string concatination)
		newID = generateID(newID)		#Then a recursion occurs until the id is 4 characters long
	return newID

print(generateID(str(random.randint(0,9))))

print(select_all_manager())
for i in select_all_staff():
	print(i[3])
	if '2' in i[3]:
		print('True')

#conn.close()

print(select_messages())