def rgb(r, g, b):
    def clamp(x):
        return max(0, min(x, 255))

    r = clamp(r)
    g = clamp(g)
    b = clamp(b)

    return "{:02X}{:02X}{:02X}".format(r, g, b).upper()


print(rgb(-20, 275, 125))
