'''
kmtrebacz/py-blog main.py

Main app of all of project.
'''


import os
import time as t
import commands

__VERSION__ = "0.1.2"


def clr():
     os.system('cls')


def startApp():
     print("""
                            $$\       $$\                     
                            $$ |      $$ |                    
 $$$$$$\  $$\   $$\         $$$$$$$\  $$ | $$$$$$\   $$$$$$\  
$$  __$$\ $$ |  $$ |$$$$$$\ $$  __$$\ $$ |$$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  $$ |\______|$$ |  $$ |$$ |$$ /  $$ |$$ /  $$ |
$$ |  $$ |$$ |  $$ |        $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |
$$$$$$$  |\$$$$$$$ |        $$$$$$$  |$$ |\$$$$$$  |\$$$$$$$ |
$$  ____/  \____$$ |        \_______/ \__| \______/  \____$$ |
$$ |      $$\   $$ |                                $$\   $$ |
$$ |      \$$$$$$  |                                \$$$$$$  |
\__|       \______/                                  \______/ 
""")
     print("Version: ", __VERSION__)
     t.sleep(1.5)



if __name__ == "__main__":
     startApp()

     commands.main()