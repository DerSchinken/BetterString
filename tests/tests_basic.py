from BetterString import *

# Basic Tests

test_string = BetterString("This is a Better String")

print(test_string.count("e"))
print(test_string.lower())
print(test_string.lower(3))
print(test_string.lower(3, 1))
print(test_string.lower(start=1, end=3))
print(test_string.upper())
print(test_string.upper(3))
print(test_string.upper(3, 1))
print(test_string.upper(start=1, end=3))
print(test_string.list())
print(test_string.colorize(color=BLUE))
print(test_string.colorize(color=BLUE, bg="yellow", bold=True, underline=True, start=4))
print(test_string.colorize(color=BLUE, bg="yellow", end=4))
print(test_string[4:], test_string[3], test_string["4"])
print(repr(test_string))
print(test_string.rainbow())
print(test_string.str())
print(test_string.bomb())
print(test_string.shuffle())
print(test_string.rot())
print(test_string.rot(15))
print(test_string.sha512())
print(test_string.sha256())
print(test_string.sha1())

print(test_string.remove("e"))
print(test_string.remove("e", count=3))
print(test_string.remove("\\w", regex=True))
print(test_string.remove("\\w", regex=True, count=6))

print(test_string.replace("e"))
print(test_string.replace("e", count=3))
print(test_string.replace("\\w", regex=True))
print(test_string.replace("\\w", regex=True, count=6))
print(test_string.replace("e", "t"))
print(test_string.replace("e", "t", count=3))
print(test_string.replace("\\w", "t", regex=True))
print(test_string.replace("\\w", "t", regex=True, count=6))

print(test_string.count("e"))
print(test_string.count("\\w", regex=True))

test_string = BetterString("['This represents a list', 'Test list']")
print(test_string.list())

test_string = BetterString("{'This represents a dictionary': 'Test Dictionary'}")
print(test_string.dict())

test_string = BetterString("1337")
print(test_string.int())

# Some normal str funcs to verify that they work
test_string = BetterString("{} String")
print(test_string.format("Test"))
print(test_string.join(["t", "e", "s", "t"]))

test_string = BetterString("{test} {test} {} String")
print(test_string.format("tessst", test="Test"))

print(test_string.binary())
print(test_string.binary(False))
print(test_string.binary(True))

print(test_string.hex())

print(test_string.swap(0, 2))
print(test_string.swap(2, 0))
