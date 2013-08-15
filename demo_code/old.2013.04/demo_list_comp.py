

def for_loop():
    x = []
    for i in range(100000):
        x.append('chr' + str(i))
    return x


def list_comp():
    return ['chr' + str(i) for i in range(100000)]


def list_comp_formatter():
    return ['chr{:d}'.format(i) for i in range(100000)]

if __name__ == '__main__':
    from timeit import timeit
    print('Python for loop:',
          timeit("for_loop()",
                 setup="from __main__ import for_loop",
                 number=100))
    print('List Comprehension:',
          timeit("list_comp()",
                 setup="from __main__ import list_comp",
                 number=100))
    print('List Comp. with string formatter:',
          timeit("list_comp_formatter()",
                 setup="from __main__ import list_comp_formatter",
                 number=100))
