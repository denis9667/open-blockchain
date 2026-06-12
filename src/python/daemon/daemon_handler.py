#Copyright (C) 2026  denis9667

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


import sys
import time
from daemoniker import Daemonizer

def main_service():
    with open( 'daemon.log', 'a') as f:
        f.write(f"Daemon running at {time.ctime()}\n")
    print("starting daemon")


if __name__ == "__main__":
    pid_file = 'main_daemon.pid'


    with Daemonizer() as (is_setup, daemonizer):
        if is_setup:

            pass


        is_parent, pid = daemonizer(pid_file)

        if is_parent:
            print("daemon started")
            sys.exit(0)


        while True:
            main_service()
            time.sleep(10)