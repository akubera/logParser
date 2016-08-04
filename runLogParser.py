from logParser import logParser
import sys

if len(sys.argv) >= 2:
    parser = logParser(sys.argv[1])
else:
    # bot = TwircBot()
    print("Please provide a file name")
