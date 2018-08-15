# 单例模式  Ywx
class Singleton(object):

    def __new__(cls, num):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam('spam')
    print(s1)
    s2 = SingleSpam('spa')
    print(s2)
    print(s1)