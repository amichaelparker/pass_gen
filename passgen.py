import random
import sys
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Return a password.')
    parser.add_argument('n', type=int, help='Number of words to generate')
    parser.parse_args(sys.argv[1:])

def pass_gen(length):
    password = ''
    for word in range(length):
        password += random.choice(open('words.txt').readlines()).rstrip()

    return password

def main():
    parse_arguments()
    print(pass_gen(int(sys.argv[1])))

if __name__ == "__main__":
    main()
