# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Ywx 抽象工厂


# 抽象产品（手机类）
class MobilePhone:

    def call_number(self):
        pass

    def photo(self):
        pass


# 抽象产品（耳机类）
class EarPhone:

    def hear_song(self):
        pass

    def bluetooth(self):
        pass


# 具体产品 （小米手机）
class XiaoMiMobile(MobilePhone):

    def call_number(self):
        print("小米手机8,正在通话中...")

    def photo(self):
        print("这是用小米8拍摄的照片！")


# 具体产品 （小米耳机）
class XiaoMiEarPhone(EarPhone):

    def hear_song(self):
        print("您正在使用小米耳机听歌...")

    def bluetooth(self):
        print("小米蓝牙耳机连接成功!")


# 具体产品 （魅族手机）
class MeizuMobile(MobilePhone):

    def call_number(self):
        print("魅族16,正在通话中...")

    def photo(self):
        print("这是用魅族16拍摄的照片！")


# 具体产品 （魅族耳机）
class MeizuEarPhone(EarPhone):

    def hear_song(self):
        print("您正在使用魅族耳机听歌...")

    def bluetooth(self):
        print("魅族蓝牙耳机连接成功!")


# 抽象工厂
class AbstractFactory:

    # 制造手机
    def produce_phone(self):
        pass

    # 制造耳机
    def produce_earphone(self):
        pass


# 具体工厂 （小米代工厂）
class XiaomiFactory(AbstractFactory):

    def produce_phone(self):
        return XiaoMiMobile()

    def produce_earphone(self):
        return XiaoMiEarPhone()


# 具体工厂 （魅族代工厂）
class MeizuFactory(AbstractFactory):

    def produce_phone(self):
        return MeizuMobile()

    def produce_earphone(self):
        return MeizuEarPhone()


if __name__ == "__main__":

    testFactory = ''
    name = input("请输入厂商名称：").strip()    # 去除两端空格
    if name == 'xiaomi':
        testFactory = XiaomiFactory()
    elif name == 'meizu':
        testFactory = MeizuFactory()
    else:
        print('暂时没有该厂商')
        exit(0)
    phone = testFactory.produce_phone()
    earphone = testFactory.produce_earphone()
    phone.call_number()
    phone.photo()
    earphone.hear_song()
    earphone.bluetooth()
