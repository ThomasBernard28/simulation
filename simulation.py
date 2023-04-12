import re
import sys


def initialize(file):
    with open(file, "r") as f:
        e = f.read()
        # delete all \n from the e string
        new_e = re.sub(r'\n', '', e)
        # First two characters are 2. and they are not decimals
        decimals = list(new_e[2:])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        initialize(sys.argv[1])
    else:
        print("Please choose a file to exploit by giving it as argument")
        sys.exit(1)