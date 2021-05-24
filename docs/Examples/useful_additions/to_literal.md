### BetterString.int
Returns the string converted to its literal

`BetterString.to_literal()`

Example:
```python 
import BetterString

test_string = BetterString("['This represents a list', 'Test list']")
print(test_string.to_literal())

test_string = BetterString("{'This represents a dictionary': 'Test Dictionary'}")
print(test_string.to_literal())

test_string = BetterString("1337")
print(test_string.to_literal())
# and so on
```
