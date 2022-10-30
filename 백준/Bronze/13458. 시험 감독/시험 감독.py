from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    people: list = list(map(int, stdin.readline().rstrip().split()))
    b, c = map(int, stdin.readline().rstrip().split())

    answer: int = 0
    for i in range(len(people)):
        answer += 1
        people[i] -= b

        if people[i] <= 0:
            continue
        else:
            answer += people[i] // c
            if people[i] % c != 0:
                answer += 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()