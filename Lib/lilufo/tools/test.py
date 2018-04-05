def test():
    print("tools.test called, ufo = ", ufo)
    glyph_count = len(ufo)
    print("\nGlyph count:", glyph_count)
    del ufo["A"]
    print("removing A from font... Done.")
    glyph_count = len(ufo)
    print("New glyph count:", glyph_count)
