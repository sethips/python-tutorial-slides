birth_list = [       # a list of birth
    [1991, 1, 1],
    [1980, 2, 6],
    [2004, 5, 3]
]

x = 0
# an infinite loop
while True:
    if x % 2 == 0:
        print('x is even when x =', x)
    if x > 10:
        break
    x += 1
print(x)
