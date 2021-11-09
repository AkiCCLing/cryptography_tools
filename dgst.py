from cryptography.hazmat.primitives import hashes
import os
def dgst_sel():
    stu_id = input("Please input your student ID:")
    stu_id = bytes(stu_id, encoding="utf8")
    select = input("Please Select:\n1.SHA-1\n2.SHA-256\n3.SHA-512\n4.MD5\n")
    if select == "1":
        sha_1(stu_id)
    if select == "2":
        sha_256(stu_id)
    if select == "3":
        sha_512(stu_id)
    if select == "4":
        MD5(stu_id)

def sha_1(stu_id):
    digest = hashes.Hash(hashes.SHA1())
    digest.update(stu_id)
    output = digest.finalize()
    print('SHA1 Digest:', output.hex())
    os.system('pause')

def sha_256(stu_id):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(stu_id)
    output = digest.finalize()
    print('SHA256 Digest:', output.hex())
    os.system('pause')

def sha_512(stu_id):
    digest = hashes.Hash(hashes.SHA512())
    digest.update(stu_id)
    output = digest.finalize()
    print('SHA512 Digest:', output.hex())
    os.system('pause')

def MD5(stu_id):
    digest = hashes.Hash(hashes.MD5())
    digest.update(stu_id)
    output = digest.finalize()
    print('MD5 Digest:', output.hex())
    os.system('pause')