import os
import time

def SayHello(name):
        if name:
                print("Hello " + name)
        else:
                name = raw_input("Vous n'avez pas saisi de nom, merci d'en saisir un:")
                SayHello(name)

def main():
    SayHello("Anis")
    time.sleep(2)
    os.system('calc.exe')
