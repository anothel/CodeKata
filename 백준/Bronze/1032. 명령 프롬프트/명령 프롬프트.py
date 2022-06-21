from sys import stdin, stdout


def main():
    files: list = list()
    for _ in range(int(stdin.readline().rstrip())):
        files.append(stdin.readline().rstrip())

    for j in range(len(files[0])):
        for i in range(len(files)):
            if files[0][j] == files[i][j]:
                if i == len(files) - 1:
                    stdout.write("%s" % files[0][j])
                    break
                else:
                    continue
            else:
                stdout.write("?")
                break


if __name__ == "__main__":
    main()
