import os
import sys
import argparse
import defcon

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help = "input filename")
    parser.add_argument("-o", help = "output filename")
    args = parser.parse_args()
    return args

def banner_art(font):
    os.system('clear')
    print("    .     *     .                  .            ")
    print(" * .------.  .        .                         ")
    print(" _/____@_@_\_    .           .                  ")
    print("(____________)      *                           ")
    print("      .        .         .                .     ")
    print("Li'l UFO 0.1       *                            ")
    print("Working UFO: ", font)
    print(" .     *         .   *    .                    .")

# Main menu
def main_menu():
    print ("Welcome, earthling.")
    print ("Please choose a choice:")
    print ("")
    print ("[0] Build new font    [5] Magic                ")
    print ("[1] UFO Test          [6] Working UFO info     ")
    print ("[2] Edit glyphs       [7] Save UFO             ")
    print ("[3] Edit kerning      [8] Restart program      ")
    print ("[4] Add glyphs        [9] Quit program         ")
    choice = input(">>> ")
    return choice

def ufo_test(font):
    # Test UFO data
    glyph_count = len(font)
    print("\nGlyph count:", glyph_count)
    del font["A"]
    print("removing A from font... Done.")
    glyph_count = len(font)
    print("New glyph count:", glyph_count)

def edit_glyphs(args):
    print("Edit glyphs!")

def edit_kerning(args):
    print("Edit kerning!")

def add_glyphs(args):
    print("Add glyphs!")

def main():

    # Load UFO
    args = create_arg_parser()
    ufo_input_path = args.i
    ufo_output_path = args.o
    font = defcon.Font(ufo_input_path)
    banner_art(font)


    #for glyph in font:
    #    print(glyph)
    # Main menu
    choice = int(main_menu())

    banner_art(font)
    if choice == 1:
        ufo_test(font)
    if choice == 2:
        edit_glyphs(font)
    if choice == 3:
        edit_kerning(font)
    if choice == 4:
        add_glyphs(font)
    if choice == 5:
        view_proof()
    if choice == 6:
        ufo_info(font)
    if choice == 7:
        font.save(ufo_output_path)
        print("UFO output... done: ", ufo_output_path)
    if choice == 8:
        restart_program()
    if choice == 9:
        print("Done, exit.")
        sys.exit()

    print("Continue? [y/n]:")
    go_on = input(">>> ")
    if go_on == 'y':
        flag = True
    else:
        flag = False

    if flag == True:
        run()
    else:
        sys.exit()

if __name__ == "__main__":
    main()
