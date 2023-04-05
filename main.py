'''
kmtrebacz/py-blog main.py

Main app of all of project.
'''

import sys 
import os
import time as t
import src.blogConfig as blogConfig
import src.const as const
import webbrowser


__VERSION__ = "0.2.2"

def startApp():
     print("Version: ", __VERSION__)
     print("""
██████╗ ██╗   ██╗     ██████╗ ██╗      ██████╗  ██████╗ 
██╔══██╗╚██╗ ██╔╝     ██╔══██╗██║     ██╔═══██╗██╔════╝ 
██████╔╝ ╚████╔╝█████╗██████╔╝██║     ██║   ██║██║  ███╗
██╔═══╝   ╚██╔╝ ╚════╝██╔══██╗██║     ██║   ██║██║   ██║
██║        ██║        ██████╔╝███████╗╚██████╔╝╚██████╔╝
╚═╝        ╚═╝        ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ 
""")
     t.sleep(1.5)


def commands():
     while True:
          inputCommands = input("\n > ")

          #
          # HELP
          #
          if inputCommands == "show -help":
               const.clr()

               print("==================")
               print("|      HELP      |")
               print("==================")
               print("show -help  ->  show all avaliable commands")
               print("show -themes  ->  show all avaliable themes, and let you open test page")
               print("create -blog  ->  create new blog")
               print("quit  ->  quit a program")

          #
          # SHOWING THEMES
          #
          elif inputCommands == "show -themes":
               const.clr()

               print("====================")
               print("|      THEMES      |")
               print("====================")
               print("- the themes times -> --ttt")


          elif inputCommands == "show -themes --ttt":
               webbrowser.open(os.path.join('./themes/ttt', 'ttt.html'), new=2)


          #
          # CREATING NEW BLOG
          #
          elif inputCommands == "create -blog":
               const.clr()

               blogConfig.main()

          #
          # QUIT
          #
          elif inputCommands == "quit":
               const.clr()

               sys.exit(0)

          #
          # ERROR
          #
          else:
               print("Error [1] -> Wrong command. Please write again")


if __name__ == "__main__":
    startApp()

    commands()

    
