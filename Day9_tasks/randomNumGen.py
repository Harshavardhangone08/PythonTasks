'''
Random Number Generator (Generators)
A program is needed to generate numbers for testing purposes. Create a generator
function that produces numbers from 1 to N and prints them one by one when iterated.
'''
def num_generator(n):
    yield from range(1, n + 1)

n = int(input("Enter a number: "))

for num in num_generator(n):
    print(num)