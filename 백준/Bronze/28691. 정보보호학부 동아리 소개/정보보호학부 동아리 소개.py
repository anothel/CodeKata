from sys import stdin


def solution(s):
    if s == 'M':
        print('MatKor')
    elif s == 'W':
        print('WiCys')
    elif s == 'C':
        print('CyKor')
    elif s == 'A':
        print('AlKor')
    elif s == '$':
        print('$clear')


if __name__ == "__main__":
    s = (stdin.readline().strip())
    solution(s)
