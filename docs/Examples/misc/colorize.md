### BetterString.colorize
Colorizes the string with the given color      
Available colors:    
`'BLUE', 'CYAN', 'GREEN', 'ORANGE', 'RED', 'BLACK', 'PURPLE', 'WHITE', 'YELLOW'`            
Or you use the variables from the package:     
`'BetterString.BLUE', 'BetterString.CYAN', 'BetterString.GREEN', 'BetterString.ORANGE', 'BetterString.RED', 'BetterString.BLACK', 'BetterString.PURPLE', 'BetterString.WHITE', 'BetterString.YELLOW'`    

Available background colors:   
`'BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'PURPLE', 'CYAN', 'WHITE'`    
Or you use the variables from the package:   
`'BetterString.BLACK_BG', 'BetterString.RED_BG', 'BetterString.GREEN_BG', 'BetterString.YELLOW_BG', 'BetterString.BLUE_BG', 'BetterString.PURPLE_BG', 'BetterString.CYAN_BG', 'BetterString.WHITE_BG'`    

`BetterString.colorize(color [optional], bg [optional],  bold [optional], underline [optional], start [optional], end [optional]) `     
_bold_ is default: False   
_underline_ is default: False   
_bg_ is default: None   
_start_ is default: 0   
_end_ is default: [size of text]    

Example:   
```python 
import BetterString

test_string = BetterString.BetterString("This Is A Test String!")

print(test_string.colorize(color=BetterString.BLUE))
print(test_string.colorize(color="blue"))
```
