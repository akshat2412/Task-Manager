import pymysql
import datetime
from Day_Manipulation import getDay
from Notifications import Notification
import DB_Manipulation 

# db = pymysql.connect("localhost","root","root","task_manager" )
# db_2 = pymysql.connect("localhost","root","root","task_manager" )
# cursor = db.cursor()

date=getDay.date


prompt='''Please choose what would you like to do \n
1. View tasks for today \n
2. View reminders for today \n
3. Add new task that you did today\n
4. Add Reminders\n
5. View tasks for custom date \n
6. View Reminders for custom date \n
7. Press 7 for quitting the program\n'''
# task="This is a test task"
# sql = "insert into schedule values('%s', '%s');"%(task, str(date))
# cursor.execute(sql)
# db.commit()
# db.close()

# if __name__=="main":



while(True):
	# Notification.showReminders()
	# Notification.showTasks()

	ans = raw_input("\n\n"+prompt+"\n"+"Your answer : ")
	
	if (ans==str(1)):
		Notification.showTasks()

	if (ans==str(2)):
		Notification.showReminders()

	if (ans==str(3)):
		DB_Manipulation.addTask()

	if (ans==str(4)):
		DB_Manipulation.addReminder()

	if (ans==str(5)):
		day = raw_input("\n\nEnter the date in YYYY-MM-DD format: ")
		Notification.showTasks(day)

	if (ans==str(6)):
		day = raw_input("\n\nEnter the date in YYYY-MM-DD format: ")
		Notification.showReminders(day)

	if (ans==str(7)):
		DB_Manipulation.closeDB()
		break

# ans = raw_input(prompt+"\n"+"Your answer : ")
# if (ans==str(2)):
# 	addTask()

