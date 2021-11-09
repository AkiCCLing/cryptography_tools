import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def sel():
    stu_id = input("Please input your student ID:\n")
    stu_id="    "+stu_id
    stu_id = bytes(stu_id,"utf-8")
    select = input("Please Select:\n1.AES\n2.3DES\n3.IDEA\n4.RSA")
    if select == "1":
        AES(stu_id)
    if select == "2":
        DES_3(stu_id)
    if select == "3":
        IDEA(stu_id)
    if select == "4":
        RSA(stu_id)

#Encryption and Decryption of AES
def AES(stu_id):
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(stu_id) + encryptor.finalize()
    print("Encryption of AES :"+ct.hex())
    decryptor = cipher.decryptor()
    print("Decryption of AES :",decryptor.update(ct) + decryptor.finalize())
    print("\n")
    os.system('pause')

#Encryption and Decryption of 3DES
def DES_3(stu_id):
    key = os.urandom(8)
    iv = os.urandom(8)
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(stu_id) + encryptor.finalize()
    print("Encryption of 3DES:"+ct.hex())
    decryptor = cipher.decryptor()
    print("Decryption of 3DES:",decryptor.update(ct) + decryptor.finalize())
    print("\n")
    os.system('pause')

#Encryption and Decryption of IDEA
def IDEA(stu_id):
    key = os.urandom(16)
    iv = os.urandom(8)
    cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(stu_id) + encryptor.finalize()
    print("Encryption of IDEA:"+ct.hex())
    decryptor = cipher.decryptor()
    print("Decryption of IDEA:",decryptor.update(ct) + decryptor.finalize())
    print("\n")
    os.system('pause')

#Encryption and Decryption of RSA
def RSA(stu_id):
    stu_id_en = ""
    stu_id_de = ""
    stu_id = bytes(stu_id,encoding = 'utf-8')
    with open("my_public.key", "rb") as key_file:
        pub_key = key_file.read()
    print(pub_key)
    public_key = serialization.load_pem_public_key(pub_key)
    print("\n")
    encryption = public_key.encrypt(stu_id,padding.PKCS1v15())
    print("Encryption of RSA:",encryption.hex(),"\n")
    with open("my_private.key", "rb") as key_file:
        pri_key = key_file.read()
    private_key = serialization.load_pem_private_key(pri_key,password=None)
    decryption = private_key.decrypt(encryption,padding.PKCS1v15())
    decryption = str(decryption)
    decryption = decryption.split('\'')[1]
    print("Decryption of RSA:",decryption,"\n")
    os.system('pause')