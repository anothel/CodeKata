from sys import stdin


def solution():
    ISBN = str(stdin.readline().strip())

    star = ISBN.index('*')

    total = 0
    for i in range(12):
        if i == star:
            continue
        weight = 1 if i % 2 == 0 else 3
        total += int(ISBN[i]) * weight

    m = int(ISBN[12])
    weight = 1 if star % 2 == 0 else 3
    for x in range(10):
        if (total + x * weight + m) % 10 == 0:
            print(x)
            return


if __name__ == "__main__":
    solution()
