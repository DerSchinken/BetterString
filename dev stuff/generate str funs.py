from inspect import signature
import inspect

already_done = [
# First all __ funcs
"__init__", "__repr__", "__doc__", 
"__getitem__", "__call__", "" 

# next all other funcs
"lower", "upper", "to_list", "to_int", "to_dict",
"colorize", "count", "replace"
]

file = open("generated_funcs.py", "w")

code = """
def {func_name}({args}) -> str:
	ret = self.string.{func_name}({args_})
	return BetterString(ret)
"""

sig = '(self)'

str_funcs = dir(str)

for func in str_funcs:
	if func in already_done:
		pass
	else:
		try:
			file.write(code.format(
				func_name=func,
				args=str(signature(eval(f"str.{func}"))).replace("(", "").replace(")", ""),
				args_=str(signature(eval(f"str.{func}"))).replace("(", "").replace(")", "").replace("self, ", "").replace(", /", ""),
			))
		except ValueError:
			file.write(code.format(
				func_name=func,
				args="self",
				args_="",
			))
