from .Exceptions import *


class bcolors:
    """
    Usage:
    bcolor.color_you_want + "your string" + bcolor.ENDC
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colorize(text, color, bold=False, underline=False) -> str:
    """
    Takes the text and colorizes it.
    Additional features:
    Make text bold
    Make text underlined
    """
    try:
        ret = f"{colors[str(color).lower()]}"
    except KeyError:
        raise ColorNotFoundError(color.lower()) from None

    if bold:
        ret += special['bold']
    if underline:
        ret += special['underline']

    ret += str(text) + special['endline']

    return ret


colors = {"blue": bcolors.OKBLUE,
          "cyan": bcolors.OKCYAN,
          "green": bcolors.OKGREEN,
          "orange":  bcolors.WARNING,
          "red": bcolors.FAIL}

special = {"endline": bcolors.ENDC,
           "bold": bcolors.BOLD,
           "underline": bcolors.UNDERLINE}


# Test
if __name__ == "__main__":
    print(colorize("Test Text", "blue", True, True))

    try:
        colorize("Test Text", "wrong color 123", False, True)
    except ColorNotFoundError as e:
        print(e)

    colorize("test text", "tsesdgsd")
