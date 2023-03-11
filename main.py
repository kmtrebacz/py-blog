'''
kmtrebacz/BlogCreator main.py

Main app of all of project.
'''


import os
import time as t
import commands

__VERSION__ = "0.1.0"


def clr():
     os.system('cls')


def startApp():
     print("kmtrebacz/BlogCreator")
     print("Version: ", __VERSION__)
     t.sleep(1.5)



if __name__ == "__main__":
     startApp()

     commands.main()