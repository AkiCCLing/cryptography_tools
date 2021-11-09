import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

def sel():
    stu_id = input("Please your student ID:")
    stu_id = bytes(stu_id,encoding='utf-8')
    fh = open('stu_id.txt', 'wb')
    fh.write(stu_id)
    fh.close()
    if os.path.isfile('E:\my_private.key') == 0:
        os.system('openssl genrsa -out my_private.key 1024')
    if os.path.isfile('E:\my_public.key') == 0:
        os.system('openssl rsa -in my_private.key -pubout -out my_public.key')
    with open("my_private.key", "rb") as key_file:
        pri_key = key_file.read()
    private_key = serialization.load_pem_private_key(pri_key,password=None)
    sign = private_key.sign(stu_id,padding.PKCS1v15(),hashes.SHA256())
    with open("my_public.key", "rb") as key_file:
        pub_key = key_file.read()
    public_key = serialization.load_pem_public_key(pub_key)
    while 1:
        try:
            public_key.verify(sign,stu_id,padding.PKCS1v15(),hashes.SHA256())
            print("匹配")
            print("当前签名：",sign)
            print("当前STU_ID:",stu_id)
            os.system('pause')
        except:
            print("不匹配")
            print("当前签名：",sign)
            print("当前STU_ID:",stu_id)
            os.system('pause')
            os.system("cls")
            break
        print("使用学号201931224000进行签名\n")
        sign = private_key.sign(b'201931224000',padding.PKCS1v15(),hashes.SHA256())