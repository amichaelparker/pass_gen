''' Generate passwords based on https://xkcd.com/936/ '''

from lib import parse
from lib import gen

def main():
    ''' Main function '''

    arguments = parse.parse_arguments()
    print(gen.pass_gen(arguments['n'], arguments['C'], arguments['max_length='], \
          arguments['min_length='], arguments['s'], arguments['i']))


if __name__ == "__main__":
    main()
