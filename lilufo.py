import argparse
import defcon

def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help = "input filename")
    parser.add_argument("-o", help = "output filename")
    args = parser.parse_args()
    return args

def banner_art():
    print(" .     *         .   *    .      ")
    print("    .     *     .                ")
    print(" * .------.  .        .          ")
    print(" _/____@_@_\_    .           .   ")
    print("(____________)      *            ")
    print("      .        .         .       ")
    print("li'l UFO   0.1     *             ")
    print("   .         .         .        .")

if __name__ == "__main__":
    banner_art()

    args = create_arg_parser()
    ufo_input_path = args.i
    ufo_output_path = args.o
    print("*********************************")
    print('ufo_input_path: ', ufo_input_path)
    print('ufo_output_path:', ufo_output_path)
    # Make UFO
    print("*********************************")
    print('Generating UFO...', ufo_output_path)
    ufo = defcon.Font(ufo_input_path)
    glyph_count = len(ufo)
    print("Glyph count:", glyph_count)
    ufo.save(ufo_output_path)
    print('Done.\n')
