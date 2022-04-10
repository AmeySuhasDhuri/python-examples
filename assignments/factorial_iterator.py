# Find out the list of factorial of a number between 1 - 101 using custom iterator

class FactorialIter:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.factorial(self.n)
            self.n += 1
            return result
        else:
            raise StopIteration

    def factorial(self, num):
        result = 1
        for i in range(1, num+1):
            result = result * i
        return result

# create an object
numbers = FactorialIter(4)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))