def rgb_to_int(r, g, b):
    if isinstance(r, int):
        if isinstance(g, int):
            if isinstance(b, int):
                pass
            else:
                raise TypeError("b has to be of type int")
        else:
            raise TypeError("g has to be of type int")
    else:
        raise TypeError("r has to be of type int")

    if r > 255:
        raise ValueError("r is too big")
    elif g > 255:
        raise ValueError("g is too big")
    elif b > 255:
        raise ValueError("b is to big")

    formula = f"65536 * {r} + 256 * {g} + {b}"
    result = eval(formula)
    return result
