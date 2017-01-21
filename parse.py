import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Return a password.')
    parser.add_argument('n', type=int, nargs='?', help='number of words to generate', default=4)
    parser.add_argument('-C', action='store_const', const=True, help='allow capitalized words')

    argument = parser.parse_args(sys.argv[1:])
    test = vars(argument)
    print(test)

    return test
