def toJadenCase(string):
    s = list(string)
    s[0] = s[0].upper()
    spaces = [i for i in range(len(s)) if s[i] == " "]
    first_letters = list(map(lambda x: x + 1, spaces))
    if len(s) in first_letters:
        first_letters.remove(len(s))
    new_list = [s[i].upper() if i in first_letters else s[i] for i in range(len(s))]

    str = ''.join(new_list)
    return str


def main():
    print(toJadenCase("How can mirrors be real if our eyes aren't real"))

main()