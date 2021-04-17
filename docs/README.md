# Docs
Some arg names are a bit weird because I don't know how to name them   

## Features:   
[upper](#upper)   
[lower](#lower)     
[to_list](#to_list)  
[to_dict](#to_dict)   
[to_int](#to_int)    
[colorize](#colorize)   
[count](#count)   

### upper
Better upper function. You can choose how many characters will be upper size

`BetterString.upper(size [optional])`   
_size_ is default: Full size   

### lower
Better lower function. You can choose how many characters will be upper size

`BetterString.lower(size [optional])`   
size is default: Full size

### to_list
Converts your string into a list or a tuple!   
If the string is representing a list it will convert it to the represented list   
if not it will return every character of the string in a list   

`BetterString.to_list()`

### to_dict
Converts your string into a dictionary

`BetterString.to_dict()`

### to_int
Converts your string into an integer

`BetterString.to_int()`

### colorize
Colorizes the string with the given color    
Available colors: "blue", "cyan", "green", "orange", "red"   

`BetterString.colorize(color, bold [optional], underline [optional]) `    
_bold_ is default: False   
_underline_ is default: False   

### count
This counts how many times the pattern appears in the string.    
The pattern has to be a str if it is not it will be automatically converted    
**You can use regex**

`BetterString.count_pattern(pattern)`
