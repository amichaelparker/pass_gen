import random

def caps_test(word):
    if word[0] == word[0].upper():
        return True

    return False

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
