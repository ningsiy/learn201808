# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Ywx 适配器模式


# 手机解锁类
class MobileUnlock:

    def unlock(self):
        pass


# 密码解锁
class PwdUnlock(MobileUnlock):

    def unlock(self):
        print("密码解锁")


# 指纹解锁
class FingerprintUnlock(MobileUnlock):

    def unlock(self):
        print("指纹解锁")


# 人脸解锁 (待适配类)
class FaceUnlock:

    def face_unlock(self):
        print("人脸解锁")


# 适配类
class Adapter(MobileUnlock):

    def __init__(self):
        self.face = FaceUnlock()

    def unlock(self):
        self.face.face_unlock()


if __name__ == '__main__':

    password = PwdUnlock()
    finger = FingerprintUnlock()
    face = Adapter()

    password.unlock()
    finger.unlock()
    face.unlock()
