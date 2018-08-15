# 简单工厂  Ywx


class Php:
    def __init__(self, lan):
        self.lan = lan

    def say(self):
        return self.lan + '实现简单工厂模式'


class Python:
    def __init__(self, lan):
        self.lan = lan

    def say(self):
        return self.lan + '实现简单工厂模式'


class UnknowLan:
    def say(self):
        return '操作错误！'


class Factory:
    def __init__(self, language):
        self.language = language

    def get_say(self):
        if self.language == 'php':
            return Php(self.language)
        elif self.language == 'python':
            return Python(self.language)
        else:
            return UnknowLan()


def test_fac():
    lan = input('请输入编程语言：')
    fac = Factory(lan)
    get_say = fac.get_say()
    say = get_say.say()
    print(say)


test_fac()
