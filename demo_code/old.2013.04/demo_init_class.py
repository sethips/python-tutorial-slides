import demo_class as dc


def demo():
    print('--- static, class method requires no object ---')
    dc.myFirstClass.indepFnt()
    dc.myFirstClass.getClsName()
    dc.mySecondClass.getClsName()

    obj1 = dc.myFirstClass(3)
    obj2 = dc.mySecondClass(7)

    print('--- class method ---')
    obj1.getClsName()
    obj2.getClsName()

    print('--- instance method ---')
    obj1.fnt1()
    obj2.fnt1()

    obj1.fnt2()
    obj2.fnt2()

if __name__ == '__main__':
    demo()
