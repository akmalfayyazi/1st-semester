m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.extend(map(int, input().split()))

q = int(input())
age = list(map(int, input().split()))

arr.sort()

def count_less_than_x(arr, age):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < age:
            left = mid + 1
        else:
            right = mid
    return left

total = []
for a in age:
    total.append(count_less_than_x(arr, a))

print(*total)