import sys
import unicodedata


def print_unicode_table(word):
    print("decimal   hex   chr {0:^40}".format("name"))  # align by center for {0} - name
    print("-------  -----  --- {0:-<40}".format(""))  # align left

    code = ord(" ")  # return an integer representing the Unicode code point of character
    end = sys.maxunicode  # get max unicode code

    while code < end:
        c = chr(code)  # get the Unicode symbol (character) representation from integer
        name = unicodedata.name(c, "*** unknown ***")  # return name (string) Unicode code
        if word is None or word in name.lower():  #
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
        code+=1

word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):  # print usage information
        print("usage: {0} [string]".format(sys.argv[0]))
        word = 0
    else:
        word = sys.argv[1].lower()
if word != 0:
    print_unicode_table(word)