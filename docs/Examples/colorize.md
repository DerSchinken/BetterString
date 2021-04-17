### colorize
Colorizes the string with the given color    
Available colors: `"blue", "cyan", "green", "orange", "red"  `    
Or you use the variables from the package:  
`BetterString.BLUE, BetterString.CYAN, BetterString.GREEN,
BetterString.ORANGE, BetterString.RED`

`BetterString.colorize(color, bold [optional], underline [optional]) `    
_bold_ is default: False   
_underline_ is default: False   

Example:   
```python
import BetterString

test_string = BetterString.BetterString("This Is A Test String!")

print(test_string.colorize(BetterString.BLUE))
print(test_string.colorize("blue"))
```
