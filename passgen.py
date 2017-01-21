import parse
import gen

def main():
    arguments = parse.parse_arguments()
    print(gen.pass_gen(arguments['n'], arguments['C']))


if __name__ == "__main__":
    main()
