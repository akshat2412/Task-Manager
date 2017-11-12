import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify 
import sys
sys.path.insert(0, '/home/akshat/Desktop/Task_manager/DB_Manipulation')
from DB_Manipulation import DB_Manipulation

Notify.init("Task Notifier")

notificationHeading="Tasks for today are: "


notification=Notify.Notification.new(
	notificationHeading,
	"",
)


def showTasks(day=""):
	if day=="":
		task_list=DB_Manipulation.getTasks()
	else:
		task_list=DB_Manipulation.getTasks(day)

	if len(task_list) <= 0:
		return

	for i,task in zip(range(1, len(task_list)+1),task_list):
		tasks=tasks + str(i) + ". " + str(task) + "\n"

	notification.update(notificationHeading, tasks)
	notification.show()


def showReminders(day=""):
	if day=="":
		task_list=DB_Manipulation.getReminders()
	else:
		task_list=DB_Manipulation.getReminders(day)

	if len(task_list) <= 0:
		return

	for i,task in zip(range(1, len(task_list)+1),task_list):
		tasks=tasks + str(i) + ". " + str(task) + "\n"

	notification.update(notificationHeading, tasks)
	notification.show()

# summary = "Wake up!"
# body = "Meeting at 3PM!"
# notification = Notify.Notification.new(
#     summary,
#     body, # Optional
# )

# Actually show on screen
# notification.show()
