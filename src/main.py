import platform
import os
import numpy as num

from clear import clear_console
from admin import *

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
            clear_console()
            adminpanel()
        else:
            print("wrong")
            login()
    else:
        print("wrong")
        login()

print(platform.system())
print("starting open-blockchain")
print("|||")
print("|||")
print("|||")
login()


 