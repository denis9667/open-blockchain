#Copyright (C) 2026  denis9667

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


from libs.clear import clear_console as clear
from main import login



def startup_init():
    print("starting main services")
    print("starting login")
    clear()
    login()

    