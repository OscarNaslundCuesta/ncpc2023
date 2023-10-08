import sys

known_int = 2
known_0 = None
sys.setrecursionlimit(100000)


def read_buf(num):
    global known_int
    global known_0

    guess = num - 1
    str = f"buf[{guess}]"
    print(str)
    read = input()

    if read == "Segmentation fault (core dumped)" or read == "Too many reads":
        exit()
    else:
        read_int = int(read)

    if read_int > 0:
        known_int = num
        if known_0:
            if known_0 - known_int == 1:
                print(f"strlen(buf) = {known_int}")
                exit()
            read_buf(int(known_int + (known_0 - known_int) / 2))
        else:
            read_buf(num * 2)
    else:
        known_0 = num
        if known_0 - known_int == 1:
            print(f"strlen(buf) = {known_int}")
            exit()
        read_buf(int(known_0 - (known_0 - known_int) / 2))


read_buf(4)

