from BetterString import *
# Tests for the errors

test_string = BetterString("This is an Better String")

try:
    test_string[12314232354325345]
except IndexError as IE:
    print(IE)

try:
    test_string[12312121212312:]
except Exceptions.IndexStartOutOfBoundError as ISOOB:
    print(ISOOB)

try:
    test_string.to_literal()
except Exceptions.CannotConvertToError as CCTE:
    print(CCTE)

try:
    test_string.to_literal()
except Exceptions.CannotConvertToError as CCTE:
    print(CCTE)

try:
    test_string()
except Exceptions.StringNotCallable as SNC:
    print(SNC)

try:
    test_string.colorize("wrong color")
except Exceptions.ColorNotFoundError as CNFE:
    print(CNFE)

try:
    test_string.upper(12311231313)
except ValueError as VE:
    print(VE)

try:
    test_string.lower(12311231313)
except ValueError as VE:
    print(VE)

try:
    test_string.upper("asdas1")
except TypeError as TE:
    print(TE)

try:
    test_string.lower("asdas1")
except TypeError as TE:
    print(TE)

try:
    test_string.swap(0, 1000)
except IndexError as IE:
    print(IE)
try:
    test_string.swap(1000, 0)
except IndexError as IE:
    print(IE)
try:
    test_string.swap(0, "10t00")
except TypeError as TE:
    print(TE)
try:
    test_string.swap("100t0", 0)
except TypeError as TE:
    print(TE)
