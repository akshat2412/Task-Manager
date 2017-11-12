import pymysql
import datetime
from Day_Manipulation import getDay
from Notifications import Notification

db = pymysql.connect("localhost","root","root","task_manager" )
db_2 = pymysql.connect("localhost","root","root","task_manager" )
cursor = db.cursor()

date=getDay.date


prompt='''Please choose what would you like to do \n
1. View tasks for today \n
2. Add new task that you did today\n
3. View tasks for custom date \n
4. View tasks after custom days \n
5. Press 5 for quitting the program\n'''
# task="This is a test task"
# sql = "insert into schedule values('%s', '%s');"%(task, str(date))
# cursor.execute(sql)
# db.commit()
# db.close()

# if __name__=="main":
def addToDB(sql):
	global cursor
	global date
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print("There was an error")

def addTask():
	task=raw_input("\nDescribe your task: ")
	day_space=[1,4,13,33,66]
	for space in day_space:
		sql = "insert into schedule values('%s', '%s');"%(task, str(date+datetime.timedelta(days=space)))
		addToDB(sql)

	print("\n\n\n\n\n\n********************************************")
	print("\nSuccess! Your task has been added\n")
	print("********************************************\n\n\n\n\n\n\n")

def viewTasks(day):
	sql = "select Task from schedule where Due_on=('%s')"%(str(day))
	try: 
		cursor.execute(sql)
	except:
		print("Some error occured")
	else:

		task_list=cursor.fetchall()
		if len(task_list)==0:
			print("\n\n\n\n\n\n********************************************")
			print("No tasks for "+str(day))
			print("********************************************\n\n\n\n\n\n\n")
			return
		print("\n\n\n\n\n\n********************************************")
		print("Your tasks for "+str(day)+" are: \n")
		for task in task_list:
			print(task[0]+"\n")
		print("********************************************\n\n\n\n\n\n\n")
		
def viewReminders(day):
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

		Notification.show(task_list)


while(True):
	viewReminders(date)
	ans = raw_input("\n\n"+prompt+"\n"+"Your answer : ")
	if (ans==str(1)):
		viewReminders(date)
	if (ans==str(2)):
		addTask()
	if (ans==str(3)):
		day = raw_input("\n\nEnter the date in YYYY-MM-DD format: ")
		viewTasks(day)
	if (ans==str(4)):
		day = raw_input("\n\nAfter how many days: ")
		viewTasks(getDay.after(int(day)))
	if (ans==str(5)):
		break

db.close()
# ans = raw_input(prompt+"\n"+"Your answer : ")
# if (ans==str(2)):
# 	addTask()

