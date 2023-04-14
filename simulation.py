import re


def initialize(file):
    with open(file, "r") as f:
        e = f.read()
        # delete all \n from the e string
        new_e = re.sub(r'\n', '', e)
        # First two characters are 2. and they are not decimals
        decimals = [int(i) for i in new_e[2:]]
        chiSquared(decimals)


# each interval should have the same value if the data is random
# the expected value is the number of data divided by the number of intervals
# the observed value is the number of data in each interval
def chiSquared(data):
    intervals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for d in data:
        tmp = intervals[d]
        tmp += 1
        intervals[d] = tmp
    print(intervals)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        initialize(sys.argv[1])
    else:
        print("Please choose a file to exploit by giving it as argument")
        sys.exit(1)
