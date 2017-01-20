import random

def main():
    password = ''
    for word in range(4):
        password += random.choice(open('words.txt').readlines()).rstrip()

    print(password)

if __name__ == "__main__":
    main()
