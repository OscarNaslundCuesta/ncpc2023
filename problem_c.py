rome = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

strings = []

n = int(input())
for i in range(n):
    strings.append(input())

for s in strings:
    out = 0
    current = 0
    last_digit = 0
    s = s[::-1]
    rm = False
    biggest = 0
    for i in range(len(s)):
        if biggest < rome[s[i]]:
            out += rome[s[i]]
            rm = False
            biggest = rome[s[i]]
        elif biggest > rome[s[i]]:
            out -= rome[s[i]]
            rm = True
        else:
            if rm:
                out -= rome[s[i]]
            else:
                out += rome[s[i]]
        last_digit = rome[s[i]]

    print(out)
    