import sys
import re


class EDecimals:
    def __init__(self, file):
        self.file = file
        self.decimals = self.initialize()

    def initialize(self):
        try:
            with open(self.file, "r") as f:
                e = f.read()
                # delete all \n from the e string
                new_e = re.sub(r'\n', '', e)
                # First two characters are 2. and they are not decimals
                decimals = [int(i) for i in new_e[2:]]
                return decimals
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)