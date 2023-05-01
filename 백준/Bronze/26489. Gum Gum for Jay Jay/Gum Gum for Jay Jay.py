from sys import stdin


def solution():
    count = 0
    while True:
        sentence = stdin.readline().strip()
        if sentence != 'gum gum for jay jay':
            break
        count += 1

    print(count)


if __name__ == "__main__":
    solution()
