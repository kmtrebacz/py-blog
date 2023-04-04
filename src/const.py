import os

def clr():
    try:
        os.system('cls')
    except:
        try:
            os.system('clear')
        except:
            print("Error [2]  - command promt can't be cleaned")