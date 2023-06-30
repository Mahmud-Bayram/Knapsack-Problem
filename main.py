file = open("ks_200_0", "r")
features = file.readline().split(" ")
lines = [[0 for i in range(2)] for j in range(int(features[0]))]

lines = file.read().split('\n')
lines = [line.split(' ') for line in lines]


def weighted_knapsack(W, lines):
    n = int(features[0])
    M = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(0, n+1):
        for w in range(0, W+1):
            if int(lines[i-1][1]) > w:
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = max(M[i-1][w], int(lines[i-1][0]) + M[i-1][w-int(lines[i-1][1])])

    print(M[n][W])


    def find_solution(M, lines, n, W):
        items = []
        i = n
        j = W

        while i > 0 and j > 0:
            if M[i][j] != M[i - 1][j]:
                items.append(i)
                j -= int(lines[i - 1][1])
            i -= 1

        items.reverse()
        return items

    solution = find_solution(M, lines, n, W)

    for i in range(1, n+1, 1):
        if i in solution:
            print(1, end=' ')
        else:
            print(0, end=' ')




W = int(features[1])
weighted_knapsack(W, lines)

