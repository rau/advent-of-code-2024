from collections import Counter

# part 1

with open("input_1.txt", "r") as file:
    data = file.read()
    data = data.split("   ")
    list1, list2 = [data[0]], [data[-1]]
    for i in range(1, len(data) - 1):
        item1, item2 = data[i].split("\n")
        list1.append(item2)
        list2.append(item1)

list1 = sorted(list1)
list2 = sorted(list2)

sum_ = 0
for pair in zip(list1, list2):
    sum_ += abs(int(pair[1]) - int(pair[0]))

print(sum_)

# part 2
with open("input_1.txt", "r") as file:
    data = file.read()
    data = data.split("   ")
    list1, list2 = [data[0]], [data[-1]]
    for i in range(1, len(data) - 1):
        item1, item2 = data[i].split("\n")
        list1.append(item2)
        list2.append(item1)

sum_ = 0
count = Counter(list2)
for num in list1:
    sum_ += int(num) * int(count[num])

print(sum_)
