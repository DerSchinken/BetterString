### remove
Return a copy with all occurrences of substring patter replaced with "".   
**You can use regex**     
 
`BetterString.remove(pattern, count [optional])`   
count default is: FULL_SIZE (full size of the string)    
  
Example:   
```python 
import BetterString

test_string = BetterString.BetterString("This Is A Test String")

print(test_string.remove("e"))
print(test_string.remove("\\w"))
```
