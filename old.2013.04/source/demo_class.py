class myFirstClass():
    X = 'First'

    def __init__(self, i):
        self.seq = i        # attribute

    def fnt1(self):         # instance method
        print(self.seq, self.X)

    def fnt2(self):
        print('Second', self.seq)

    @classmethod
    def getClsName(cls):    # class method
        print(cls.__name__, cls.X)

    @staticmethod
    def indepFnt():         # static method
        print(1*1)


class mySecondClass(myFirstClass):  # inherit from myFirstClass
    X = 'Second'

    def __init__(self, i):  # overloading
        super().__init__(i*10)
        self.son_seq = i

    def fnt2(self):
        super().fnt2()      # call myFirstClass.fnt2()
        print('Son', self.son_seq)
