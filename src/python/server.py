#Copyright (C) 2026  denis9667
import hashlib
import time
import uvicorn
from fastapi import FastAPI, Body

server_app = FastAPI() #создаём fastapi серверное приложение
blockchain_data = [] #данные блокчейна о блоках
difficulty = 2 #стандартная сложность блокчейна

def calculate_hash(index, prev_hash, timestamp, data, nonce): #считаем/создаём хеш
    value = f"{index}{prev_hash}{timestamp}{data}{nonce}".encode()
    return hashlib.sha256(value).hexdigest()

@server_app.get("/status") #api для проверки статуса
def get_status():
    return {"status": "running", "blocks_count": len(blockchain_data), "difficulty": difficulty}

@server_app.get("/blocks") #api для получения данных о блоках
def get_blocks():
    return blockchain_data

@server_app.post("/set_difficulty") #api для изменения сложности блокчейна
def set_difficulty(payload: dict = Body(...)):
    global difficulty
    difficulty = payload.get("difficulty", 2)
    return {"status": "success", "difficulty": difficulty}

@server_app.post("/mine") #api для майна/создания блока с данными
def mine_endpoint(payload: dict = Body(...)):
    global blockchain_data
    data = payload.get("data", "")
    prev_hash = "0"*64 if not blockchain_data else blockchain_data[-1]["hash"]
    index = len(blockchain_data)
    timestamp = time.time()
    nonce = 0
    target = "0" * difficulty
    
    while True: 
        current_hash = calculate_hash(index, prev_hash, timestamp, data, nonce) #считаем/создаём хеш для блока из времени, передыдущего хеша и данных блока с нужным количеством нулей
        if current_hash.startswith(target): #создаём блок с хешом
            new_block = {"index": index, "previous_hash": prev_hash, "timestamp": timestamp, "data": data, "nonce": nonce, "hash": current_hash}
            blockchain_data.append(new_block) #добавляем новый блок в данные блокчейна о блоках
            return {"status": "mined", "block": new_block} #возвращаем статус "mined block"
        nonce += 1

def run_fastapi_server(): #запускаем fastapi сервер
    if not blockchain_data:
        t = time.time()
        blockchain_data.append({"index": 0, "previous_hash": "0"*64, "timestamp": t, "data": "Genesis Block", "nonce": 0, "hash": "0000"})
    uvicorn.run(server_app, host="127.0.0.1", port=8000, log_level="warning")

# Точка входа для запуска процесса бэкенда через subprocess
if __name__ == "__main__":
    run_fastapi_server()
