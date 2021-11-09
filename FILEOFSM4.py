from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from win32api import GetSystemMetrics
key = b''
key_str = ""
value = b"100"
sm4 = CryptSM4()
count = 0
#加密的文件夹
src_file = ''

#加密后的文件夹
dst_file = ''
# Encryption and Decryption
def encryption(addr,file):
    sm4.set_key(key,SM4_ENCRYPT) 
    with open(addr,'rb') as f:
        a = f.read()
    with open(addr,'wb') as f:
        b = sm4.crypt_ecb(a)
        f.write(b)
        global count
        count += 1
        print(count,"files have been encrypted")
    os.rename(file,file+".sm4")
    
def decryption(addr,file):
    sm4.set_key(key,SM4_DECRYPT)
    with open(addr,'rb') as f:
        global count
        count += 1
        print(count,"files have been encrypted")
        a = f.read()
    with open(addr,'wb') as f:
        if a==b'':
            pass
        else:
            b = sm4.crypt_ecb(a)
            f.write(b)
    os.rename(file,os.path.splitext(file)[0])

def sel(a):
    global count
    if a == "1":
        shutil.copytree(src_file,dst_file)
        for path,dir,files in os.walk(dst_file):#遍历
            for file in files:
                file = os.path.join(path,file)
                if os.path.isfile(file)==True:
                    encryption(os.path.join(path,file),file)
        messagebox.showinfo(message = "Encryption Completed!")
        count = 0
    if a == "2":
        for path,dir,files in os.walk(dst_file):#遍历
            for file in files:
                file = os.path.join(path,file)
                if os.path.isfile(file)==True:
                    decryption(os.path.join(path,file),file)
        messagebox.showinfo(message = "Decryption Completed!\nDirectory after encryption with SM4 : {}".format(dst_file))
        count = 0

# 通过win32api获取系统屏幕的分辨率
def get_system_metrics():
    return GetSystemMetrics(0),GetSystemMetrics(1)

# 传入窗口大小(分辨率)计算出窗口居中的位置
def get_window_positons(width,height):
    system_metrics =get_system_metrics()
    window_x_position = (system_metrics[0] - width)//2
    window_y_position = (system_metrics[1] - height) // 2
    return window_x_position,window_y_position

def openfolder():
    global r
    r = filedialog.askdirectory()
    r = r.replace('/','\\')
    
def en_bu():
    global r
    global src_file
    global dst_file
    src_file = r
    dst_file = src_file+".sm4"
    sel("1")
def de_bu():
    global r
    global src_file
    global dst_file
    dst_file = r
    sel("2")

fl = os.path.isfile('E:\key.txt')
if fl:
    fileofkey = open('E:\key.txt')
    fileofkey.seek(2, 0)
    key_str = fileofkey.read()
    key = bytes(key_str,"utf-8")
    fileofkey.close()
else:
    key_gen = input()
    if key_gen == "y":    
        fileofkey = open('E:\key.txt','w',encoding='utf-8')
        key = os.urandom(16)
        key_str = str(key)
        key_str = key_str.split('\'')[1]
        fileofkey.write(key_str)
        fileofkey.close()

root = Tk()
root.title("SM4加密软件")
root_width = 400
root_height = 200
r = StringVar()
r1 = StringVar()
pos = get_window_positons(root_width, root_height)
root.geometry(f'{root_width}x{root_height}+{pos[0]}+{pos[1]}')
Label(root,text = '请选择目录',width=10).place(x=110,y=50)
Button(root,text = '加密',width=8,command=en_bu).place(x=80,y=120)
Button(root,text = '解密',width=8,command=de_bu).place(x=240,y=120)
Button(root,text = '选择目录',width=8,command=openfolder).place(x=200,y=45)
root.mainloop()