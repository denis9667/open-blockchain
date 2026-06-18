#Copyright (C) 2026  denis9667

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))) #что-бы точно библиотеки из src/python/libs/*.py импортировались
from src.python.main import startup

if __name__ == "__main__":
    startup() #запуск входа в админский аккаунт


