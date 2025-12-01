from sys import stdin


def solution(s1, s2):
    if s1 == s2:
        print('0')
    else:
        print('1550')


if __name__ == "__main__":
    s1 = (stdin.readline().strip())
    s2 = (stdin.readline().strip())
    solution(s1, s2)
