def longest_word():
    words = ["artificial", "intelligence", "is", "awesome"]
    longest_word = max(words, key=len)
    return f"longest word : {longest_word} \nlength: {len(longest_word)}"

def temprature():
    celcius = int(input("input how much celcius: "))
    fahrenheit = celcius * 1.8 + 32
    return f"{celcius} celcius in fahrenhait is {int(fahrenheit)}"

def sum_average():
    number = list(map(int, input("fill the numbers: ").split()))
    summ = sum(number)
    average = summ / len(number)
    print(f"sum of the numbers is: {summ} \nand the average is: {int(average)}")

def count_frequency():
    count = {}
    text = "hello world hello"
    text = text.lower().split()
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

def even_number():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            pass
    return even

def remove_duplicate():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    numbers = set(numbers)
    numbers = list(numbers)
    return numbers

def matrix_transpose():
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    transpoosed = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpoosed.append(row)
    return transpoosed

def is_palindrome():
    text = "A man, a plan, a canal, Panama"
    text = text.lower().replace(" ", "").replace(",", "")
    if text == text[::-1]:
        return True
    else:
        return False

def largest_number():
    number = list(map(int, input().split()))
    largest = max(number)
    return largest

def character_string():
    string = input()
    character = input()
    many = string.count(character)
    return many

def reverse_string():
    string = input()
    reveres = string[::-1]
    return reveres

def two_list():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    the_list = [i for i in first if i in second]
    return the_list

def sum_digits():
    digit = int(input())
    digit = " ".join(str(digit))
    digit = digit.split()
    digit = list(map(int, digit))
    result = sum(digit)
    return result

def is_substring():
    first = input()
    second = input()
    if second in first:
        return "yes"
    else:
        return "no"
        
def if_anagrams():
    first = input()
    second = input()
    first = " ".join(first)
    second = " ".join(second)
    for i in first:
        if i in second:
            return "yes"
        else:
            return "no"

def division_anumber():
    number = int(input())
    divisor = []
    for i in range(1, number+1):
        if number % i == 0:
            divisor.append(i)
    return divisor

def count_word():
    sentence = input()
    sentence = list(map(str, (sentence).split()))
    count = 0
    for i in sentence:
        count += 1
    
    return count
    
def second_largest():
    number = list(map(int, input().split()))
    second = sorted(number)[-3]
    return second

def sum_even():
    number = list(map(int, input().split()))
    even = []
    for i in number:
        if i % 2 == 0:
            even.append(i)
    result = sum(even)
    return result

def remove():
    number = list(map(int, input().split()))
    removing = int(input())
    result = []
    for i in number:
        if i != removing:
            result.append(i)
    return result

def count():
    number = list(map(int, input().split()))
    counting = int(input())
    counter = 0
    for i in number:
        if i == counting:
            counter += 1
    return counter

def max_minn():
    number = list(map(int, input().split()))
    maxx = max(number)
    minn = min(number)    
    return f"max: {maxx} \nmin: {minn}"

def max_min():
    number = list(map(int, input().split()))
    number = sorted(number)
    minn, maxx = number[0], number[-1]
    return f"max: {maxx} \nmin: {minn}"

def reverse_list():
    number = list(map(int, input().split()))
    number = number[::-1]
    return number

def merge_2_list():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    result = first + second
    return result

print(if_anagrams())