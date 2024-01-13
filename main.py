from datetime import date, datetime

days_name = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Monday",
        6: "Monday",
    }



def name_users_birthday(name): # Розділення ім'я та прізвища 
    result = name.split()
    return result[0]

def get_birthdays_per_week(users):
    birthdays = {
        "Monday":[],
        "Tuesday":[],
        "Wednesday":[],
        "Thursday":[],
        "Friday":[],
        "Saturday":[],
        "Sunday":[],
    }
    if len(users) == 0:    
        return {}
    
    birthday_users = {}
    current_day = date.today()

    for i in users:
        new_birthday_date = i["birthday"]
        if new_birthday_date.year != current_day.year:
            year = current_day.year
            mouth = i["birthday"].month
            day = i["birthday"].day
            new_birthday_date = datetime(year=year+1, month=mouth, day=day).date()

        days_difference = new_birthday_date - current_day

        min_days = 0
        max_days = 6
        if current_day.weekday() == 6:
            min_days = -1
            max_days = 5
        elif current_day.weekday() == 0:
            min_days = -2
            max_days = 4

        if int(days_difference.days) >= min_days and int(days_difference.days) <= max_days :
            day_birthday_weekday = new_birthday_date.weekday()
            birthdays[days_name.get(day_birthday_weekday)].append(name_users_birthday(i["name"]))

    for day in range(0,7):
        date_b = days_name.get(day)
        if len(birthdays[date_b])!=0:
            birthday_users[date_b] = birthdays[date_b]

    return birthday_users

if __name__ == "__main__":
    users = [
        #{"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},

        {"name": "John Koum", "birthday": datetime(2023, 12, 21).date()},
        {"name": "Doe Koum", "birthday": datetime(2023, 12, 20).date()},
        {"name": "Alice Koum", "birthday": datetime(2024, 1, 1).date()},

    ]

    result = get_birthdays_per_week(users)
    print(result)
    
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")