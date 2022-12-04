from datetime import datetime, timedelta
#тест от 04.12.22
test_users = [
    {"name": "Harry", "birthday": datetime(year=1990, month=12, day=1)},  #не выводит
    {"name": "Oliver", "birthday": datetime(year=1990, month=12, day=2)},   #не выводит
    {"name": "Jack", "birthday": datetime(year=1990, month=12, day=3)},   #Пн Jack Charlie Thomas
    {"name": "Charlie", "birthday": datetime(year=1990, month=12, day=4)},   #Пн Jack Charlie Thomas
    {"name": "Thomas", "birthday": datetime(year=1990, month=12, day=5)},    #Пн Jack Charlie Thomas
    {"name": "Jacob", "birthday": datetime(year=1990, month=12, day=6)},     #Вт Jacob James
    {"name": "Alfie", "birthday": datetime(year=1990, month=12, day=7)},     #Ср Alfie
    {"name": "Riley", "birthday": datetime(year=1990, month=12, day=8)},     #Чт Riley
    {"name": "William", "birthday": datetime(year=1990, month=12, day=9)},   #Пт William Isabella
    {"name": "James", "birthday": datetime(year=1990, month=12, day=6)},   #Вт Jacob James
    {"name": "Amelia", "birthday": datetime(year=1991, month=12, day=11)},  #не выводит
    {"name": "Olivia", "birthday": datetime(year=1991, month=12, day=12)},  #не выводит
    {"name": "Jessica", "birthday": datetime(year=1991, month=12, day=13)}, #не выводит
    {"name": "Emily", "birthday": datetime(year=1991, month=12, day=14)},   #не выводит
    {"name": "Lily", "birthday": datetime(year=1991, month=12, day=15)},    #не выводит
    {"name": "Ava", "birthday": datetime(year=1991, month=12, day=16)},    #не выводит
    {"name": "Isabella", "birthday": datetime(year=1991, month=12, day=9)},#Пт William Isabella
    {"name": "Sophie", "birthday": datetime(year=1991, month=12, day=18)},  #не выводит
]
week_bday = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
}

def week_control(bday, current_datetime):
    diff_day = 5 - abs(current_datetime.weekday()+1)
    next_week_Sat = current_datetime + timedelta(days=diff_day)
    diff_next_week = (bday - next_week_Sat).days
    if 0 <= diff_next_week <= 2:
        return("Monday")
    elif diff_next_week == 3:
        return("Tuesday")
    elif diff_next_week == 4:
        return("Wednesday")
    elif diff_next_week == 5:
        return("Thursday")
    elif diff_next_week == 6:
        return("Friday")
    else:
        return("No result")

def user_list(week_bday):
    for key, value in week_bday.items():
        if value:
            print(f"{key}: {', '.join(value)}")

def get_day_birthdays(users: list):
    current_datetime = datetime.now()
    for name in users:
        b_day = name["birthday"]
        b_day_this_year = datetime(year=current_datetime.year, month=b_day.month, day=b_day.day)
        day_happy = week_control(b_day_this_year, current_datetime)
        if day_happy == "No result":
            continue
        (week_bday[day_happy]).append(name["name"])
    user_list(week_bday)

if __name__ == "__main__":
    get_day_birthdays(test_users)