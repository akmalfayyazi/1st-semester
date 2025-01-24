input = int(input()) # input 2 atau 3
print('+'+'-'*(2*input+1)+'+')
for i in range(input):
        s = '| '
        for j in range(input):
            if j % 2 == 0:
                s += 'V ' if i % 2 == 0 else '. '
            else:
                s += '. ' if i % 2 == 0 else 'V '
        s += '| '
        print(s)
print('+'+'-'*(2*input+1)+'+')