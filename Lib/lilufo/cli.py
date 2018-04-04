import os
import sys
from .router import router

def main_menu(ufo):
    banner(ufo)
    choice = int(tools())
    print("Choice:", choice)
    router(choice, ufo)
    exit()

# BANNER ART #----------------#
def banner(ufo):
    os.system('clear')
    print("    .     *     .           .     ")
    print("   .-----.                        ")
    print(" _/___@_@_\_              .       ")
    print("(___________)      *              ")
    print(" LIL UFO 1.0      *   .           ")
    print("")
    print("UFO Working File: ", ufo)
    print("UFO Output Path:  ", ufo)

# TOOLS MENU #----------------#
def tools():
    print ("")
    print ("[0] MAKE FONTS        [5] MATH       ")
    print ("[1] TEST UFO          [6] INFO       ")
    print ("[2] EDIT GLYPHS       [7] VIEW       ")
    print ("[3] EDIT KERNING      [8] SAVE       ")
    print ("[4] EDIT FONT         [9] QUIT       ")
    print("")
    choice = input(">>> ")
    return choice

def exit():
    print("Exit? [y/n]:")
    c = input(">>> ")
    if c == 'n':
        sys.exit()
    else:
        pass
