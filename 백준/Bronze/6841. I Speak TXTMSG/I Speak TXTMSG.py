from sys import stdin, stdout


def solution():
    while True:
        s: str = stdin.readline().rstrip()
        if s == 'CU': stdout.write("see you\n")
        elif s == ':-)': stdout.write("I’m happy\n")
        elif s == ':-(': stdout.write("I’m unhappy\n")
        elif s == ';-)': stdout.write("wink\n")
        elif s == ':-P': stdout.write("stick out my tongue\n")
        elif s == '(~.~)': stdout.write("sleepy\n")
        elif s == 'TA': stdout.write("totally awesome\n")
        elif s == 'CCC': stdout.write("Canadian Computing Competition\n")
        elif s == 'CUZ': stdout.write("because\n")
        elif s == 'TY': stdout.write("thank-you\n")
        elif s == 'YW': stdout.write("you’re welcome\n")
        elif s == 'TTYL':
            stdout.write("talk to you later\n")
            break
        else:
            stdout.write("%s\n" % s)


if __name__ == "__main__":
    solution()
