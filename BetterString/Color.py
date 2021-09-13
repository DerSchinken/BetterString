from .Exceptions import ColorNotFoundError, BackgroundColorNotFound
from colorama import init, Fore, Back
from random import choice


init(autoreset=True)


class Colors:
    """
    Usage:
    Colors.color_you_want + "your string" + Special.ENDC
    """
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    BLACK = Fore.BLACK
    WHITE = Fore.WHITE
    YELLOW = Fore.YELLOW
    MAGENTA = Fore.MAGENTA


colors = Colors()


class BackgroundColors:
    """
    Usage:
    Colors.background_color_you_want + "your string" + Special.ENDC
    """
    BLACK = Back.BLACK
    RED = Back.RED
    GREEN = Back.GREEN
    YELLOW = Back.YELLOW
    BLUE = Back.BLUE
    CYAN = Back.CYAN
    WHITE = Back.WHITE
    MAGENTA = Back.MAGENTA


background_colors = BackgroundColors()


class Special:
    """
    Usage:
    Colors.effect_you_want + "your string" + Special.ENDC
    """
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
                           colors.YELLOW, colors.MAGENTA]
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
