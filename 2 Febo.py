'''str = input("Enter UR Name:")
print(str)
str = input("Press any key")'''

def fibo(n):
    a=0
    b=1
    for x in range(n,0,-1):
        a=b
        b=a+b
        print(a)
    return b

num = int(input('Enter n value : '))

print(fibo(num))

input('Enter any key to exit:')