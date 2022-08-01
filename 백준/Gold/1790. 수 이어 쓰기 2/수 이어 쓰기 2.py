from sys import stdin, stdout


def solution():
    n, k = map(int, stdin.readline().rstrip().split())

    answer: int = 0
    digit: int = 1
    nine: int = 9

    while k > digit * nine:
        k -= digit * nine
        answer += nine
        digit += 1
        nine *= 10
    answer = (answer + 1) + ((k - 1) // digit)

    if answer > n:
        stdout.write("-1\n")
    else:
        stdout.write("%s\n" % str(answer)[(k - 1) % digit])


if __name__ == "__main__":
    solution()
