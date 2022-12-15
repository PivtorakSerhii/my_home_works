from datetime import datetime, timedelta
#тест от 15.12.22
test_users = [
    {"name": "Harry", "birthday": datetime(year=1990, month=12, day=10)},  #не выводит
    {"name": "Oliver", "birthday": datetime(year=1990, month=12, day=11)},   #не выводит
    {"name": "Jack", "birthday": datetime(year=1990, month=12, day=12)},   #не выводит
    {"name": "Charlie", "birthday": datetime(year=1990, month=12, day=13)},   #не выводит
    {"name": "Thomas", "birthday": datetime(year=1990, month=12, day=14)},    #не выводит
    {"name": "Jacob", "birthday": datetime(year=1990, month=12, day=15)},     #не выводит
    {"name": "Alfie", "birthday": datetime(year=1990, month=12, day=16)},     #не выводит
    {"name": "Riley", "birthday": datetime(year=1990, month=12, day=17)},     # Riley, William, James
    {"name": "William", "birthday": datetime(year=1990, month=12, day=18)},   # Riley, William, James
    {"name": "James", "birthday": datetime(year=1990, month=12, day=19)},     # Riley, William, James
    {"name": "Amelia", "birthday": datetime(year=1991, month=12, day=20)},  # Amelia
    {"name": "Olivia", "birthday": datetime(year=1991, month=12, day=21)},  # Olivia
    {"name": "Jessica", "birthday": datetime(year=1991, month=12, day=22)}, # Jessica
    {"name": "Emily", "birthday": datetime(year=1991, month=12, day=23)},   # Emily
    {"name": "Lily", "birthday": datetime(year=1991, month=12, day=26)},    #не выводит
    {"name": "Ava", "birthday": datetime(year=1991, month=12, day=27)},    #не выводит
    {"name": "Isabella", "birthday": datetime(year=1991, month=12, day=28)},#не выводит
    {"name": "Sophie", "birthday": datetime(year=1991, month=12, day=29)},  #не выводит
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
    elif 3 <= diff_next_week <= 6:
        return(bday.strftime('%A'))
    else:
        return("No result")

def print_user_list(week_bday):
    for key, value in week_bday.items():
        if value:
            print(f"{key}: {', '.join(value)}")

def get_birthdays_per_week(users: list):
    current_datetime = datetime.now() #datetime(year=2022, month=11, day=22)
    for name in users:
        bday = name["birthday"]
        bday_this_year = datetime(year=current_datetime.year, month=bday.month, day=bday.day)
        day_bday = week_control(bday_this_year, current_datetime)
        if day_bday == "No result":
            continue
        (week_bday[day_bday]).append(name["name"])
    print_user_list(week_bday)

if __name__ == "__main__":
    get_birthdays_per_week(test_users)