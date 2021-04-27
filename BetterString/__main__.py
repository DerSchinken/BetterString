import BetterString
import tabulate
import sys

docs = "https://github.com/DrBumm/BetterString/tree/main/docs"
github = "https://github.com/DrBumm/BetterString"

options = [
    # "--short, --long", "Description"
    ["-h,", "--help", "Shows this help"],
    ["-b,", "--bold", "Make text bold"],
    ["-ul,", "--underline", "Make text underlined"],
    ["-l,", "--lower", "Make text lowercase"],
    ["-u,", "--upper", "Make text uppercase"],
]

flags = {
    "help": False,
    "h": False,
    "bold": False,
    "b": False,
    "underline": False,
    "ul": False,
    "lower": False,
    "l": False,
    "upper": False,
    "u": False,
}


def print_help():
    print("Usage:\n  BetterString <Text> [options]\n")
    print("Options:")
    print("  " + tabulate.tabulate(options, tablefmt="plain").replace("\n", "\n  "))


def err(text):
    print("Err:", text)
    exit(-1)


try:
    str_text = sys.argv[1]
    if str_text == "-h" or str_text == "--help":
        print_help()
        exit()
except IndexError:
    print_help()
    str_text = ""
    exit()

i = 0
for arg in sys.argv[2:]:
    arg_found = False
    for option in options:
        try:
            if arg in [option[0].replace(",", ""), option[1]]:
                flags[arg.replace("-", "").replace("--", "")] = True
                arg_found = True
                break
        except IndexError:
            pass
    if not arg_found:
        err(f"Wrong argument '{arg}'")
    i += 1
if (flags["u"] or flags["upper"]) and (flags["l"] or flags["lower"]):
    err("upper and lower cannot be True at the same time")


if flags["h"] or flags["help"]:
    print_help()
    exit()

ret = ""
if flags["b"] or flags["bold"]:
    ret += BetterString.special.BOLD

if flags["ul"] or flags["underline"]:
    ret += BetterString.special.UNDERLINE

if flags["l"] or flags["lower"]:
    ret += str_text.lower()

if flags["u"] or flags["upper"]:
    ret += str_text.upper()

if not (flags["u"] or flags["upper"]) and not (flags["l"] or flags["lower"]):
    ret += str_text

ret += BetterString.special.ENDC

print(ret)
