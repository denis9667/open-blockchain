#Copyright (C) 2026  denis9667

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


import platform
import os


from .libs.clear import clear_console
from .admin import *

from .libs.clear import clear_console as clear
from .admin import adminpanel


user = "admin"
password = "admin"
log = ""
pas = ""



                                                   
def login():                                        
    print("#############open-blockchain##############")
    print("# to start/manage open-blockchain log in #")
    print("##########################################")
    print("")
    log = input("username:")
    if log == user:
        pas = input("password:")
        if pas == password:
            print("login successful!")
            clear()
            init_admpanel()
        else:
            print("wrong")
            login()
    else:
        print("wrong")
        login()

def startup():
    print(platform.system())
    print("starting open-blockchain")
    print("|||")
    print("|||")
    print("|||")
    login()


