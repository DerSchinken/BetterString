from .Exceptions import BackgroundColorNotFound as BackgroundColorNotFound, ColorNotFoundError as ColorNotFoundError
from typing import Any

class Colors:
    BLUE: Any
    CYAN: Any
    GREEN: Any
    RED: Any
    BLACK: Any
    WHITE: Any
    YELLOW: Any
    MAGENTA: Any

colors: Any

class BackgroundColors:
    BLACK: Any
    RED: Any
    GREEN: Any
    YELLOW: Any
    BLUE: Any
    CYAN: Any
    WHITE: Any
    MAGENTA: Any

background_colors: Any

class Special:
    ENDC: str
    BOLD: str
    UNDERLINE: str

def colorize(**kwargs) -> str: ...
def rainbow(text: str) -> str: ...
