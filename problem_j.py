line1 = input()
line2 = input()

things, scouts = line1.split(" ")
scouts = int(scouts)
things = int(things)
max_num_things = min(scouts * 2, things)

num_list = line2.split(" ")
num_list2 = []
for num in num_list:
    num_list2.append(int(num))

num_list2 = sorted(num_list2)[::-1]


scout_list = []
rest_list = []
i = 0
for thing in num_list2:
    if i < scouts:
        scout_list.append(thing)
    else:
        rest_list.append(thing)

    i += 1

scout_list = scout_list[::-1]

i2 = 0
for rest in rest_list:
    scout_list[i2] += rest

    i2 += 1

print(max(scout_list))
