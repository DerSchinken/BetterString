### BetterString.remove
Return a copy with all occurrences of substring patter replaced with "".   
**You can use regex**     
 
`BetterString.remove(pattern, count [optional], regex [optional])`   
count default is: [size of text]      
regex default is: False     

  
Example:   
```python 
import BetterString

test_string = BetterString.BetterString("This Is A Test String")

print(test_string.remove("e"))
print(test_string.remove("\\w", regex=True))
```
