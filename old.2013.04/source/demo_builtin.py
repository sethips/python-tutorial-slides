def test_sort():
    # test sorted
    l = ['1', '11', '21', '2', '13', '103']
    print('befor sorted l =', l)
    print('sort by string =', sorted(l))
    print('sort by int =', sorted(l, key=lambda x: int(x)))
    print('l is not modified after sort.', l)


def demo_print():
    print(1, 2, 4, 5)   # 會用空白連接多個 arg
    print(1, end='')    # 不讓 print 換新的一行
    print(2)
    print('1' + str(1))     # string + int 的時候記得要型別轉換

if __name__ == '__main__':
    test_sort()
    demo_print()
