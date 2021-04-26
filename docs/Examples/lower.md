
### lower
Better lower function. You can set start and end

`BetterString.lower(end [optional], start [optional])`   
_end_ is default: Full size    
_start_ is default: 0    

Example:    
```python 
import BetterString

test_string = BetterString.BetterString("This Is A Test String")

print(test_string.lower())
print(test_string.lower(6))
print(test_string.lower(3, 1))
print(test_string.lower(start=1, end=3))
```
