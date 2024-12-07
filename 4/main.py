# part 1
data = None
with open("input_4.txt", "r") as file:
    data = file.read().split("\n")

ans = 0
for j in range(len(data[0])):
    for i in range(len(data) - 3):
        word = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j]
        word_back = data[i + 3][j] + data[i + 2][j] + data[i + 1][j] + data[i][j]
        if word == "XMAS":
            ans += 1
        if word_back == "XMAS":
            ans += 1

for i in range(len(data)):
    for j in range(len(data[0]) - 3):
        word = data[i][j : j + 4]
        word_back = data[i][j + 3] + data[i][j + 2] + data[i][j + 1] + data[i][j]
        if word == "XMAS":
            ans += 1
        if word_back == "XMAS":
            ans += 1

for i in range(len(data) - 3):
    for j in range(len(data[0]) - 3):
        word = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3]
        word_back = (
            data[i + 3][j + 3] + data[i + 2][j + 2] + data[i + 1][j + 1] + data[i][j]
        )
        if word == "XMAS":
            ans += 1
        if word_back == "XMAS":
            ans += 1

for i in range(len(data) - 3):
    for j in range(3, len(data[0])):
        word = data[i][j] + data[i + 1][j - 1] + data[i + 2][j - 2] + data[i + 3][j - 3]
        word_back = (
            data[i + 3][j - 3] + data[i + 2][j - 2] + data[i + 1][j - 1] + data[i][j]
        )
        if word == "XMAS":
            ans += 1
        if word_back == "XMAS":
            ans += 1

print(ans)

ans = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) - 1):
        center = data[i][j]
        if center != "A":
            continue

        diag1 = data[i - 1][j - 1] + center + data[i + 1][j + 1]
        diag2 = data[i - 1][j + 1] + center + data[i + 1][j - 1]
        diag1_rev = data[i + 1][j + 1] + center + data[i - 1][j - 1]
        diag2_rev = data[i + 1][j - 1] + center + data[i - 1][j + 1]

        if (
            (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM")
        ) or (
            (diag1_rev == "MAS" or diag1_rev == "SAM")
            and (diag2_rev == "MAS" or diag2_rev == "SAM")
        ):
            ans += 1

print(ans)
