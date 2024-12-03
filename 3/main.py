import re

# part 1
data = None
with open("input_3.txt", "r") as file:
    data = file.read()

print(data)
ans = 0

pattern = r"mul\((\d+),(\d+)\)"
for match in re.finditer(pattern, data):
    num1, num2 = match.groups()
    num1, num2 = int(num1), int(num2)
    ans += num1 * num2

print(ans)

# part 2
ans = 0
enabled = True
last_dont_pos = -1
last_do_pos = -1

dont_matches = list(re.finditer(r"don't\(\)", data))
do_matches = list(re.finditer(r"do\(\)", data))
mul_matches = list(re.finditer(r"mul\((\d+),(\d+)\)", data))

for match in mul_matches:
    pos = match.start()

    latest_dont = max((m.start() for m in dont_matches if m.start() < pos), default=-1)
    latest_do = max((m.start() for m in do_matches if m.start() < pos), default=-1)

    enabled = (
        latest_do > latest_dont if (latest_dont != -1 or latest_do != -1) else True
    )

    if enabled:
        num1, num2 = match.groups()
        ans += int(num1) * int(num2)

print(ans)
