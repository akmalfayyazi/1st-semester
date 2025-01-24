def palindrome(S):
    N = len(S)
    
    for i in range(N):
        if S[i] != S[N - i - 1]:
            return "Bukan King!"
    
    return "Palindrome King!"

S = input()

print(palindrome(S))
