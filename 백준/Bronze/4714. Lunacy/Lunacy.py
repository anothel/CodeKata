from sys import stdin, stdout


def solution():
    while True:
        w = float(stdin.readline().rstrip())
        if w < 0:
            return

        stdout.write(
            "Objects weighing %.2f on Earth will weigh %.2f on the moon.\n" %
            (w, w * 0.167))


if __name__ == "__main__":
    solution()
