file = open("knapsack_dosyalar\\ks_10000_0", "r")
features = file.readline().split(" ")
lines = [[0 for i in range(2)] for j in range(int(features[0]))]

lines = file.read().split('\n')
lines = [line.split(' ') for line in lines]


def weighted_knapsack(lines):
    i = 0
    j = 0
    M = list(range(int(features[0])))
    for i in range(int(features[0])):
        if int(lines[i][1]) < 1000000:
            oran = int(lines[i][1]) / int(lines[i][0])
            M[i] = oran

    for index in range(len(M)):
        min_index = index

        for j in range(index + 1, len(M)):
            if M[j] < M[min_index]:
                min_index = j
                term = M[min_index]
                M[min_index] = M[index]
                M[index] = term

                term = lines[min_index]
                lines[min_index] = lines[index]
                lines[index] = term

    topWeight = 0
    topValue = 0
    values = []
    for j in range(int(features[0])-1, 0, -1):
        topWeight += int(lines[j][1])
        topValue += int(lines[j][0])
        values.append(int(lines[j][0]))
        if topWeight > 1000000:
            topWeight -= int(lines[j][1])
            topValue -= int(lines[j][0])
            values.pop()
            break

    print(topValue)
    return values


values = weighted_knapsack(lines)


file2 = open("knapsack_dosyalar\\ks_10000_0", "r")

lineNo = []
items = [[0 for _ in range(2)] for _ in range(int(features[0]))]
items = file2.read().split('\n')
items.pop(0)
items = [item.split(' ') for item in items]

for i in range(0, int(features[0]), 1):
    if int(items[i][0]) in values:
        lineNo.append(i)

for i in range(1, int(features[0])+1, 1):
    if i in lineNo:
        print(1, end=' ')
    else:
        print(0, end=' ')



