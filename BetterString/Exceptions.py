class IndexStartOutOfBoundError(Exception):
    def __init__(self):
        super().__init__("Index start is out of bounds!")


class StringCannotBeConverted(Exception):
    def __init__(self, string, convert_type):
        super().__init__(f"String: '{string}' cannot be converted to type: '{convert_type}'!")


class StringNotCallable(Exception):
    def __init__(self):
        super().__init__("String not callable!")


class ColorNotFoundError(Exception):
    def __init__(self, color):
        super().__init__(f"Color '{color}' not found!")


class CannotConvertToError(Exception):
    def __init__(self, type):
        super().__init__(f"Cannot convert the string to type {type}!")
