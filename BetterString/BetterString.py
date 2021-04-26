from .Exceptions import *
from .Color import *
import re

# Important: Always put out new version on PyPI before pushing to github

FULL_SIZE = "fs"

# Colors
BLUE = 'BLUE'
CYAN = 'CYAN'
GREEN = 'GREEN'
ORANGE = 'ORANGE'
RED = 'RED'
BLACK = 'BLACK'
PURPLE = 'PURPLE'
WHITE = 'WHITE'
YELLOW = 'YELLOW'

# Background Colors
BLACK_BG = 'BLACK'
RED_BG = 'RED'
GREEN_BG = 'GREEN'
YELLOW_BG = 'YELLOW'
BLUE_BG = 'BLUE'
PURPLE_BG = 'PURPLE'
CYAN_BG = 'CYAN'
WHITE_BG = 'WHITE'


class BetterString(str):
    __doc__ = """
    This returns a string with more functionality!

    BetterString has the same functions as str with a few extras and changes
    """.replace("    ", "")[1:]

    def __init__(self, inp):
        super().__init__()

        self.string = str(inp)

    def lower(self, end=FULL_SIZE, start=0):
        """
        Better Upper function. You can
        choose how many characters will
        be upper size
        """
        lower_string = ""
        if end == "fs":
            end = len(self.string)
        elif isinstance(end, str):
            try:
                end = int(end)
            except ValueError:
                raise TypeError("end has to be of type Int")

        if isinstance(start, str):
            try:
                start = int(start)
            except ValueError:
                raise TypeError("Start has to be of type Int")

        if end > len(self.string):
            raise ValueError(f"'end' of {end} is to big!")
        if start > len(self.string):
            raise ValueError(f"'start' of {start} is to big")

        i = start
        for i in range(start, end):
            if i <= end:
                lower_string += self.string[i].lower()

        lower_string += self.string[i + 1:]

        return BetterString(lower_string)

    def upper(self, end=FULL_SIZE, start=0):
        """
        Better Upper function. You can
        choose how many characters will
        be upper size
        """
        upper_string = ""
        if end == "fs":
            end = len(self.string)
        elif isinstance(end, str):
            try:
                end = int(end)
            except ValueError:
                raise TypeError("Size has to be of type Integer") from None
        if isinstance(start, str):
            try:
                start = int(start)
            except ValueError:
                raise TypeError("Start has to be of type Int")

        if end > len(self.string):
            raise ValueError(f"Size of {end} is to big!")
        if start > len(self.string):
            raise ValueError(f"'start' of {start} is to big")

        i = start
        for i in range(start, end):
            if i <= end:
                upper_string += self.string[i].upper()

        upper_string += self.string[i + 1:]

        return BetterString(upper_string)

    def to_list(self) -> list:
        """
        Converts your string into a list or a tuple
        If the string is representing a list it will
        convert it to the represented list
        if not it will return every character in a list
        """
        try:
            list_ = eval(self.string)
        except SyntaxError:
            list_ = list(self.string)
        except NameError:
            list_ = list(self.string)

        return list_

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

    def colorize(self, color=None, bg=None, bold=False, underline=False, start=0, end=FULL_SIZE):
        """
        Colorizes the string with the given color

        Available text colors:
        'BLUE',
        'CYAN',
        'GREEN',
        'ORANGE',
        'RED',
        'BLACK',
        'PURPLE',
        'WHITE',
        'YELLOW'

        Available background colors:
        'BLACK',
        'RED',
        'GREEN',
        'YELLOW',
        'BLUE',
        'PURPLE',
        'CYAN',
        'WHITE'

        :param color: Color of the text
        :param bold: If the text should be bold
        :param underline: If the text should be underlined
        :param bg: Background color of the text
        :param start: start of colors and stuff
        :param end: end of colors and stuff
        """
        if end == "fs":
            end = len(self.string)

        return BetterString(colorize(text=self.string, color=color, bold=bold, underline=underline, bg=bg, start=start, end=end))

    def count(self, pattern, start: int = 0, end: int = FULL_SIZE, regex: bool = False):
        """
        This counts how many time the pattern appears
        in the string.
        The pattern has to be a str if it is not it
        will be automatically converted

        **You can use regex**
        """
        if end == "fs":
            end = len(self.string)
        if regex:
            ret = len(re.findall(str(pattern), self.string[start:end]))
        else:
            ret = self.string.count(pattern, start, end)
        return ret

    def replace(self, old: str, new: str = "", count: int = FULL_SIZE, regex: bool = False):
        """
        Return a copy with all occurrences of substring old replaced by new.

        **You can use regex**

        count
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        if count == "fs":
            count = len(self.string)
        if regex:
            ret = re.sub(old, new, self.string, count)
        else:
            ret = self.string.replace(old, new, count)
        return BetterString(ret)

    def remove(self, pattern: str, count: int = FULL_SIZE, regex: bool = False):
        """
        Return a copy with all occurrences of substring pattern removed

        **You can use regex**

        count
        Maximum number of occurrences to replace.
        FULL_SIZE (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        if count == "fs":
            count = len(self.string)
        if regex:
            ret = re.sub(str(pattern), "", self.string, count)
        else:
            ret = self.string.replace(pattern, "", count)
        return ret

    def capitalize(self):
        """
        Return a capitalized version of S, i.e. make the first
        character have upper case and the rest lower case.
        """
        ret = self.string.capitalize()
        return BetterString(ret)

    def casefold(self):
        """
        Return a version of the string suitable for caseless comparisons.
        """
        ret = self.string.casefold()
        return BetterString(ret)

    def center(self, width: int, fillchar: str = ' '):
        """
        Return S centered in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space)
        """
        ret = self.string.center(int(width), str(fillchar))
        return BetterString(ret)

    def expandtabs(self, tabsize: int = 8):
        """
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        ret = self.string.expandtabs(int(tabsize))
        return BetterString(ret)

    def format(self, *args, **kwargs):
        """
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        ret = self.string.format(*args, **kwargs)
        return ret

    def format_map(self, mapping):
        """
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        ret = self.string.format_map(mapping)
        return BetterString(ret)

    def join(self, iterable):
        """
        Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        """
        ret = self.string.join(iterable)
        return BetterString(ret)

    def ljust(self, width: int, fillchar: str = ' '):
        """
        Return S left-justified in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space).
        """
        if str(fillchar).lower() == "rickroll":
            print("Never Gonna Give You Up!")
        ret = self.string.ljust(int(width), str(fillchar))
        return BetterString(ret)

    def lstrip(self, chars: str = None):
        """
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is a str, it will be converted to unicode before stripping
        """
        if chars is None:
            ret = self.string.lstrip(chars)
        else:
            ret = self.string.lstrip(str(chars))
        return BetterString(ret)

    def rjust(self, width: int, fillchar: str = ' '):
        """
        Return S right-justified in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space).
        """
        ret = self.string.rjust(int(width), str(fillchar))
        return BetterString(ret)

    def rstrip(self, chars: str = None):
        """
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is a str, it will be converted to unicode before stripping
        """
        if chars is None:
            ret = self.string.rstrip(chars)
        else:
            ret = self.string.rstrip(str(chars))
        return BetterString(ret)

    def strip(self, chars: str = None):
        """
        Return a copy of the string S with leading and trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead. If chars
         is a str, it will be converted to unicode before stripping
        """
        if chars is None:
            ret = self.string.strip(chars)
        else:
            ret = self.string.strip(str(chars))
        return BetterString(ret)

    def swapcase(self):
        """
        Return a copy of S with uppercase characters converted to lowercase and vice versa.
        """
        ret = self.string.swapcase()
        return BetterString(ret)

    def title(self):
        """
        Return a titlecased version of S, i.e. words start with title case characters, all
        remaining cased characters have lower case.
        """
        ret = self.string.title()
        return BetterString(ret)

    def translate(self, table):
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

    def zfill(self, width: int):
        """
        Pad a numeric string S with zeros on the left, to fill a field of the specified width.
        The string S is never truncated.
        """
        ret = self.string.zfill(int(width))
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

    def __call__(self):
        raise StringNotCallable()

    def __repr__(self):
        ret = f"BetterStrings('{self.string}')"

        return BetterString(ret)

    def __add__(self, value: int or str):
        ret = self.string.__add__(str(value))
        return BetterString(ret)

    def __getnewargs__(self):
        ret = self.string.__getnewargs__()
        return BetterString(ret)

    def __mul__(self, value: int):
        ret = self.string.__mul__(int(value))
        return BetterString(ret)

    def __rmul__(self, value: int):
        ret = self.string.__rmul__(int(value))
        return BetterString(ret)

# Discord: Peter | Btw. SCHINKEN!!1!!11#0930
