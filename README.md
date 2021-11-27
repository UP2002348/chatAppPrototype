## About
I made this app for my final year project for A-levels. The main feature of this app is for messaging amongst a team within a business. Managers have certain features that staff do not have. The app aims to improve productivity levels of a business by cutting/lowering any unnecessary activity that happens in a business by integrating some face-to-face events to be executed on the app, as well as store data of staff activity, in order to give a more accurate feedback to staff by their seniors. This is what segregates my app design from other popular apps such as slack or microsoft teams.

## Built with
So far this app is built on a local network system, however with a few adjustments this could be easily live and running at any business. Nevertheless, the core technologies used for this app is:
* Python
* PyQt
* SQLite

## getting started
* `pip install -r requirements.txt` installs the required modules and files.
* In the `server.py` file manually change the port number to own ideal port. 
* In the `clienttemp.py` file change the port number to the number you put in `server.py` file. Also change the HOST variable to servers IP Address.
* Open the `FullProgram.py` file to start the application.

## Features
* Users can create an account and automatically have the capability to message any staff without having to add them. Users could also quickly change their details directly from their accounts instead of manually disturbing the managers to get things changed.
* Users that has an account status of "Staff" are monitored by Managers on things like, how many tasks they have completed, how long they spent on the app, how long they spent messaging, etc.
* Managers could easily assign tasks to staff directly from their user panel instantly.
* Users and managers could make noted and reminders for themselves.

## Complications/Improvements
As mentioned in the "built with" section, there are some minor issues that could be easily updated:
* Servers IP address could change and therefore each time clienttemp.py file needs to be manually updated. This will be updated soon.
* Files are currently not modularised properly. Modularisation needs to be implemented for easier maintenance.
* Improved Graphical User Interface.
* Users have the ability to create accounts however this should be managed by the business/admin rather than every user.
* database needs to be migrated from SQLight3 to a different db such as PostrgeSQL, as SQLight has scalability complications and doesn't support concurrency. 
