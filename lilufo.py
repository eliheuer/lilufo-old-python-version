import argparse
import defcon
import sys, os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help = "input filename")
    parser.add_argument("-o", help = "output filename")
    args = parser.parse_args()
    return args

def banner_art():
    os.system('clear')
    print(" .     *         .   *    .      ")
    print("    .     *     .                ")
    print(" * .------.  .        .          ")
    print(" _/____@_@_\_    .           .   ")
    print("(____________)      *            ")
    print("      .        .         .       ")
    print("Li'l UFO 0.1       *             ")
    print(".             .        .        .")

# Main menu
def main_menu():
    print ("Welcome, earthling.")
    print ("Please choose a choice:")
    print ("\n[1] UFO Test")
    print ("[2] Edit glyphs")
    print ("[3] Edit kerning")
    print ("[4] Add glyphs")
    print ("[5] Restart program")
    print ("[6] Quit program")

    choice = input(">>> ")
    return choice

def ufo_test(ufo):
    # Test UFO data
    glyph_count = len(ufo)
    print("\nGlyph count:", glyph_count)

    del ufo["A"]
    print("removing A from font... Done.")
    glyph_count = len(ufo)
    print("New glyph count:", glyph_count)

    ufo.save(ufo_output_path)
    print("UFO output... done: ", ufo_output_path)

def edit_glyphs(args):
    print("Edit glyphs!")

def edit_kerning(args):
    print("Edit kerning!")

def add_glyphs(args):
    print("Add glyphs!")

def run():
    banner_art()

    # Load UFO
    args = create_arg_parser()
    ufo_input_path = args.i
    ufo_output_path = args.o
    ufo = defcon.Font(ufo_input_path)

    # Main menu
    choice = int(main_menu())

    banner_art()
    if choice == 1:
        ufo_test(ufo)
    if choice == 2:
        edit_glyphs(ufo)
    if choice == 3:
        edit_kerning(ufo)
    if choice == 4:
        add_glyphs(ufo)
    if choice == 5:
        view_proof()
    if choice == 6:
        ufo_info(ufo)
    if choice == 7:
        ufo.save(ufo_output_path)
        print("UFO output... done: ", ufo_output_path)
    if choice == 8:
        restart_program()
    if choice == 9:
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
    run()
