### BetterString.list
Converts your string into a list or a tuple!   
If the string is representing a list it will convert it to the represented list   
if not it will return every character of the string in a list   

`BetterString.list()`

Example:
```python 
import BetterString

test_string = BetterString.BetterString("This Is A Test String")

print(test_string.list())

test_string = BetterString.BetterString("[1, 2, 3, 'Test']")

print(test_string.list())
```
