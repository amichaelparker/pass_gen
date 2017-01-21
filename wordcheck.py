def caps_test(word):
    if word[0] == word[0].upper():
        return True

    return False

def word_length(word, maximum, minimum):
    if minimum <= len(word) <= maximum:
        return True

    return False
