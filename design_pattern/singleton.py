# 单例模式  Ywx
class Singleton(object):

    def __new__(cls, num):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':
    class SingleTest(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    test1 = SingleTest('Test')
    print(test1)
    test2 = SingleTest('ttttt')
    print(test2)
    print(test1)