import os
import numpy as num

user = "admin"
password = "admin"
log = ""
pas = ""

def adminpanel():
    print("#############open-blockchain##########")
    print("###############admin-panel############")
    print("# 1. start open-blockchain           #")
    print("# 2. settings                        #")
    print("# 3. quit admin-panel                #")
    print("######################################")
                                                   
def login():                                        
    print("#############open-blockchain##########")
    print("to start/manage open-blockchain log in")
    print("######################################")
    print("")
    log = input("username:")
    if log == user:
        pas = input("password:")
        if pas == password:
            print("login successful!")
            print("")
            adminpanel()
        else:
            print("wrong")
            login()
    else:
        print("wrong")
        login()

print("starting open-blockchain")
print("|||")
print("|||")
print("|||")
login()


