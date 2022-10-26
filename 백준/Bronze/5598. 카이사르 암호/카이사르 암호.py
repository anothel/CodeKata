from sys import stdin, stdout


def solution():
    answer: str = ''
    for i in stdin.readline().rstrip():
        if i == 'A' or i == 'B' or i == 'C':
            answer += chr(ord(i) + 23)
        else:
            answer += chr(ord(i) - 3)
    stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solution()