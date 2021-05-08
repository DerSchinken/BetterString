### BetterString.replace
Return a copy with all occurrences of substring old replaced by new.
You don't have to define new it is now default ""  
**You can use regex**   

`BetterString.replace(old, new [optional], count [optional], regex [optional])`    
new default is: ""     
count default is: [size of text]         
regex default is: False    

Example:
```python 
import BetterString

test_string = BetterString.BetterString("This Is A Test String")

print(test_string.replace("e"))
print(test_string.replace("\\w", regex=True))
```
