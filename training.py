from datetime import date
users = [{'name': 'Андрій', 'birthday': date(year=2001, month=12, day=25)}, {
    'name': 'Фома', 'birthday': date(year=2002, month=8, day=26)}, 
    {'name': 'Петро', 'birthday': date(year=2003, month=9, day=27)}, 
    {'name': 'Василь', 'birthday': date(year=2004, month=10, day=28)}]
days_weeks = {0:'Понеділок', 1:'Вівторок',2:'Середа',3:'Четвер',4:"П'ятниця",5:'Субота',6:'Неділя'}
months_year_birthday = {0:'Січня', 1:'Лютого', 2:'Березня', 3:'Квітня', 4:'Травня',
 5:'Червня', 6:'Липня', 7:'Серпня', 8:'Вересня', 9:'Жовтня', 10:'Листопада', 11:'Грудня'}
months_year = {0: 'Січень', 1: 'Лютий', 2: 'Березень', 3: 'Квітень', 4: 'Травень',
5: 'Червень', 6: 'Липень', 7: 'Серпень', 8: 'Вересень', 9: 'Жовтень', 10: 'Листопад', 11: 'Грудень'}


#Загальний список юбілярів
def list_birthday():
    list_data = list()
    dict_months_jubilar = {}
    list_jubilar = list()
    for a in users:
        for key, value in a.items():
            if key == 'name':
                keyname = 'Колега'
                print(keyname,':',value)
                
            elif key == 'birthday':
                key = 'Дата народження'
                list_data = str(value).split('-')[::-1]
                for keydata, value in months_year_birthday.items():
                     if int(keydata) == int(list_data[1])-1:
                        month = months_year_birthday.get(keydata)
                print(key, ':', list_data[0] ,month, list_data[2], ' року')        
                if key == 'Дата народження':
                     print('________________________')    

def main():
    print('Введіть код потрібної операції, та натисніть "Enter": ')
    print('1- Вивести загальний список з датами народження')
    print('2- Вивести спискок юбілярів поточного тижня')
    chois =  input(' : ')
    if chois == '1':
        list_birthday()
    elif chois == '2':
        print('Функція в стадії розробки.')

main()
        

            

