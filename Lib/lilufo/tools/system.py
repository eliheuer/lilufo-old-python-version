def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def create_arg_parser():
    """
    Get input and output UFOs from the commandline
    See: https://elih.blog/ttf-to-ufo
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help = "input filename")
    parser.add_argument("-o", help = "output filename")
    args = parser.parse_args()
return args
