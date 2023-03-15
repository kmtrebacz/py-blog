'''
kmtrebacz/py-blog commands.py

Python file that let you write commands
'''


import sys
import os
import time as t
import createNew


# CLEARING CMD
def clr():
     os.system('cls')


# WHILE COMMANDS INPUT
def main():

     while True:
          inputCommands = input(" > ")


          #
          # HELP
          #
          if inputCommands == "-help":
               print(" HELP ")
               print("======")
               print("-help  ->  show all avaliable commands")
               print("-crtNew  ->  create new blog")
               print("-quit  ->  quit a program")


          #
          # CREATING NEW BLOG
          #
          elif inputCommands == "-crtNew":
               clr()
               print(inputCommands)
               createNew.main()


          #
          # QUIT
          #
          elif inputCommands == "-quit":
               sys.exit(0)

          #
          # ERROR
          #
          else:
               print("Error [1] -> Wrong command. Please write again")
