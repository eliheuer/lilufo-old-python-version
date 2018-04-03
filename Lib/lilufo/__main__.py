from defconQt import representationFactories as baseRepresentationFactories
from lilufo.windows.glyphWindow import GlyphWindow, DotsWidget
from PyQt5.QtWidgets import QApplication
import argparse
import defcon
import os
import sys

# --------------------------- #
# Main: Program starts here.  #
# --------------------------- #
def main():
    global app

    # register representation factories
    baseRepresentationFactories.registerAllFactories()

    # [TODO]I'm not sure this is the best place for this? 
    app = QApplication([])

    # Load UFO
    # args = create_arg_parser()
    # ufo_input_path = args.i
    # ufo_output_path = args.o
    # ufo = defcon.Font(ufo_input_path)

    # Test
    print("TEST ::")

if __name__ == "__main__":
    main()
