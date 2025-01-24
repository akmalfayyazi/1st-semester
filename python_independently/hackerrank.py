def string_number():
    n = int(input())
    for i in range(1, n + 1):
        a = str(i)
        print(a, end="")

def list_comprehensif():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    return [[i,j,k] for i in list(range(0,x+1)) for j in list(range(0, y + 1)) for k in list(range(0,z+1)) if i + j + k != n]

def runner_up():
    n = int(input())
    m = list(map(int, input().split()))
    m = sorted(set(m))
    return m[-2]

def nested_list():
    nest = []
    s = set()
    for _ in range(int(input("input how many student: "))):
        name = input("input the name: ")
        grade = float(input("input their grades: "))
        nest.append([name, grade])
        s.add(grade)

    low_grade = sorted(s)[1]
    low_student = []

    for i,j in nest:
        if j == low_grade:
            low_student.append(i)

    for i in sorted(low_student):
        print(i)

def precentege():
    key_value = {}
    for _ in range(int(input())):
        name, *line = input().split()
        grades = list(map(float, line))
        key_value[name] = grades
    the_selected = input()
    result = 0
    for i in key_value:
        if i == the_selected:
            result = sum(key_value[the_selected])/len(key_value[the_selected])
    
    print(f"{result:.2f}")

def numpy_array():
    import numpy
    column, row = map(int, input("input the column and the row: ").split())
    the_list = []
    for i in range(column):
        num = list(map(int, input("input the number: ").split()))
        the_list.append(num)
            
    max_vertikal = numpy.min(the_list, axis=1)
    max_vertikal = numpy.max(max_vertikal)

def tupple():
    n = int(input())
    tupel = tuple(map(int, input().split()))
    print(tupel)

def listt():
    arr = []
    for i in range(int(input("input how many command do you want: "))):
        command = list(map(str, input().split()))
        if command[0] == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            arr.remove(int(command[1]))
        elif command[0] == "append":
            arr.append(int(command[1]))
        elif command[0] == "print":
            print(arr)
        elif command[0] == "sort":
            arr = sorted(arr)
        elif command[0] == "pop":
            arr.pop()
        elif command[0] == "reverse":
            arr.reverse()

def swap_case():
    string = input("input the string: ")
    result = ""
    for i in string:
        if i.islower():
            i = i.upper()
            result += i
        elif i.isupper():
            i = i.lower()
            result += i
        else:
            result += i

    print(result)

def delimeter():
    word = input()
    result = word.split()
    result = "-".join(result)
    return result

def full_name(first, second):
    full = first + " " + second
    return f"Hello {full}! You just delved into python."

def abracadabra(string, position, letter):
    string = list(string)
    string.pop(position)
    string.insert(position, letter)
    result = "".join(string)
    return result
    
def count_substring(string, substring):
    result = 0
    for i in range(len(string)):
        if substring == string[i:i + len(substring)]:
            result += 1
    return result

def is_alpabet():
    s = input()
    if any(i.isalnum() for i in s):
        print("True")
    else:
        print("False")
    if any(i.isalpha() for i in s):
        print("True")
    else:
        print("False")
    if any(i.isdigit() for i in s):
        print("True")
    else:
        print("False")
    if any(i.islower() for i in s):
        print("True")
    else:
        print("False")
    if any(i.isupper() for i in s):
        print("True")
    else:
        print("False")
    
def make_hackerrank():
    n = int(input())
    # ---------top------------
    times = 1
    space = (n * 2) - 1
    for i in range(n):
        print(("H" * times).center(space))
        times += 2

    # ---------top-----------
    space1 = " " * int((n - 1) / 2)
    for i in range(n+1):
        space2 = " " * n * 3
        thickness = "H" * n
        print(space1 + thickness + space2 + thickness)

    # ---------middle------------
    for i in range(int((n+1)/2)):
        middle = "H"*n*5
        print(space1 + middle)

    # --------------bottom---------
    space1 = " " * int((n - 1) / 2)
    for i in range(n+1):
        space2 = " " * n * 3
        thickness = "H" * n
        print(space1 + thickness + space2 + thickness)

    # ----------bottom narrow-------
    times2 = (n * 2) - 1
    the_space = n * 4
    for i in range(n):
        last_space = " " * the_space
        print(last_space + "H" * times2)
        the_space += 1
        times2 -= 2

def text_wrap():
    sentence = input()
    max_width = int(input())
    import textwrap
    result = textwrap.fill(sentence, max_width)
    return result

def mat():
    n, m = map(int, input().split())
    # first
    a = int((n-1) / 2)
    kali = 1
    for i in range(a):
        sentence = ".|." * kali
        result = sentence.center(m, "-")
        kali += 2
        print(result)

    # the welcome
    print("WELCOME".center(m, "-"))

    # last
    kali2 = n - 2
    for i in range(a):
        sentence = ".|." * kali2
        result = sentence.center(m, "-")
        kali2 -= 2
        print(result)

def bilangan():
    n = int(input())
    result = len(bin(n)) - 2
    for i in range(1, n + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal.rjust(result)} {octal.rjust(result)} {hexadecimal.rjust(result)} {binary.rjust(result)}")

def rangoli():
    n = int(input())
    for i in range(n):
        s = "-".join(chr(ord("a") + n - j - 1)for j in range(i + 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, "-"))

    for i in range(n - 2, -1, -1):
        s = "-".join(chr(ord("a") + n - j - 1) for j in range(i + 1))
        print((s + s[::-1][1:]).center(n*4-3, "-"))

def capitalize():
    s = input()
    word = s.split(" ")
    resultt = []
    for i in word:
        result = i.capitalize()
        resultt.append(result)

    print( " ".join(resultt))

def banana():
    s = "BANANA"
    vowel = 0
    consonant = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            a = s[i:j + 1]
            if a[0] in "AIUEO":
                vowel += 1
            else:
                consonant += 1
    if vowel > consonant:
        print("Kevin", vowel)
    elif vowel < consonant:
        print("Stuart", consonant)
    else:
        print("Draw")

def average():
    s = list(map(int, input().split()))
    s = set(s)
    s = sum(s) / len(s)
    print(s)

def set():
    m = int(input())
    set1 = set(list(map(int, input().split())))
    n = int(input())
    set2 = set(list(map(int, input().split())))
    a = sorted(set1.symmetric_difference(set2))
    for i in a:
        print(i)

def set1():
    a = set()
    for i in range(int(input())):
        country = input()
        a.add(country)
    print(len(a))

def set3():
    a = int(input())
    b = set(list(map(int, input().split())))
    for _ in range(int(input())):
        command = list(map(str, input().split()))
        if command[0] == "pop":
            b.pop()
        if command[0] == "remove":
            b.remove(int(command[1]))
        if command[0] == "discard":
            b.discard(int(command[1]))
    print(sum(b))














    




            