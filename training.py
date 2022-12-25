from datetime import  date, datetime, timedelta
users = [{'name': 'Андрій', 'birthday': datetime(year=2001, month=12, day=25).date()}, {
    'name': 'Фома', 'birthday': datetime(year=2002, month=8, day=26).date()}, 
    {'name': 'Василь', 'birthday': datetime(year=2003, month=12, day=26).date()}, 
    {'name': 'Петро', 'birthday': datetime(year=2004, month=12, day=27).date()}]
days_weeks = {0:'Понеділок', 1:'Вівторок',2:'Середа',3:'Четвер',4:"П'ятниця",5:'Субота',6:'Неділя'}
months_year_birthday = {0:'Січня', 1:'Лютого', 2:'Березня', 3:'Квітня', 4:'Травня',
 5:'Червня', 6:'Липня', 7:'Серпня', 8:'Вересня', 9:'Жовтня', 10:'Листопада', 11:'Грудня'}
months_year = {0: 'Січень', 1: 'Лютий', 2: 'Березень', 3: 'Квітень', 4: 'Травень',
5: 'Червень', 6: 'Липень', 7: 'Серпень', 8: 'Вересень', 9: 'Жовтень', 10: 'Листопад', 11: 'Грудень'}


#Загальний список юбілярів
def list_birthday():    
    for a in users:
        for key, valuename in a.items():
            if key == 'name':
                keyname = 'Колега'
                print(keyname,':',valuename)
                                
            elif key == 'birthday':
                key = 'Дата народження'
                list_data = str(valuename).split('-')[::-1]
                for keydata, value in months_year_birthday.items():
                     if keydata == int(list_data[1])-1:
                        month = months_year_birthday.get(keydata)                                               
                print(key, ':', list_data[0] ,month, list_data[2], ' року')               
                if key == 'Дата народження':
                     print('________________________')    


def weekly_jubilars():
    today = datetime.now().date()
    
    if today.weekday() > 0:
        day_delta = today + timedelta(days=(6+ (7-today.weekday())))
    else:
        day_delta = timedelta(days=7)  
    list_today = str(today).split('-')[::-1]
    
    list_day_delta = str(day_delta).split('-')[::-1]
    list_name= list()
    global list_weekly
    list_weekly = list()   
    day_birth = True
        
    for i in users:      
        
        for a , b in i.items():
            
            if a == 'birthday':
                a = 'Дата народження'
                list_data = str(b).split('-')[::-1]
                for keydata, value in months_year_birthday.items():
                    if keydata == int(list_data[1])-1:
                        month = months_year_birthday.get(keydata)
                rez = a+ ' : '+ list_data[0]+ ' '+month+ ' '+list_data[2]+ ' року'
                list_data = str(b).split('-')[::-1]                
                if int(list_day_delta[2]) > int(list_today[2]):
                    list_day_delta[2] = list_today[2]
                    list_day_delta[1] = '12'
                    list_day_delta[0] = '31'                
                if int(list_data[0]) >= int(list_today[0]) and int(list_data[0]) <= int(list_day_delta[0]) and int(list_data[1]) == int(list_today[1]):
                    list_name.append(rez)
                    date_today = str(today).split('-')
                    date_custom = str(b).split('-')
                    date_custom[0] = date_today[0]
                    
                    for z in range(len(date_custom)):
                        if z == 0:
                            year_1 = int(date_custom[z])
                        elif z ==1:
                            month_1 = int(date_custom[z])
                        elif z ==2:
                            day_1 = int(date_custom[z])
                    b = datetime(year=year_1, month=month_1, day=day_1)                    
                    list_weekly.append(str(b.weekday()))
                    
                    day_birth = True 
                else:
                    day_birth = False                             
                    
                
            elif a == 'name': 
                if day_birth == True:
                    list_name.append('Іменинник: '+str(b))
                    list_weekly.append(b)

    print('____________________________________')
    print('')
                    
    if len(list_name) >0: 
        count =1
        print('Іменинники на цьому тижні:') 
        print()  
             
        for f in list_name:
            print(f)
            count +=1
            if count%2 !=0:
                print('__________________________________')
    print('Юбіляри по днях тижня:')    
    day_old = None
    try:
        int(list_weekly[-1])
    except:
        list_weekly.pop()
    print(list_weekly)
    for s in range(len(list_weekly)):
        
        for q, m in days_weeks.items():                
            try:
                if s == 5 or s == 6:
                    s = 0                                        
                if int(list_weekly[s]) == q:
                    if day_old != m:
                        print(m,':')
                        print(list_weekly[s-1])
                        day_old = m     
                    else:
                        print(list_weekly[s-1])   

            except:
                continue






    


    

def spisok_weekly():
    print('')               



    

def main():
    work = True
    while work == True:
        print('Введіть код потрібної операції, та натисніть "Enter": ')
        print('1- Вивести загальний список з датами народження')
        print('2- Вивести спискок юбілярів поточного тижня')
        print('exit- Завершення роботи')
        chois =  input(' : ') 
    
        if chois == '1':
           list_birthday()
           print('return - Повернення в головне меню')
           print('exit- Завершення роботи')
           chois = input(' : ')
           if chois == 'exit':
            work = False
            break
           elif chois == 'return':
            main()
        elif chois == '2':
           weekly_jubilars()
           print('return - Повернення в головне меню')
           print('exit- Завершення роботи')
           chois = input(' : ')
           if chois == 'exit':
            work = False
            break
           elif chois == 'return':
            main()        
        elif chois == 'return':
           main()
        elif chois == 'exit':
            work = False
            break
    


main()
        

            

