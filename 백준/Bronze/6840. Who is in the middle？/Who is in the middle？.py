from sys import stdin


def solution():
    people: list = []
    for _ in range(3):
        people.append(int(stdin.readline().rstrip()))
    people.sort()

    print(people[1])


if __name__ == "__main__":
    solution()
