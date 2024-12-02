from collections import Counter

# part 1

data = 0
with open("input_2.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

ans = 0
for line in data:
    nums = line.split(" ")
    inc = int(nums[1]) - int(nums[0]) > 0
    good = True
    for index, num in enumerate(nums[1:]):
        if inc:
            if int(num) - int(nums[index]) > 0 and int(num) - int(nums[index]) < 4:
                continue
            else:
                good = False
        else:
            if int(num) - int(nums[index]) < 0 and int(num) - int(nums[index]) > -4:
                continue
            else:
                good = False

    if good:
        ans += 1

print(ans)

# part 2


with open("input_2.txt", "r") as file:
    data = file.read()
    data = data.split("\n")


def check(nums):
    inc = int(nums[1]) - int(nums[0]) > 0
    good = True
    for index, num in enumerate(nums[1:]):
        if inc:
            if int(num) - int(nums[index]) > 0 and int(num) - int(nums[index]) < 4:
                continue
            else:
                good = False
        else:
            if int(num) - int(nums[index]) < 0 and int(num) - int(nums[index]) > -4:
                continue
            else:
                good = False

    return good


ans = 0
for line in data:
    nums = line.split(" ")

    for i in range(0, len(nums)):
        if check(nums[:i] + nums[i + 1 :]):
            ans += 1
            break


print(ans)
