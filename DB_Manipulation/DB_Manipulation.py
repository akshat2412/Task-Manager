import pymysql
import datetime
from Day_Manipulation import getDay
# from Notifications import Notification
# from Reminder import Reminder

db = pymysql.connect("localhost","root","root","task_manager" )
# db_2 = pymysql.connect("localhost","root","root","task_manager" )
cursor = db.cursor()

date=getDay.date


def addToDB(db,task, date=date):
	sql = "insert into '%s' values('%s', '%s');"%(db,task, str(date))
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print("There was an error")


def addTask():
	task=raw_input("\nDescribe your task: ")
	day_space=[1,4,13,33,66]
	for space in day_space:
		date=str(date+datetime.timedelta(days=space))
		addToDB("schedule", task, date)

	print("\n\n\n\n\n\n********************************************")
	print("\nSuccess! Your task has been added\n")
	print("********************************************\n\n\n\n\n\n\n")

def addReminder():
	task=raw_input("\nDescribe your reminder: ")
	date=raw_input("\nDate of Reminder in YYYY-MM-DD format: ")
	if date == "":
		addToDB("reminders",task)
	else:
		addToDB("reminders",task, date)	
	print("\n\n\n\n\n\n********************************************")
	print("\nSuccess! Your task has been added\n")
	print("********************************************\n\n\n\n\n\n\n")

def closeDB():
	db.close()


def getTasks(day):
	sql = "select Task from schedule where Due_on=('%s')"%(str(day))
	try: 
		cursor.execute(sql)
	except:
		print("Some error occured")
	else:
		retrievedList=cursor.fetchall()
		
		task_list=list()
		
		for task in retrievedList:
			task_list.append(str(task[0]))

		return task_list
		
def getReminders(day):
	sql = "select Task from reminders where Due_on=('%s')"%(str(day))
	try: 
		cursor.execute(sql)
	except:
		print("Some error occured")
	else:
		retrievedList=cursor.fetchall()
		
		task_list=list()
		
		for task in retrievedList:
			task_list.append(str(task[0]))

		return task_list
