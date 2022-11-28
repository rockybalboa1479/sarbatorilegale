from datetime import datetime
import calendar

def get_date():
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    return currentMonth, currentYear

def get_calendar():
    mm, yy = get_date()
    
    return calendar.month(yy, mm)

print(get_calendar().split("\n"))