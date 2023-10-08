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

    for i in range(len(s)):
        if last_digit < rome[s[i]] and i == len(s)-1:
            out += rome[s[i]] - current

        elif i == len(s) - 1:
            out += current + rome[s[i]]

        elif last_digit == rome[s[i]]:
            current += rome[s[i]]

        elif last_digit < rome[s[i]]:
            current = rome[s[i]] - current
        else:
            out += current
            current = rome[s[i]]
        last_digit = rome[s[i]]

    print(out)