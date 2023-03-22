'''
kmtrebacz/py-blog commands.py

Python file that let you write commands
'''


import sys
import time as t
import createNew
import const


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
               const.clr()
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
