from BetterString import *

test_string = BetterString("This is a Better String")

print(test_string.count_pattern("e"))
print(test_string.lower())
print(test_string.lower(3))
print(test_string.upper())
print(test_string.upper(3))
print(test_string.to_list())
print(test_string.colorize(BLUE))
print(test_string[4:], test_string[3], test_string["4"])
print(repr(test_string))

test_string = BetterString("['This represents a list', 'Test list']")
print(test_string.to_list())

test_string = BetterString("{'This represents a dictionary': 'Test Dictionary'}")
print(test_string.to_dict())

test_string = BetterString("1337")
print(test_string.to_int())
