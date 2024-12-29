import random

a = random.randrange(1, 100, 1)
print(a)

b = random.random()
print(b)    #dowolona liczba całkowita

c = random.choice("abcdefghij")
print(c)    #dowolny element z nawiasu

d = random.uniform(1, 100)
print(d)    #dowolna liczba rzeczywista z zakresu

print("Press Enter to close the program...")
input()