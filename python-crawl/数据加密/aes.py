# _*_coding :utf-8 _*_
# @Time :2022/10/21 10:43
# @File : 001
# @Project : python-crawl


import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


# cbc模式
class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    # cbc模式
    def encrypt_c(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt_c(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


# ecb模式 没有iv 偏移量
class EncryptDate:
    def __init__(self, key):
        self.key = key.encode("utf-8")              # 初始化密钥
        self.length = 16                            # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES 加密 ECB模式的实例
        self.unpad = lambda date: date[0:-ord(date[-1])]  # 截断函数，去除填充的字符

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        a = self.pad(encrData)
        res = self.aes.encrypt(a.encode("utf-8"))
        msg = str(base64.b64encode(res), encoding="utf-8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf-8"))
        msg = self.aes.decrypt(res).decode("utf-8")
        return self.unpad(msg)


if __name__ == "__main__":
    aes1 = AESCipher('6666666666666666')
    data = "hello world"

    # cbc模式
    data1 = aes1.encrypt_c(data)
    data2 = aes1.decrypt_c(data1)

    print(data1, type(data1))  # 比特流数据
    print(data2)

    # ecb模式
    aes2 = EncryptDate('6666666666666666')
    data1 = aes2.encrypt(data)
    data2 = aes2.decrypt(data1)
    print(data1)
    print(data2)

















