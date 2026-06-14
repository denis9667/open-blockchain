#Copyright (C) 2026  denis9667

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


import platform
import os

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
  