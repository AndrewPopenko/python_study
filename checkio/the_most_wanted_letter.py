import string


# first attempt
def checkio_my(text):
    text = text.lower()

    max_cnt = 0
    letter = ''

    for char in text:
        tmp = text.count(char)
        if tmp >= max_cnt and char.isalpha():
            max_cnt = tmp
            letter = char

    return letter


def checkio(text):
    letters = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            try:
                letters[char] += 1
            except KeyError:
                letters[char] = 1

    letters = list(letters.items())

    letters.sort(key=lambda k: (-k[1], k[0]))

    return


def checkio_another_solution(text):
    text = text.lower()

    return max(string.ascii_lowercase, key=text.count)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
