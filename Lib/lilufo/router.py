from lilufo.tools.exit import exit
from lilufo.tools.font import font
from lilufo.tools.glif import glif
from lilufo.tools.info import info
from lilufo.tools.kern import kern
from lilufo.tools.make import make
from lilufo.tools.math import math
from lilufo.tools.quit import quit
from lilufo.tools.save import save
from lilufo.tools.test import test
from lilufo.tools.view import view

# MAIN MENU ROUTER #-------------#
def router(choice, ufo):
    ###############
    if choice == 0:
        make()
    ###############
    if choice == 1:
        test()
    ###############
    if choice == 2:
        glif()
    ###############
    if choice == 3:
        kern()
    ###############
    if choice == 4:
        font()
    ###############
    if choice == 5:
        math()
    ###############
    if choice == 6:
        info()
    ###############
    if choice == 7:
        view()
    ###############
    if choice == 8:
        save()
    ###############
    if choice == 9:
        exit(ufo)

