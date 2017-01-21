import random
import wordcheck as wc

def pass_gen(length, caps, maximum, minimum):
    password = ''

    for _ in range(length):
        new_word = ''

        if caps:
            new_word = random.choice(open('words.txt').readlines()).rstrip()
            while not wc.word_length(new_word, maximum, minimum):
                new_word = random.choice(open('words.txt').readlines()).rstrip()
        else:
            new_word = random.choice(open('words.txt').readlines()).rstrip()
            while wc.caps_test(new_word) or not wc.word_length(new_word, maximum, minimum):
                new_word = random.choice(open('words.txt').readlines()).rstrip()

        password += new_word

    return password
