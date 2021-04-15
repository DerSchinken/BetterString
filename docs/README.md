# Docs
Some arg names are a bit weird because I don't know how to name them

### upper
BetterString.upper(size [optional])

Better upper function. You can choose how many characters will be upper size

BetterString.upper(size: int=FULL_SIZE) -> str

### lower
BetterString.lower(size [optional])

Better lower function. You can choose how many characters will be upper size

BetterString.lower(size: int=FULL_SIZE) -> str

### to_list
BetterString.to_list()    

Converts your string into a list or a tuple!   
If the string is representing a list it will convert it to the represented list   
if not it will return every character of the string in a list   

BetterString.to_list() -> list

### to_dict
BetterString.to_dict()

Converts your string into a dictionary

BetterString.to_dict() -> dict

### to_int
BetterString.to_int()

Converts your string into an integer

BetterString.to_int() -> int

### colorize 
BetterString.colorize(color, bold [optional], underline [optional])     

Colorizes the string with the given color    
Available colors: "blue", "cyan", "green", "orange", "red"   

BetterString.colorize(color: str, bold: bool = False, underline: bool = False) -> str   

### count_pattern
BetterString.count_pattern(pattern)

This counts how many times the pattern appears in the string.    
The pattern has to be a str if it is not it will be automatically converted    
**You can use regex**

BetterString.count_pattern(pattern: str) -> int
