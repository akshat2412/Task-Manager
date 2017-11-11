import datetime

date=datetime.date.today()

def after(no_of_days):
	return str(date+datetime.timedelta(days=no_of_days))

def before(no_of_days):
	return str(date-datetime.timedelta(days=no_of_days))