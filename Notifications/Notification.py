import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify 

Notify.init("Task Notifier")

notificationHeading="Tasks for today are: "

notification=Notify.Notification.new(
	notificationHeading,
	"",
)
def show(task_list):
	tasks = ""
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
