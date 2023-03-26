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
          elif inputCommands == "-cNew":
               const.clr()
               print(inputCommands)
               createNew.main()

          #
          # SHOWING THEMES
          #
          elif inputCommands == "-thms":
               print(" THEMES ")
               print("========")
               print("- the themes times [1]")

               whatOpen = input("Which theme you want to see:")

               if whatOpen == "1":
                    print("ttt")
               else:
                    print("Error")



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
