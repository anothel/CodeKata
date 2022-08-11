from sys import stdin, stdout


def canPlay(k: int, a: int) -> bool:
    return True if a < k else False


def howMany(time: int, hm: int) -> int:
    return time * hm


if __name__ == "__main__":
    k: int = int(stdin.readline().rstrip())
    a, x = map(int, stdin.readline().rstrip().split())
    b, y = map(int, stdin.readline().rstrip().split())

    if canPlay(k, a + b) or canPlay(k, a) or canPlay(k, b):
        stdout.write("%d\n" % max(
            howMany(k - a, x) + howMany(k - (a + b), y),
            howMany(k - b, y) + howMany(k - (a + b), x), howMany(k - a, x),
            howMany(k - b, y)))
    else:
        stdout.write("0\n")
