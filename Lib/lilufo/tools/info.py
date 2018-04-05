def info():
    print("tools.info called, ufo = ", ufo)

    glyph_count = len(ufo)
    print("\nGlyph count:", glyph_count)

    for glyph in ufo:
        print("Glyph: ",glyph)
        for contour in glyph:
            print("  Contour: ", contour)
    print("\nDone.\n")
