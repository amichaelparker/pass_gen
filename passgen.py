import random
import sys
import argparse

def caps_test(word):
    if word[0] == word[0].upper():
        return True

    return False

def parse_arguments():
    parser = argparse.ArgumentParser(description='Return a password.')
    parser.add_argument('n', type=int, nargs='?', help='number of words to generate', default=4)
    parser.add_argument('-C', action='store_const', const=True, help='allow capitalized words')

    argument = parser.parse_args(sys.argv[1:])
    test = vars(argument)
    print(test)

    return test

def pass_gen(length, caps):
    password = ''

    for _ in range(length):
        new_word = ''

        if caps:
            new_word = random.choice(open('words.txt').readlines()).rstrip()
        else:
            new_word = random.choice(open('words.txt').readlines()).rstrip()
            while caps_test(new_word):
                new_word = random.choice(open('words.txt').readlines()).rstrip()

        password += new_word

    return password

def main():
    arguments = parse_arguments()
    print(pass_gen(arguments['n'], arguments['C']))


if __name__ == "__main__":
    main()
