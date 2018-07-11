def math():
    print("tools.math called, ufo = ", ufo)
    print("bye!")

    for glyph in ufo:
        print("Glyph: ", glyph)
        for contour in glyph:
            print("  Contour: ", contour)
            for point in contour:
                print("    Point: ", point)
    print("\nDone.\n")
