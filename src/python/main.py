#Copyright (C) 2026  denis9667

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

import platform
import os

# Пытаемся импортировать костыль очистки. Если не найдём - включим стандартный
try:
    from libs.clear import clear_console as clear
except ModuleNotFoundError:
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

user = "admin" #стандартный пользователь (админ)
password = "admin" #стандартный пароль от аккаунта (админа)
stat = 0  # 0 - остановлен, 1 - запущен


def com_exec(command): 
    global stat  # Работаем с глобальным статусом
    
    if command == "1":
        clear()
        if stat == 0:
            print("starting open-blockchain...") 
            stat = 1 
        else:
            print("stopping open-blockchain...")
            stat = 0
        input("\nНажмите Enter, чтобы вернуться в меню...")
        clear()
        
    elif command == "2":
        clear()
        print("--- settings ---") 
        print(f"Статус блокчейна: {stat}") 
        input("\nНажмите Enter, чтобы вернуться в меню...")
        clear()
        
    elif command == "3":
        clear()
        print("--- plugins ---") 
        input("\nНажмите Enter, чтобы вернуться в меню...")
        clear()

    elif command == "4":
        clear()
        print("Выход из аккаунта...")
        print(f"[INFO] Блокчейн продолжает работу в фоне. Статус: {stat}")
        input("\nНажмите Enter для перехода к окну авторизации...")
        clear()
        return "exit"  # Сигнал для выхода из меню в окно логина
        
    elif command == "0":
        clear()
        print("Остановка open-blockchain (shutdown)...")
        stat = 0 # Сбрасываем статус в 0
        print("Выход из аккаунта...")
        print("Программа полностью завершена. Всего доброго!")
        
        import sys
        sys.exit()  # Мгновенное и полное закрытие программы
    
    return "continue"




def init_admpanel():
    print("starting admin panel")
    print("")
    adminpanel()


def adminpanel():
    while True:
        if stat == 0:
            print("#############open-blockchain##########")
            print("###############admin-panel############")
            print("# 1. start open-blockchain           #")
            print("# 2. settings                        #")
            print("# 3. plugins                         #")       
            print("# 4. log out                         #")       
            print("# 0. shutdown and exit               #")
            print("######################################")
        elif stat == 1:
            print("#############open-blockchain##########")
            print("###############admin-panel############")
            print("# 1. stop open-blockchain            #")
            print("# 2. settings                        #")
            print("# 3. plugins                         #")       
            print("# 4. log out                         #")       
            print("# 0. shutdown and exit               #")
            print("######################################")
            
        command = input("> ")
        
        result = com_exec(command)
        if result == "exit":
            login()  # Возвращаемся в окно логина
            break    # Прерываем текущий цикл меню



def login():                                        
    while True:  # Бесконечный цикл вместо рекурсии
        print("#############open-blockchain##############")
        print("# to start/manage open-blockchain log in #")
        print("##########################################")
        print("")
        log = input("username: ")
        if log == user:
            pas = input("password: ")
            if pas == password:
                print("login successful!")
                clear()
                init_admpanel()
                break  # Выходим из цикла авторизации, так как зашли успешно
            else:
                clear()
                print("Wrong password! Try again.\n")
        else:
            clear()
            print("Wrong username! Try again.\n")


def startup():
    print(platform.system())
    print("starting open-blockchain")
    print("|||")
    print("|||")
    print("|||")
    clear()
    login()

# Точка входа для запуска файла напрямую
if __name__ == "__main__":
    startup()


