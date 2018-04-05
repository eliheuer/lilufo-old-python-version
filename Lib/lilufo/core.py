from .cli import main_menu
from .router import router
import argparse
import defcon

# load ufo #------------------#
global ufo # make ufo a global object

# use argparse #--------------#
parser = argparse.ArgumentParser()
parser.add_argument("-i", help = "input filename")
parser.add_argument("-o", help = "output filename")
args = parser.parse_args()

# use defcon #----------------#
ufo_input_path = args.i
ufo_output_path = args.o
ufo = defcon.Font(ufo_input_path)

# run main loop #-------------#
def main():
    flag = True
    while flag == True:
        main_menu(ufo)
