result = 0

def merge(arr, l, m, r, result):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l+i]
    
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l 

    while(i < n1 and j < n2):
        if(L[i] < R[j]):
            arr[k] = L[i]
            i+=1
            result[0]+=1
        else:
            arr[k] = R[j]
            j+=1
            result[1]+=1
        k+=1
    
    result[2]+=1
            
    while(i<n1):
        arr[k] = L[i]
        k+=1
        i+=1
        result[0]+=1
    
    while(j < n2):
        arr[k] = R[j]
        k+=1
        j+=1
        result[1]+=1

        

def merge_sort(arr, l, r, result):
    if (l < r):
        m = (l+r) // 2

        merge_sort(arr, l, m, result)
        merge_sort(arr, m+1, r, result)
        merge(arr, l, m, r,result)

n = int(input())
arr = list(map(int, input().split()))

result = [0] * 3

merge_sort(arr, 0, len(arr) - 1, result )

for i in result:
    print(i)