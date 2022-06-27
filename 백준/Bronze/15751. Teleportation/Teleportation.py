from sys import stdin, stdout


def main():
    a, b, x, y = map(int, stdin.readline().rstrip().split())

    stdout.write(
        "%d\n" %
        (min([abs(b - a),
              abs(x - a) + abs(b - y),
              abs(a - y) + abs(b - x)])))


if __name__ == "__main__":
    main()