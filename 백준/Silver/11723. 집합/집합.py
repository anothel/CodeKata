from sys import stdin, stdout


def func_toggle(zip: set, x: int):
    if x in zip:
        zip.discard(x)
    else:
        zip.add(x)


def func_all(zip: set):
    zip.clear()
    for i in range(1, 21):
        zip.add(i)


def solution():
    zipList: set = set()
    for _ in range(int(stdin.readline().rstrip())):
        table = list(map(str, stdin.readline().rstrip().split()))
        if table[0] == "add":
            zipList.add(int(table[1]))
        elif table[0] == "remove":
            zipList.discard(int(table[1]))
        elif table[0] == "check":
            stdout.write("1\n" if int(table[1]) in zipList else "0\n")
        elif table[0] == "toggle":
            func_toggle(zipList, int(table[1]))
        elif table[0] == "all":
            func_all(zipList)
        elif table[0] == "empty":
            zipList.clear()


if __name__ == "__main__":
    solution()
