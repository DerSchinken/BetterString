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
        """
        Return a copy with all occurrences of substring old replaced by new.

        count
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        return BetterString(self.string.replace(old, new, count))

    def capitalize(self, /):
        """
        Return a capitalized version of S, i.e. make the first
        character have upper case and the rest lower case.
        """
        ret = self.string.capitalize()
        return BetterString(ret)

    def casefold(self, /):
        """
        Return a version of the string suitable for caseless comparisons.
        """
        ret = self.string.casefold()
        return BetterString(ret)

    def center(self, width, fillchar=' ', /):
        """
        Return S centered in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space)
        """
        ret = self.string.center(width, fillchar)
        return BetterString(ret)

    def expandtabs(self, tabsize=8, /):
        """
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        ret = self.string.expandtabs(tabsize)
        return BetterString(ret)

    def format(self, *args, **kwargs):
        """
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        ret = self.string.format(*args, **kwargs)
        return ret

    def format_map(self, mapping, /):
        """
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        ret = self.string.format_map(mapping)
        return BetterString(ret)

    def join(self, iterable, /):
        """
        Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        """
        ret = self.string.join(iterable)
        return BetterString(ret)

    def ljust(self, width, fillchar=' ', /):
        """
        Return S left-justified in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space).
        """
        ret = self.string.ljust(width)
        return BetterString(ret)

    def lstrip(self, chars=None, /):
        """
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is a str, it will be converted to unicode before stripping
        """
        ret = self.string.lstrip(chars)
        return BetterString(ret)

    def rjust(self, width, fillchar=' ', /):
        """
        Return S right-justified in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space).
        """
        ret = self.string.rjust(width, fillchar)
        return BetterString(ret)

    def rstrip(self, chars=None, /):
        """
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is a str, it will be converted to unicode before stripping
        """
        ret = self.string.rstrip(chars)
        return BetterString(ret)

    def strip(self, chars=None, /):
        """
        Return a copy of the string S with leading and trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead. If chars
         is a str, it will be converted to unicode before stripping
        """
        ret = self.string.strip(chars)
        return BetterString(ret)

    def swapcase(self, /):
        """
        Return a copy of S with uppercase characters converted to lowercase and vice versa.
        """
        ret = self.string.swapcase()
        return BetterString(ret)

    def title(self, /):
        """
        Return a titlecased version of S, i.e. words start with title case characters, all
        remaining cased characters have lower case.
        """
        ret = self.string.title()
        return BetterString(ret)

    def translate(self, table, /):
        """
        Replace each character in the string using the given translation table.

        table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.

        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        ret = self.string.translate(table)
        return BetterString(ret)

    def zfill(self, width, /):
        """
        Pad a numeric string S with zeros on the left, to fill a field of the specified width.
        The string S is never truncated.
        """
        ret = self.string.zfill(width)
        return BetterString(ret)

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

    def __repr__(self):
        ret = f"BetterStrings('{self.string}')"

        return BetterString(ret)

    def __add__(self, value, /):
        ret = self.string.__add__(value)
        return BetterString(ret)

    def __getnewargs__(self):
        ret = self.string.__getnewargs__()
        return BetterString(ret)

    def __mul__(self, value, /):
        ret = self.string.__mul__(value)
        return BetterString(ret)

    def __rmul__(self, value, /):
        ret = self.string.__rmul__(value)
        return BetterString(ret)
