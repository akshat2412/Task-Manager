db_2 = pymysql.connect("localhost","root","root","reminders" )
cursor_2 = db_2.cursor()

def set(task, date):
	sql="insert into reminders values('%s', '%s')"%(str(task),str(date))
	cursor_2.execute(sql)
	db_2.commit()

def viewFor(date):
	 sql="select Task from reminders where Date = ('%s')"%(str(date))
	 cursor_2.execute(sql)
	 db_2.commit()