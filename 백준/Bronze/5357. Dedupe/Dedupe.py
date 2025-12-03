from sys import stdin


def solution(s):
    result = []
    prev = ''
    for char in s:
        if char != prev:
            result.append(char)
        prev = char
    print(''.join(result))


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    for _ in range(N):
        s = (stdin.readline().strip())
        solution(s)
