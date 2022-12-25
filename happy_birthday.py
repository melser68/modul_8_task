from datetime import date, datetime, timedelta
users = [{'name': 'John', 'birthday': datetime(year=2001, month=12, day=29).date()}, {
    'name': 'Mike', 'birthday': datetime(year=2002, month=12, day=28).date()},
    {'name': 'Dilan', 'birthday': datetime(year=2003, month=12, day=26).date()},
    {'name': 'Robert', 'birthday': datetime(year=2004, month=12, day=27).date()}]


# Вираховуємо реквізити сьогоднішньої дати
today = datetime.today().date()
name_day_today = today.strftime('%A')
name_month_today = today.strftime('%B')
num_month_today = today.strftime('%m')
num_day_today = today.strftime('%w')
list_today = str(today).split('-')[::-1]

# Вираховуємо скільки днів додати до тижня аналізу юбілярів,
#  якщо сьогодні не неділя
if int(num_day_today) > 0:

    delta_time = 6 - int(num_day_today)
else:
    delta_time = 0

# Вираховуємо реквізити остатнього дня аналізу юбілярів
max_date_control = today + timedelta(7 + delta_time)
max_day_control = max_date_control.strftime('%A')
max_month_control = max_date_control.strftime('%B')
max_num_month_control = max_date_control.strftime('%m')
max_num_day_control = max_date_control.strftime('%w')
list_control = str(max_date_control).split('-')[::-1]

# Вираховуємо список днів аналізу
data_list = today - timedelta(days=1)
list_analiz = list()
while data_list < max_date_control:
    data_list = data_list + timedelta(days=1)
    list_analiz.append(data_list)


def get_birthdays_per_week():
    old_day = ''
    list_monday = list()
    list_tuesday = list()
    list_wednesday = list()
    list_thursday = list()
    list_friday = list()
    for i in users:
        for key, value in i.items():
            if key == 'name':
                name = value
            else:
                list_date = str(value).split('-')[::-1]
                list_date[2] = today.strftime('%Y')
                list_date.append(name)
                for i in range(len(list_date)):
                    if i == 0:
                        day = int(list_date[i])
                    elif i == 1:
                        month = int(list_date[i])
                    elif i == 2:
                        year = int(list_date[i])

                new_value = datetime(year=year, month=month, day=day).date()
                list_date.append(new_value)
                list_date.append(list_date[4].strftime('%A'))
                
                for r in range(len(list_date)):
                    for o in list_analiz:
                        
                        if list_date[r] == o:
                            if list_date[5] == 'Monday' or list_date[4].strftime('%w') == '5' or list_date[4].strftime('%w') == '6':
                                list_monday.append(list_date[3])
                            elif list_date[5] == 'Tuesday':
                                list_tuesday.append(list_date[3])
                            elif list_date[5] == 'Wednesday':
                                list_wednesday.append(list_date[3])
                            elif list_date[5] == 'Thursday':
                                list_thursday.append(list_date[3])
                            elif list_date[5] == 'Friday':
                                list_friday.append(list_date[3])
    if len(list_monday) >0:
        print('Monday: ', list_monday)
    if len(list_tuesday) > 0:
        print('Tuesday: ', list_tuesday)
    if len(list_wednesday) > 0:
        print('Wednesday: ', list_wednesday)
    if len(list_thursday) > 0:
        print('Thursday: ', list_thursday)
    if len(list_friday) > 0:
        print('Friday: ', list_friday)

              
                            


get_birthdays_per_week()
