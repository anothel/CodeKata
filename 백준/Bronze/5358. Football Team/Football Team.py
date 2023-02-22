from sys import stdin, stdout


def solution():
    while True:
        s: str = str(stdin.readline().rstrip())
        if s == '':
            break
    
        for i in s:
            if i == 'i':
                stdout.write("e")
            elif i == 'e':
                stdout.write("i")
            elif i == 'I':
                stdout.write("E")
            elif i == 'E':
                stdout.write("I")
            else:
                stdout.write("%s" % i)
        stdout.write("\n")


if __name__ == "__main__":
    solution()
