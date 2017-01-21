from lib import parse
from lib import gen

def main():
    arguments = parse.parse_arguments()
    print(gen.pass_gen(arguments['n'], arguments['C'], arguments['max_length='], \
          arguments['min_length=']))


if __name__ == "__main__":
    main()
