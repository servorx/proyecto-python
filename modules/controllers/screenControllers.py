from os import system
import sys

def clean_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def pause_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    x=input("press a keybind to continue")
    return x
  else:
    system("pause")