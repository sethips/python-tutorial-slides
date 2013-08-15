# demo_for.py


def test_for():
    # loop in list, (set, string are the same)
    l = [1, 2, 4]
    for i in l:
        print(str(i))

    # loop using range()
    for x in range(10):
        print('this is', x, 'th time.')

    print(list(range(5)))   # make range into list

    # loop with an index
    str_l = ['abc', 'def', 'ghi', 'jkl']
    for i, s in enumerate(str_l):
        print(i, 'th item is', s)
        if i == 1:
            for c in s:
                print(c)

    # loop in dict
    my_profile = {'name': 'liang',
                  'address': 'moon',
                  'birth': '1991'}

    for k, v in my_profile.items():
        print('key', k, 'contains', v)

    # loop only key in dict
    for k in my_profile.keys():
        print(k)

    # looping at more than two iterables
    list1 = ['a', 'b', 'c']
    list2 = [1, 4, 6, 7, 8]
    list3 = [1, 4.5, 3.5, 3]
    for i, j, k in zip(list1, list2, list3):
        #print('i', i, ',j', j, 'k', k)
        print('i: {:>4s}, j: {:4d}, k: {:4.1f}'.format(i, j, k))

if __name__ == '__main__':
    test_for()
