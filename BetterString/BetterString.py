from .Exceptions import *
from .Color import *
import re


FULL_SIZE = "fs"
BLUE = "blue"
CYAN = "cyan"
GREEN = "green"
ORANGE = "orange"
RED = "red"


class BetterString(str):
    __doc__ = """
    This returns a string with more functionality!

    BetterString has the same functions as str with a few extras and changes
    """.replace("    ", "")[1:]

    def __init__(self, inp):
        super().__init__()

        self.string = str(inp)

    # Upper / Lower
    def lower(self, size: int or str = FULL_SIZE):
        """
        Better Upper function. You can
        choose how many characters will
        be upper size
        """
        lower_string = ""
        if size == "fs":
            size = len(self.string) - 1
        elif isinstance(size, str):
            raise TypeError("Size has to be of type Integer")

        if size > len(self.string) - 1:
            raise ValueError(f"Size of {size} is to big!")

        i = 0
        for i in range(0, size):
            if i <= size:
                lower_string += self.string[i].lower()

        lower_string += self.string[i + 1:]

        return BetterString(lower_string)

    def upper(self, size: int or str = FULL_SIZE):
        """
        Better Upper function. You can
        choose how many characters will
        be upper size
        """
        upper_string = ""
        if size == "fs":
            size = len(self.string)-1
        elif isinstance(size, str):
            raise TypeError("Size has to be of type Integer")

        if size > len(self.string)-1:
            raise ValueError(f"Size of {size} is to big!")

        i = 0
        for i in range(0, size):
            if i <= size:
                upper_string += self.string[i].upper()

        upper_string += self.string[i+1:]

        return BetterString(upper_string)

    # Convert Str to type ...
    # I will not cover all types!
    def to_list(self) -> list or tuple:
        """
        Converts your string into a list or a tuple
        If the string is representing a list it will
        convert it to the represented list
        if not it will return every character in a list
        """
        try:
            liste = eval(self.string)
        except SyntaxError:
            liste = list(self.string)

        return liste

    def to_int(self) -> int:
        """
        Converts your string into an integer
        """
        try:
            return int(self.string)
        except ValueError:
            raise CannotConvertToError("int")

    def to_dict(self) -> dict:
        """
        Converts your string into an dictionary
        """
        try:
            return eval(self.string)
        except SyntaxError:
            raise CannotConvertToError("dict") from None
        except NameError:
            raise CannotConvertToError("dict") from None
        except TypeError:
            raise CannotConvertToError("dict") from None

    # Extras
    def colorize(self, color: str, bold: bool = False, underline: bool = False):
        """
        Colorizes the string with the given color

        Available colors:
        "blue",
        "cyan",
        "green",
        "orange",
        "red"

        :param color: Color which the text should have
        :param bold: If the text should be bold
        :param underline: If the text should be underlined
        """
        return BetterString(colorize(self.string, color, bold, underline))

    def count(self, pattern: str, start: int = 0, end: int = FULL_SIZE) -> int:
        """
        This counts how many time the pattern appears
        in the string.
        The pattern has to be a str if it is not it
        will be automatically converted

        **You can use regex**
        """
        if end == "fs":
            end = len(self.string)-1
        return len(re.findall(str(pattern), self.string[start:end]))

    def replace(self, old, new, count=1):
        return BetterString(self.string.replace(old, new, count))

    # Magic methods
    def __getitem__(self, item: int or slice):
        """
        item has to be int or slice
        if it is an str it will try to convert the str into an int
        """
        ret = None

        if isinstance(item, str):
            try:
                item = int(item)
            except ValueError:
                raise TypeError("String indices must be integers")

        if isinstance(item, int):
            ret = self.string[int(item)]

        elif isinstance(item, slice):
            slice_size = item.start
            str_len = len(self.string)

            if slice_size < str_len:
                ret = self.string[item]
            else:
                raise IndexStartOutOfBoundError

        elif isinstance(item, str):
            raise TypeError("String indices must be integers!")

        return BetterString(ret)

    def __call__(self) -> Exception:
        raise StringNotCallable()

    def __repr__(self) -> str:
        ret = f"BetterStrings('{self.string}')"

        return BetterString(ret)
