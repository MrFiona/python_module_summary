#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-04-05 21:26
# Author  : MrFiona
# File    : summary_AES.py
# Software: PyCharm



import base64
from Cryptodome.Cipher import AES
# from Cryptodome.Util.Padding import pad, unpad

BLOCK_SIZE = 16
PADDING = b'\0'
key = b'B31F2A75FBF94099'
iv = b'B31F2A75FBF94099'

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * bytes(chr(BLOCK_SIZE - len(s) % BLOCK_SIZE), encoding='utf-8')
unpad = lambda s: s[:-ord(s[len(s)-1:])]

#使用aes算法，进行加密解密操作
#为跟java实现同样的编码，注意PADDING符号自定义
def encrypt_aes(sourceStr):
    generator = AES.new(key, AES.MODE_ECB)
    crypt = generator.encrypt(pad(sourceStr))
    cryptedStr = base64.b64encode(crypt)
    print("cryptedStr_1:\t", cryptedStr)
    return cryptedStr

def decrypt_aes(cryptedStr):
    generator = AES.new(key, AES.MODE_ECB)
    cryptedStr = base64.b64decode(cryptedStr)
    print("cryptedStr_2:\t", cryptedStr)
    recovery = unpad(generator.decrypt(cryptedStr))
    decryptedStr = recovery.rstrip(PADDING)
    return decryptedStr

sourceStr = b'B31F2A75FBF94099'
encry = encrypt_aes(sourceStr)
print('original secret:\t', encry)
print(decrypt_aes(encry))

