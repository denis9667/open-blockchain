#Copyright (C) 2026  denis9667

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


import os, sys, time, json, urllib.request, subprocess, signal

try:
    from libs.clear import clear_console as clear
except ModuleNotFoundError:
    def clear(): os.system('cls' if os.name == 'nt' else 'clear')

user, password = "admin", "admin"
PID_FILE = "blockchain_node.pid"
SERVER_URL = "http://127.0.0.1:8000"

def check_node_alive():
    try:
        with urllib.request.urlopen(f"{SERVER_URL}/status", timeout=1) as r:
            return json.loads(r.read().decode())
    except: return None

def send_post(endpoint, data):
    try:
        req = urllib.request.Request(f"{SERVER_URL}{endpoint}", data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as r: return json.loads(r.read().decode())
    except: return {"status": "error"}

def stop_node():
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, "r") as f: 
                pid = int(f.read().strip())
            # Кросс-платформенное принудительное завершение процесса
            os.kill(pid, signal.SIGTERM)
        except: pass
        try: os.remove(PID_FILE)
        except: pass

def com_exec(command): 
    node_info = check_node_alive()
    is_running = node_info is not None
    
    if command == "1":
        clear()
        if not is_running:
            print("[DAEMON] Запуск фонового блокчейна FastAPI...")
            try:
                python_exe = sys.executable
                server_path = os.path.join(os.path.dirname(__file__), "server.py")
                
                # Флаг скрытия окна только для Windows, на Unix это не вызовет ошибок
                creation_flags = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                
                proc = subprocess.Popen(
                    [python_exe, server_path],
                    creationflags=creation_flags,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                
                with open(PID_FILE, "w") as f:
                    f.write(str(proc.pid))
                
                time.sleep(2.5)
                if check_node_alive(): print("[SUCCESS] Блокчейн успешно запущен в фоне!")
                else: print("[ERROR] Сервер не ответил. Проверьте server.py.")
            except Exception as e: print(f"Ошибка запуска: {e}")
        else:
            print("[DAEMON] Остановка фонового процесса...")
            stop_node()
            print("[SUCCESS] Остановлен.")
        input("\nEnter..."); clear()
        
    elif command == "2":
        clear()
        if not is_running: print("Блокчейн оффлайн."); input("\nEnter..."); clear(); return "continue"
        while True:
            node_info = check_node_alive()
            print(f"--- НАСТРОЙКИ (Сложность: {node_info['difficulty'] if node_info else '?'}) ---\n1. Изменить сложность\n2. Проводник блоков\n0. Назад")
            cmd = input("> ")
            if cmd == "1":
                diff = int(input("Новая сложность: "))
                send_post("/set_difficulty", {"difficulty": diff})
            elif cmd == "2":
                clear()
                with urllib.request.urlopen(f"{SERVER_URL}/blocks") as r: blocks = json.loads(r.read().decode())
                for b in blocks: print(f"Блок #{b['index']} | Данные: {b['data']}\nХэш: {b['hash']}\n" + "-"*30)
                input("\nEnter..."); clear()
            elif cmd == "0": clear(); break
        
    elif command == "3":
        clear()
        if not is_running: print("Сервер выключен!")
        else:
            tx_data = input("Введите данные блока: ")
            res = send_post("/mine", {"data": tx_data})
            if res.get("status") == "mined": print(f"[SUCCESS] Блок #{res['block']['index']} добавлен в цепь!")
        input("\nEnter..."); clear()

    elif command == "4":
        clear(); print("Выход из аккаунта. Сервер работает в фоне."); input("\nEnter..."); clear()
        return "exit"
        
    elif command == "0":
        clear(); print("[SHUTDOWN] Выключение сервера...")
        stop_node()
        sys.exit()
    return "continue"

def adminpanel():
    while True:
        is_run = check_node_alive() is not None
        print(f"#############open-blockchain##########\n###############admin-panel (Фон: {'ON' if is_run else 'OFF'})###")
        print(f"# 1. {'stop' if is_run else 'start'} background node            #\n# 2. settings & block explorer       #\n# 3. MINE NEW BLOCK ON NODE          #\n# 4. log out                         #\n# 0. shutdown node and exit          #\n######################################")
        if com_exec(input("> ")) == "exit":
            login(); break

def login():                                        
    while True:
        print("#############open-blockchain##############\n# to start/manage open-blockchain log in #\n##########################################\n")
        if input("username: ") == user and input("password: ") == password:
            clear(); adminpanel(); break
        else: clear(); print("Неверно!\n")

def startup(): clear(); login()