class IndexStartOutOfBoundError(Exception):
    def __init__(self):
        super().__init__("Index start is out of bounds!")


class StringNotCallable(Exception):
    def __init__(self):
        super().__init__("String not callable!")


class ColorNotFoundError(Exception):
    def __init__(self, color):
        super().__init__(f"Color '{color}' not found!")


class BackgroundColorNotFound(Exception):
    def __init__(self, color):
        super().__init__(f"Background color '{color}' not found!")


class CannotConvertToError(Exception):
    def __init__(self):
        super().__init__(f"Cannot convert the string!")
