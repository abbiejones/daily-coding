# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

alphabet = {1: 'a', 2: 'b', 3: 'c' , 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16: 'p', 17: 'q', 18:  'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

decoded_words = set()

def one_letter(code, index, word):
    if index < len(code):
        if int(code[index]) in alphabet.keys():
            word = word + alphabet[int(code[index])]
            one_letter(code, index + 1, word)
            two_letter(code, index + 1, word)
    if (index == len(code)):
        decoded_words.add(word)


def two_letter(code, index, word):
    if index + 1 < len(code):
        if int(code[index: index + 2]) in alphabet.keys():
            word = word + alphabet[int(code[index: index + 2])]
            one_letter(code, index + 2, word)
            two_letter(code, index + 2, word)
    if (index == len(code)):
        decoded_words.add(word)


def branch(code):
    if len(code) >= 1:
        one_letter(code, 0, word = "")
    if len(code) >= 2:
        two_letter(code, 0, word = "")


def main():
    branch("4321")
    print(decoded_words)


main()