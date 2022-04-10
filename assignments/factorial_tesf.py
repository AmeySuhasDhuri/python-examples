#Write a function to calculate factorial of a function.
#iterate over range of values

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result

for i in range(1, 101):
    print(i, " - ", factorial(i))


