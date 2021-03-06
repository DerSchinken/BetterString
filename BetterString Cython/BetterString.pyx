from string import ascii_lowercase as lc, ascii_uppercase as uc
from hashlib import sha1, sha256, sha512
from typing import Tuple, Any, Iterator
from random import randint, choice
from itertools import permutations
from functools import wraps
from re import sub, findall


# Important: Always put out new version on PyPI before pushing to github

FULL_SIZE = "full_size"
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
    # randoms shuffle function doesn't work
    # idk why but it just doesn't return anything
    @wraps(f)
    def wrapper(*args):
        # Checking that there are no args
        if len(args) > 1:
            raise TypeError(f"{f.__name__} takes 1 positional arguments but {len(args)} was given")

        ret, indexes_done = "", []
        # While not every char is done
        # choose a random char put it to the ret
        # append the char index to indexes done
        # if indexes done has the length of the string
        # break
        while True:
            index = randint(0, len(args[0].string) - 1)
            if index not in indexes_done:
                ret += args[0].string[index]
                indexes_done.append(index)
            elif len(indexes_done) == len(args[0].string):
                break

        return f(args[0], ret)

    return wrapper


class IndexStartOutOfBoundError(Exception):
    def __init__(self):
        super().__init__("Index start is out of bounds!")


class StringNotCallable(Exception):
    def __init__(self):
        super().__init__("String not callable!")


class ColorNotFoundError(Exception):
    def __init__(self, color: str):
        super().__init__(f"Color '{color}' not found!")


class BackgroundColorNotFound(Exception):
    def __init__(self, color: str):
        super().__init__(f"Background color '{color}' not found!")


class CannotConvertToError(Exception):
    def __init__(self):
        super().__init__(f"Cannot convert the string!")




class Colors:
    """
    Usage:
    Colors.color_you_want + "your string" + Special.ENDC
    """
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    BLACK = '\033[30m'
    PURPLE = '\033[35m'
    WHITE = '\033[37m'
    YELLOW = '\033[43'


colors = Colors()


class BackgroundColors:
    BLACK = '\033[93m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[35m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'


background_colors = BackgroundColors()


class Special:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colorize(**kwargs) -> str:
    """
    Takes the text and colorizes it.
    Additional features:
    Change background
    Make text bold
    Make text underlined
    """
    # Get text
    try:
        text = kwargs["text"]
        if not isinstance(text, str):
            raise TypeError("'text' has to be of type 'str'")
    except KeyError:
        raise TypeError("You need to give a text!")

    # Get color
    try:
        color = kwargs["color"]
    except KeyError:
        color = None

    # Get background or bg (short for background)
    try:
        bg = kwargs["background"]
    except KeyError:
        try:
            bg = kwargs["bg"]
        except KeyError:
            bg = None

    # Get bold
    try:
        bold = kwargs["bold"]
        if not isinstance(bold, bool):
            raise TypeError("'bold' has to be of type 'bool'!")
    except KeyError:
        bold = False

    # Get underline
    try:
        underline = kwargs["underline"]
        if not isinstance(underline, bool):
            raise TypeError("'underline' has to be of type 'bool'!")
    except KeyError:
        underline = False

    # Get start
    try:
        start = int(kwargs["start"])
    except KeyError:
        start = 0
    except TypeError:
        raise TypeError("'start' has to be of type 'int'!") from None
    # Get end
    try:
        end = int(kwargs["end"])
    except KeyError:
        end = len(text)
    except TypeError:
        raise TypeError("'end' has to be of type 'int'!") from None

    ret = text[:start]
    if color:
        try:
            ret += colors.__getattribute__(color.upper())
        except AttributeError:
            raise ColorNotFoundError(color.lower()) from None

    if bg:
        try:
            ret += background_colors.__getattribute__(bg.upper())
        except AttributeError:
            raise BackgroundColorNotFound(bg.lower()) from None

    if bold:
        ret += Special.BOLD
    if underline:
        ret += Special.UNDERLINE

    ret += text[start:end]
    ret += Special.ENDC
    ret += text[end:]

    return ret


def rainbow(text: str) -> str:
    ret, color_list = "", [colors.CYAN, colors.RED, colors.BLACK, colors.BLUE, colors.GREEN, colors.WHITE,
                           colors.ORANGE, colors.PURPLE, colors.YELLOW]
    try:
        i = 0
        while True:
            if not text[i] == " ":
                ret += choice(color_list) + text[i]
            else:
                ret += " "
            i += 1
    except IndexError:
        return ret + Special.ENDC


class BetterString(str):
    """
    This returns a string with more functionality!
    BetterString has the same functions as str with a few extras and changes
    """

    def __init__(self, string: str):
        self.string = str(string)

    def lower(self, end: int = FULL_SIZE, start: int = START):
        """
        Better Upper function. You can
        choose how many characters will
        be upper size
        """
        lower_string, i = "", 0
        # Getting full size
        if end == FULL_SIZE:
            end = len(self.string)
        # Checking if everything has the right type or can be converted to the right type
        elif isinstance(end, str):
            try:
                end = int(end)
            except ValueError:
                raise TypeError("end has to be of type Int") from None
        if isinstance(start, str):
            try:
                start = int(start)
            except ValueError:
                raise TypeError("start has to be of type Int") from None

        # Checking that nothing is to big
        if end > len(self.string):
            raise ValueError(f"'end' of {end} is to big!")
        if start > len(self.string):
            raise ValueError(f"'start' of {start} is to big")

        for i in range(start, end):
            if i <= end:
                lower_string += self.string[i].lower()

        lower_string += self.string[i + 1:]

        return BetterString(lower_string)

    def upper(self, end: int = FULL_SIZE, start: int = START):
        """
        Better Upper function. You can
        choose how many characters will
        be upper size
        """
        upper_string, i = "", 0
        # Getting full size
        if end == FULL_SIZE:
            end = len(self.string)
        # Checking if everything has the right type or can be converted to the right type
        elif isinstance(end, str):
            try:
                end = int(end)
            except ValueError:
                raise TypeError("Size has to be of type Integer") from None
        if isinstance(start, str):
            try:
                start = int(start)
            except ValueError:
                raise TypeError("Start has to be of type Int") from None

        # Checking that nothing is to big
        if end > len(self.string):
            raise ValueError(f"Size of {end} is to big!")
        if start > len(self.string):
            raise ValueError(f"'start' of {start} is to big")

        for i in range(start, end):
            if i <= end:
                upper_string += self.string[i].upper()

        upper_string += self.string[i + 1:]

        return BetterString(upper_string)

    def to_literal(self):
        """
        Returns the string converted to its literal
        """
        try:
            converted = eval(self.string)
            return converted
        except SyntaxError:
            raise CannotConvertToError from None

    def str(self) -> str:
        """
        Returns the String
        """
        return self.string

    def colorize(self, color: str = None, bg: str = None, bold: bool = False, underline: bool = False,
                 start: int = START, end: int = FULL_SIZE):
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
        # If nothing is set change nothing and return self
        if color is None and \
                bg is None and \
                bold is False and \
                underline is False and \
                start == START and end == FULL_SIZE:
            return self

        # Getting full size
        if end == FULL_SIZE:
            end = len(self.string)

        return BetterString(
            colorize(
                text=self.string,
                color=color,
                bold=bold,
                underline=underline,
                bg=bg,
                start=start,
                end=end
            )
        )

    @shuffle_funcs
    def shuffle(self, ret):
        """
        Shuffles the string
        """
        return BetterString(ret)

    @shuffle_funcs
    def bomb(self, ret):
        """
        Shuffles the string but an random amount of characters will disintegrate
        """
        return BetterString(ret[:randint(0, len(self.string) - 1)])

    def permutations(self) -> Iterator[Tuple[Any, ...]]:
        """
        returns all permutations of the string
        """
        # We are returning the itertools.permutations object
        # because if we convert it to a list this would
        # take an eternity depending on the length of the string
        return permutations(self.string)

    def rainbow(self):
        """
        Makes the string rainbow colored
        """
        return BetterString(rainbow(self.string))

    def sha512(self) -> str:
        """
        Returns the sha512 value of the string
        """
        return sha512(self.string.encode()).hexdigest()

    def sha256(self) -> str:
        """
        Returns the sha256 value of the string
        """
        return sha256(self.string.encode()).hexdigest()

    def sha1(self) -> str:
        """
        Returns the sha1 value of the string
        """
        return sha1(self.string.encode()).hexdigest()

    def rot(self, rot: int = 13):
        """
        Caesar encryption

        :param rot: rotation
        """
        rot = str.maketrans(lc + uc, lc[rot:] + lc[:rot] + uc[rot:] + uc[:rot])

        return BetterString(self.string.translate(rot))

    def binary(self, liste: bool = False) -> list:
        """
        Returns the binary of the string

        :param liste: Set to True if return should be a list
        """
        # liste is german for list
        if not isinstance(liste, bool):
            raise TypeError("'liste' has to be of type 'bool'!")

        # Iterating over all characters and converting them to binary
        ret = []
        for byte in bytearray(self.string, "utf-8"):
            ret.append(bin(byte).replace("0b", ""))

        if liste:
            return ret
        elif not liste:
            return BetterString(' '.join(ret))

        # return BetterString(' '.join([bin(x) for x in bytearray(self.string, "utf-8")])).remove("0b") if not liste
        # else [bin(x).replace("0b", "") for x in bytearray(self.string, "utf-8")] ^ Ez oneliner; but it is not
        # checking the type of liste

    def hex(self):
        """
        Returns the hex of the string
        """
        return self.string.encode().hex()

    def count(self, pattern: str, start: int = START, end: int = FULL_SIZE, regex: bool = False) -> int:
        """
        This counts how many time the pattern appears
        in the string.
        The pattern has to be a str if it is not it
        will be automatically converted

        **You can use regex**
        """
        # Getting the full size
        if end == FULL_SIZE:
            end = len(self.string)

        if regex:
            ret = len(findall(str(pattern), self.string[start:end]))
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
        # Getting the full size
        if count == FULL_SIZE:
            count = len(self.string)

        if regex:
            ret = sub(old, new, self.string, count)
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
        # Getting the full size
        if count == FULL_SIZE:
            count = len(self.string)

        if regex:
            ret = sub(str(pattern), "", self.string, count)
        else:
            ret = self.string.replace(pattern, "", count)

        return BetterString(ret)

    def swap(self, index1: int, index2: int):
        """
        Swaps character with index of index1 with character of index index2
        """
        # Checking if index1 and index2 is of type int
        # if not try to convert them
        if not isinstance(index1, int):
            try:
                index1 = int(index1)
            except ValueError:
                raise TypeError("index1 has to be of type int!") from None
        if not isinstance(index2, int):
            try:
                index2 = int(index2)
            except ValueError:
                raise TypeError("index2 has to be of type int!") from None

        # Turning the string into an list because
        # strings are immutable but lists are mutable
        tmp_new_string = list(self.string)
        try:
            # Getting the chars of both indexes
            index1_char = tmp_new_string[index1]
            index2_char = tmp_new_string[index2]

            # Swapping
            tmp_new_string[index1] = index2_char
            tmp_new_string[index2] = index1_char

            # Putting the new string together
            new_string = ''.join(tmp_new_string)
        except IndexError:
            raise IndexError("string index out of bounds") from None

        return BetterString(new_string)

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

        return BetterString(ret)

    def format_map(self, mapping):
        """
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        ret = self.string.format_map(mapping)

        return BetterString(ret)

    def join(self, iterable: Iterator):
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

    # easter egg warning
    def schinken_hash(self) -> str:
        string, char_decs, char_sum, result = str(self.string), [], 0, 0

        # getting the sum of all chars and appending the char decs to a list
        for char in string:
            char_sum += ord(char)
            char_decs.append(ord(char))
        # result += every char dec ** sum of all chars + length of the string
        for char_dec in char_decs:
            result += char_dec ** char_sum + len(string)

        # return hex value of result removing the 0x and only display half - the length of the string
        return hex(result)[2:int(len(hex(result)) / len(string))]

        # Short
        # string_hex = hex(sum([ord(char)**sum(map(ord, self.string))+len(self.string) for char in self.string]))
        # return "SCH" + string_hex[2:int(len(string_hex)/len(self.string))]

    def zfill(self, width: int):
        """
        Pad a numeric string S with zeros on the left, to fill a field of the specified width.
        The string S is never truncated.
        """
        ret = self.string.zfill(int(width))

        return BetterString(ret)

    # Magic methods
    def __getitem__(self, item):
        """
        item has to be int or slice
        if it is an str it will try to convert the str into an int
        """
        ret = None

        if isinstance(item, str):
            try:
                item = int(item)
            except ValueError:
                raise TypeError("String indices must be integers") from None

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

    def __add__(self, value):
        ret = self.string.__add__(str(value))

        return BetterString(ret)

    def __getnewargs__(self) -> tuple:
        return self.string.__getnewargs__()

    def __mul__(self, value: int):
        ret = self.string.__mul__(int(value))

        return BetterString(ret)

    def __rmul__(self, value: int):
        ret = self.string.__rmul__(int(value))

        return BetterString(ret)


# Discord: Peter | Btw. SCHINKEN!!1!!11#0930
