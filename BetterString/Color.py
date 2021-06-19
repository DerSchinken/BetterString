from .Exceptions import *
from random import choice


class Colors:
    """
    Usage:
    tcolors.color_you_want + "your string" + tcolors.ENDC
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


def rainbow(text):
    ret = ""
    color_list = [colors.CYAN, colors.RED, colors.BLACK, colors.BLUE, colors.GREEN, colors.WHITE, colors.ORANGE, colors.PURPLE, colors.YELLOW]
    try:
        i = 0
        while True:
            if not text[i] == " ":
                ret += choice(color_list) + text[i]
            else: ret += " "
            i += 1
    except IndexError:
        return ret + Special.ENDC
