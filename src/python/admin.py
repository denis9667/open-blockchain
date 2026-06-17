#Copyright (C) 2026  denis9667

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


from .libs.clear import clear_console as clear

def init_admpanel():
    print("starting admin panel")
    adminpanel()

def adminpanel():
    print("#############open-blockchain##########")
    print("###############admin-panel############")
    print("# 1. start open-blockchain           #")
    print("# 2. settings                        #")
    print("# 3. plugins                         #")       
    print("# 0. exit admin panel                #")
    print("######################################")
    command = input(">")
     