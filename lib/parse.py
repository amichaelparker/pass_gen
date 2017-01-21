''' Module for parsing command line arguments '''

import argparse
import sys

def parse_arguments():
    ''' Construct argument parser and available arguments, return dict '''

    parser = argparse.ArgumentParser(description='Return a password based on a word list. \
                                     No arguments passed defaults to 4 word total with \
                                     capitalization allowed.')

    parser.add_argument('n', type=int, nargs='?', help='number of words to generate', default=4)
    parser.add_argument('-C', action="store_const", const=True, help='allow capitalized words')
    parser.add_argument('-s', action="store_const", const=True, \
                        help='append special character')
    parser.add_argument('-i', action="store_const", const=True, \
                        help='append digit')
    parser.add_argument('--max_length=', metavar='', type=int, default=50, \
                        help='maximum length of generated words')
    parser.add_argument('--min_length=', metavar='', type=int, default=1, \
                        help='minimum length of generated words')

    argument = parser.parse_args(sys.argv[1:])
    test = vars(argument)

    return test
