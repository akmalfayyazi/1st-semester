n, m = map(int, input().split())
for i in range(n):
    for j in range(n):
        if (i < m or i >= n - m or j < m or j >= n - m):
            print("*", end="")
        else:
            print(" ", end="")
    print()
