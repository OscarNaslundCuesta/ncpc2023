s1 = input()
s2 = input()
s3 = input()

pre_d1 = s1.split(" ")
d1 = []
for num in pre_d1:
    d1.append(int(num))

pre_d2 = s2.split(" ")
d2 = []
for num in pre_d2:
    d2.append(int(num))

pre_d3 = s3.split(" ")
d3 = []
for num in pre_d3:
    d3.append(int(num))

w1v2 = 0
w1v3 = 0
w2v1 = 0
w2v3 = 0
w3v1 = 0
w3v2 = 0

i = 0
for num in d1:
    j = 0
    for num2 in d2:
        if d1[i] > d2[j]:
            w1v2 += 1
        elif d1[i] < d2[j]:
            w2v1 += 1
        j += 1
    i += 1

i = 0
for num in d1:
    j = 0
    for num2 in d2:
        if d1[i] > d3[j]:
            w1v3 += 1
        elif d1[i] < d3[j]:
            w3v1 += 1
        j += 1
    i += 1

i = 0
for num in d2:
    j = 0
    for num2 in d2:
        if d2[i] > d3[j]:
            w2v3 += 1
        elif d2[i] < d3[j]:
            w3v2 += 1
        j += 1
    i += 1


if w1v2 >= w2v1 and w1v3 >= w3v1 and w1v2 != 0 and w1v3 != 0:
    print(1)
elif w2v1 >= w1v2 and w2v3 >= w3v2 and w2v1 != 0 and w2v3 != 0:
    print(2)
elif w3v1 >= w1v3 and w3v2 >= w2v3 and w3v1 != 0 and w3v2 != 0:
    print(3)
else:
    print("No dice")
