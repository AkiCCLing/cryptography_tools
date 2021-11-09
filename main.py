import dgst
import encryption
import dig_sign

def selection(sel):
    if sel == "1":
        encryption.sel()
    if sel == "2":
        dgst.dgst_sel()
    if sel == "3":
        dig_sign.sel()
    if sel == "4":
        exit()

while 1:
    sel = input("Welcome! Please Select:\n1.Encryption and Decryption\n2.Digest\n3.Digital Signature\n4.Exit\n")
    selection(sel)
