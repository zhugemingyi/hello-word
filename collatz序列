def collatz(number):
    if number % 2 == 0:
        number //= 2
        return number
    if number % 2 == 1:
        number = 3 * number + 1
        return number
try:
    print("数：")
    num=int(input())
    sum=collatz(num)
    print(sum)
    while sum!=1:
        sum=collatz(sum)
        print(sum)
except ValueError:
    print('错误')
