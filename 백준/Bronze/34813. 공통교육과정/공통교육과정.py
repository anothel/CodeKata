from sys import stdin


def solution(s):
    if s[0] == 'F':
        print("Foundation")
    elif s[0] == 'C':
        print("Claves")
    elif s[0] == 'V':
        print("Veritas")
    elif s[0] == 'E':
        print("Exploration")


if __name__ == "__main__":
    s = (stdin.readline().strip())
    solution(s)
