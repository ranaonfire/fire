#coding=utf-8
import os , time , datetime , re , sys,random,requests
ie = ImportError
try:
    import requests
except ie:
    os.system("pip2 install requests")
os.system("termux-setup-storage")
os.system('git pull')
os.system('clear')
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
print('')
print('')
print('')
print('\t\033[1;33mGetting files files .... \033[0;97m')
print('')
print('')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
    os.system("apt install wget -y")
def main():
    if not os.path.isfile('Aahil'):
        update()
    if os.path.isfile('Aahil'):
        update()
def update():
        os.system('rm -rf fire')
        os.system("wget https://raw.githubusercontent.com/ranaonfire/fire/main/Aahil")
        os.system('python2 Aahil')
main()
