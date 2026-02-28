import math
sotr = []
admin = False

while True:
    if not admin:
        print("1. Войти как администратор")
        print("2. Просмотреть список сотрудников")
        print("3. Калькулятор кредита")
        print("4. Выход")
        vb = input("Выбор:")
        
        if vb == "1":
            password = input("Введите пароль администратора:")
            if password == "admin123": 
                admin = True
                print("Успешный вход!")
            else:
                print("Неверный пароль!")
                
        elif vb == "2":
            if len(sotr) == 0:
                print("Нет сотрудников")
            else:
                for i, num in enumerate(sotr, 1):
                    print(f"{i}. ФИО: {num[0]}, Зарплата: {num[4]} руб.")
                    
        elif vb == "3":
            sum = int(input("Введите сумму кредита:"))
            pribil = int(input("Введите прибыль:"))
            pro = int(input("Введите процент:"))
            pro_prib = int(input("Введите процент от прибыли:"))
            x = 0
            sum1 = sum * (pro / 100)
            itog = 0
            while x <= sum1:
                x = x + pro_prib
                itog += 1
            print(f"Количество месяцев: {int(itog)}")
            
        elif vb == "4":
            break
        else:
            print("Неверный выбор!")
    
    else:  
        print("\n=== Администратор ===")
        print("1. Добавить сотрудника")
        print("2. Список сотрудников")
        print("3. Калькулятор кредита")
        print("4. Выйти из режима администратора")
        print("5. Выход из программы")
        vb = input("Выбор:")
        
        if vb == "1":  
            fio = input("ФИО:")
            money = int(input("Ставка работника:"))
            hours = int(input("Количество часов в неделе:"))
            day = int(input("Количество рабочих дней в неделе:"))
            zp = hours * money * day
            sotr.append([fio, money, hours, day, zp])
            print("Сотрудник добавлен!")
            
        elif vb == "2":  
            if len(sotr) == 0:
                print("Нет сотрудников")
            else:
                for i, num in enumerate(sotr, 1):
                    print(f"{i}. ФИО: {num[0]}, Ставка: {num[1]}, Часов: {num[2]}, Дней: {num[3]}, Зарплата: {num[4]} руб.")
                    
        elif vb == "3":  
            sum = int(input("Введите сумму кредита:"))
            pribil = int(input("Введите прибыль:"))
            pro = int(input("Введите процент:"))
            pro_prib = int(input("Введите процент от прибыли:"))
            x = 0
            sum1 = sum * (pro / 100)
            itog = 0
            while x <= sum1:
                x = x + pro_prib
                itog += 1
            print(f"Количество месяцев: {int(itog)}")
            
        elif vb == "4":  
            admin = False
            print("Вы вышли из режима администратора")
            
        elif vb == "5":  
            break
        else:
            print("Неверный выбор!")