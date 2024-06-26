# DOCUMENTATION
## STOCK AUTOMATIZATION
#### made by Naima Cavegn, Zachary Jenkins <br><br>

## PROJECT DESCRIPTION:
This repository is for an automation project of module 122 Bash. <br>
The assignment was as LB2 project work to create an automation with server and client.<br>
Everyone in the team should have their own customized code, but ideas and inspirations can be shared. <br>
It's an automation for stocks that tracks the increase and decrease of the stocks and updates them in certain time intervals.<br>
Users can enter their e-mail and receive the data from the stocks accordingly.<br>
The automation is useful for those who are interested in the market and stocks, as they are directly notified when something happens. 
All data is retrieved from an API and updated at certain frequency.<br>

## MILESTONES
A: We discussed the Projekt with our teacher and filled out the document with the "An forderungsdefinition". In a second step we created an UML  activity diagram. <br>
![image](https://github.com/naica922/Modul_122_Aktien/assets/150661049/d998ba72-3e48-4ea9-b3ba-16963a2ba9c3)
<br>
B: Implementation of the solution <br>
C: We've created this GitHub Repository with three branches. One for Zachary, one for Naima and the main branch. However, we had a little trouble working with the branches because we haven't done this before. However, we tried our best.

## PROJECT START AND END:
We started the project approximately on the 26.03.24 and had to work on it at school a total of 4 times. <br>
That's about 16 hours in altogether and the rest at home. <br>
The project was presented on 6.5.24 with a demo and the documentation.

## PROJECT RESULTS:
Our project checks the stocks from the API and updates them every several minutes.
It sends an Email to the hardcoded mail which you can use to test our codes.
If an error happens, you should get a response which helps you to fix it. <br>
Basically we are both content, but we could have used help from the teacher on some topics. Despite this, we implemented the project.

## TEAM:
Naima Cavegn and Zachary Jenkins
We basically wrote our code on our own, but we were allowed to support each other with questions and project development.

## DEADLINE:
The project deadline was May 6, when we also had to hand in our project.

## INSTALLATION:
To use our project yourself, you can use the following instructions with the data and set up the project locally. We did the project with a raspberry py<br>
We both created our own documentation for the setup which you can find in the branches zachary and naima.

# Starting the Project
To start the project you should be able to use a Rasberry Pi and connect to it through the cmd using ssh. Currently it doesn't work locally.

1. Prepare the Raspberry Pi
Install the OS: Ensure that your Raspberry Pi has Raspberry Pi OS  installed and is up to date. You can update the system with the following commands in the terminal:
```
sudo apt update
sudo apt upgrade
```

2. Install Python
Python Installation: Raspberry Pi OS comes with Python pre-installed, usually both Python 2 and Python 3. To check if Python is installed and determine its version, run:
```
sudo apt install python3
```
3. Transfer Your Script to the Raspberry Pi
Script Transfer: You can transfer your Python script to the Raspberry Pi using several methods:
SCP (Secure Copy Protocol): From your PC in the same network, you can use SCP to transfer files:
```
scp path/to/send_stock_email.py pi@raspberrypi.local:/home/pi/
```
FTP/SFTP: Use an FTP client like FileZilla to transfer files to /home/pi/.
Directly Editing on Pi: Use a text editor like nano on the Raspberry Pi to create and edit your script directly:
```
nano send_stock_email.py
```
4. Execute the Script
Execute the Script: Run your script on the Raspberry Pi:
```
python3 send_stock_email.py
```
5. Automate the Script (Optional)
Cron Job: If you want your script to run at regular intervals, set up a cron job:
```
crontab -e
```
Add a line to the crontab file to schedule your script:
```
*/10 * * * * python3 /home/pi/send_stock_email.py
```
This cron job runs the script every 10 minutes.

Step 5 shouldn't be needed since it is already automated in the code that it should be automated every 10 minutes.
