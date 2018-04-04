# ART #########################
def banner_art():
    # os.system('clear')
    print("    .     *     .           .    ")
    print("   .------.                      ")
    print(" _/____@_@_\_              .     ")
    print("(____________)      *            ")
    print(" LI'L UFO 1.0     *      .       ")
    print("Working UFO: ", ufo)

# MAIN MENU ###################
def main_menu():
    print ("")
    print ("[0] Build new font    [5] Magic                  ")
    print ("[1] UFO Test          [6] Working UFO info       ")
    print ("[2] Edit glyphs       [7] Save UFO               ")
    print ("[3] Edit kerning      [8] Restart program        ")
    print ("[4] Add glyphs        [9] Quit program           ")
    choice = input(">>> ")
    return choice

# [0] Menu item: ufo
def ufo_build(ufo):
    # TEMP
    print("TEMP")

# [1] Menu item: ufo
def ufo_test(ufo):
    # Test UFO data
    glyph_count = len(ufo)
    print("\nGlyph count:", glyph_count)
    del ufo["A"]
    print("removing A from font... Done.")
    glyph_count = len(ufo)
    print("New glyph count:", glyph_count)

# [2] Menu item: UFO
def edit_glyphs(self):
    print("Edit glyphs!")
    app = QApplication([])
    win = GlyphWindow()
    win.show()
    return app.exec()

# [3] Menu item: UFO
def edit_kerning(args):
    print("Edit kerning!")

# [4] Menu item: UFO
def add_glyphs(args):
    print("Add glyphs!")

# [5] Menu item: UFO MAGIC
def magic(ufo):
    print("UFO info:")

    for glyph in ufo:
        print("Glyph: ", glyph)
        for contour in glyph:
            print("  Contour: ", contour)
            for point in contour:
                print("    Point: ", point)
    print("\nDone.\n")


### [6] MENU ITEM #############
def ufo_info(ufo):
    print("UFO info:")

    ### GLYPH COUNT ###########
    glyph_count = len(ufo)
    print("\nGlyph count:", glyph_count)

    ### GLYPH CONTOUR #########
    for glyph in ufo:
        print("Glyph: ",glyph)
        for contour in glyph:
            print("  Contour: ", contour)
    print("\nDone.\n")




    # Main Menu ###############
    banner_art(ufo)
    choice = int(main_menu())
    banner_art(ufo)

    if choice == 1:
        ufo_test(ufo)
    if choice == 2:
        win = GlyphWindow()
        win.show()
    if choice == 3:
        edit_kerning(ufo)
    if choice == 4:
        add_glyphs(ufo)
    if choice == 5:
        magic(ufo)
    if choice == 6:
        ufo_info(ufo)
    if choice == 7:
        font.save(ufo_output_path)
        print("UFO output... done: ", ufo_output_path)
    if choice == 8:
        restart_program()
    if choice == 9:
        print("Done, exit.")
        sys.exit()

    # CONTINUE ################
    print("Continue? [y/n]:")
    go_on = input(">>> ")
    if go_on == 'y':
        run()
    else:
        sys.exit()

