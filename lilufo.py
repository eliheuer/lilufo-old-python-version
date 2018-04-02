import argparse
import defcon
import sys, os

def restart_program():
    """
    Restarts the current program.
    Note: this function does not return. Any cleanup action
    (like saving data) must be done before calling this function.
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)

def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help = "input filename")
    parser.add_argument("-o", help = "output filename")
    args = parser.parse_args()
    return args

def get_ufos():
    args = create_arg_parser()
    ufo_input_path = args.i
    ufo_output_path = args.o
    print('UFO input path: ', ufo_input_path)
    print('UFO output path:', ufo_output_path)
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
    print ("\nWelcome, earthling.")
    print ("Please choose a choice:")
    print ("\n[1] Write Output UFO")
    print ("[2] Edit glyphs")
    print ("[3] Edit kerning")
    print ("[4] Restart program")
    print ("[5] Quit program")

    choice = input(">>> ")
    exec_choice(int(choice))

def exec_choice(choice):
    if int(choice) == 1:
        print("Choice = 1")
        return 1
    if int(choice) == 2:
        print("Choice = 2")
        return 2
    if int(choice) == 3:
        print("Choice = 3")
        return 3
    if int(choice) == 4:
        print("Choice = 4")
        restart_program()
    if int(choice) == 5:
        print("Choice = 5")
        sys.exit()
    else:
        print("Error: enter an integer please. :(")

def ufo_test(args):
    ufo_input_path = args.i
    ufo_output_path = args.o
    print('\nUFO input path: ', ufo_input_path)
    print('UFO output path:', ufo_output_path)
    ufo = defcon.Font(ufo_input_path)

    glyph_count = len(ufo)
    print("\nGlyph count:", glyph_count)
    del ufo["A"]
    print("removing A from font... Done.")
    glyph_count = len(ufo)
    print("New glyph count:", glyph_count)
    ufo.save(ufo_output_path)
    print("UFO output... done: ", ufo_output_path)
    print('Done.\n')

if __name__ == "__main__":
    banner_art()
    args = create_arg_parser()
    choice = main_menu()
    ufo_test(args)
