### BetterString.upper
Better upper function. You can set start and end

`BetterString.upper(end [optional], start [optional])`   
_end_ is default: [size of text]      
_start_ is default: 0    

Example:
```python 
import BetterString

test_string = BetterString.BetterString("This Is A Test String")

print(test_string.upper())
print(test_string.upper(6))
print(test_string.upper(3, 1))
print(test_string.upper(start=1, end=3))
```
