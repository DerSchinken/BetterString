from string import ascii_lowercase as lc, ascii_uppercase as uc
from functools import wraps
from .Color import *
from .Exceptions import *
import re
import random
import hashlib

# Important: Always put out new version on PyPI before pushing to github

FULL_SIZE = "fs"
START = 0

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


# Decorators
def shuffle_funcs(f):
    @wraps(f)
    def wrapper(*args):
        ret = ""
        indexes_done = []
        while True:
            index = random.randint(0, len(args[0].string) - 1)
            if index not in indexes_done:
                ret += args[0].string[index]
                indexes_done.append(index)
            elif len(indexes_done) == len(args[0].string):
                break

        return f(args[0], ret)

    return wrapper


# Dummy so we can use it for function annotations
# I could use from __future__ import annotations
# but that is only available for python 3.7+
class BetterString(object):
    pass


# noinspection PyRedeclaration
# ^ so PyCharm doesn't cry cuz we redeclare this class
class BetterString(str):
    """
    This returns a string with more functionality!
    BetterString has the same functions as str with a few extras and changes
    """

    def __init__(self, string):
        self.string = str(string)

    def lower(self, end=FULL_SIZE, start=START) -> BetterString:
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

    def upper(self, end=FULL_SIZE, start=START) -> BetterString:
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

    def list(self) -> list:
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

    def int(self) -> int:
        """
        Converts your string into an integer
        """
        try:
            return int(self.string)
        except ValueError:
            raise CannotConvertToError("int")

    def dict(self) -> dict:
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

    def str(self) -> str:
        """
        Returns the String
        """
        return self.string

    def colorize(self, color=None, bg=None, bold=False, underline=False, start=START, end=FULL_SIZE) -> BetterString:
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

        return BetterString(
            colorize(text=self.string, color=color, bold=bold, underline=underline, bg=bg, start=start, end=end))

    @shuffle_funcs
    def shuffle(self, ret) -> BetterString:
        """
        Shuffles the string
        """
        return BetterString(ret)

    @shuffle_funcs
    def bomb(self, ret) -> BetterString:
        """
        Shuffles the string but an random amount of characters will disintegrate
        """
        return BetterString(ret[:random.randint(0, len(self.string) - 1)])

    def rainbow(self) -> BetterString:
        """
        Makes the string rainbow colored
        """
        return BetterString(rainbow(text=self.string))

    def sha512(self) -> str:
        """
        Returns the sha512 value of the string
        """
        return hashlib.sha512(self.string.encode()).hexdigest()

    def sha256(self) -> str:
        """
        Returns the sha256 value of the string
        """
        return hashlib.sha256(self.string.encode()).hexdigest()

    def sha1(self) -> str:
        """
        Returns the sha1 value of the string
        """
        return hashlib.sha1(self.string.encode()).hexdigest()

    def rot(self, rot=13) -> BetterString:
        """
        Caesar encryption

        :param rot: rotation
        """
        rot = str.maketrans(lc + uc, lc[rot:] + lc[:rot] + uc[rot:] + uc[:rot])

        return BetterString(self.string.translate(rot))

    def binary(self, list_=False) -> list or BetterString:
        """
        Returns the binary of the string

        :param list_: Set to True if return should be a list
        """
        if not isinstance(list_, bool):
            raise TypeError("'list_' has to be of type 'bool'!")

        ret = []
        for byte in bytearray(self.string, "utf-8"):
            ret.append(bin(byte).replace("0b", ""))

        if list_:
            return ret
        elif not list_:
            return BetterString(' '.join(ret))

        # return BetterString(' '.join([bin(x) for x in bytearray(self.string, "utf-8")])).remove("0b") if not list_ else [bin(x).replace("0b", "") for x in bytearray(self.string, "utf-8")]
        # ^ Ez oneliner; but it is not checking the type of list_

    def hex(self):
        """
        Returns the hex of the string
        """
        return self.string.encode().hex()

    def count(self, pattern, start: int = START, end: int = FULL_SIZE, regex: bool = False) -> int:
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

    def replace(self, old: str, new: str = "", count: int = FULL_SIZE, regex: bool = False) -> BetterString:
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

    def remove(self, pattern: str, count: int = FULL_SIZE, regex: bool = False) -> BetterString:
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
        return BetterString(ret)

    def capitalize(self) -> BetterString:
        """
        Return a capitalized version of S, i.e. make the first
        character have upper case and the rest lower case.
        """
        ret = self.string.capitalize()
        return BetterString(ret)

    def casefold(self) -> BetterString:
        """
        Return a version of the string suitable for caseless comparisons.
        """
        ret = self.string.casefold()
        return BetterString(ret)

    def center(self, width: int, fillchar: str = ' ') -> BetterString:
        """
        Return S centered in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space)
        """
        ret = self.string.center(int(width), str(fillchar))
        return BetterString(ret)

    def expandtabs(self, tabsize: int = 8) -> BetterString:
        """
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        ret = self.string.expandtabs(int(tabsize))
        return BetterString(ret)

    def format(self, *args, **kwargs) -> BetterString:
        """
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        ret = self.string.format(*args, **kwargs)
        return BetterString(ret)

    def format_map(self, mapping) -> BetterString:
        """
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        ret = self.string.format_map(mapping)
        return BetterString(ret)

    def join(self, iterable) -> BetterString:
        """
        Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        """
        ret = self.string.join(iterable)
        return BetterString(ret)

    def ljust(self, width: int, fillchar: str = ' ') -> BetterString:
        """
        Return S left-justified in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space).
        """
        if str(fillchar).lower() == "rickroll":
            print("Never Gonna Give You Up!")
        ret = self.string.ljust(int(width), str(fillchar))
        return BetterString(ret)

    def lstrip(self, chars: str = None) -> BetterString:
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

    def rjust(self, width: int, fillchar: str = ' ') -> BetterString:
        """
        Return S right-justified in a Unicode string of length width.
        Padding is done using the specified fill character (default is a space).
        """
        ret = self.string.rjust(int(width), str(fillchar))
        return BetterString(ret)

    def rstrip(self, chars: str = None) -> BetterString:
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

    def strip(self, chars: str = None) -> BetterString:
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

    def swapcase(self) -> BetterString:
        """
        Return a copy of S with uppercase characters converted to lowercase and vice versa.
        """
        ret = self.string.swapcase()
        return BetterString(ret)

    def title(self) -> BetterString:
        """
        Return a titlecased version of S, i.e. words start with title case characters, all
        remaining cased characters have lower case.
        """
        ret = self.string.title()
        return BetterString(ret)

    def translate(self, table) -> BetterString:
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

    def zfill(self, width: int) -> BetterString:
        """
        Pad a numeric string S with zeros on the left, to fill a field of the specified width.
        The string S is never truncated.
        """
        ret = self.string.zfill(int(width))
        return BetterString(ret)

    # Magic methods
    def __getitem__(self, item: int or slice) -> BetterString:
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
        return '"' + self.string + '"'

    def __add__(self, value: int or str) -> BetterString:
        ret = self.string.__add__(str(value))
        return BetterString(ret)

    def __getnewargs__(self) -> BetterString:
        ret = self.string.__getnewargs__()
        return BetterString(ret)

    def __mul__(self, value: int) -> BetterString:
        ret = self.string.__mul__(int(value))
        return BetterString(ret)

    def __rmul__(self, value: int) -> BetterString:
        ret = self.string.__rmul__(int(value))
        return BetterString(ret)

# Discord: Peter | Btw. SCHINKEN!!1!!11#0930
