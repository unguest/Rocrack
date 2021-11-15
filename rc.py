import sys
import os.path
import subprocess

def check_conf():

    print('[ ~ ] > Looking for all my requirements...\n')

    hashcat_test = subprocess.Popen("hashcat", stdout=subprocess.PIPE, shell=True)
    _ = hashcat_test.communicate()[0]

    if int(hashcat_test.returncode) == 255 or int(hashcat_test.returncode) == 0:
        print('[ * ] Hashcat installed')
    elif hashcat_test.returncode == 127:
        print('[ ! ] Hashcat not installed on this computer.')
        exit()
    else:
        print('[ ! ] Hashcat may be installed but not properly')
        exit()

    if not os.path.isfile('rockyou.txt'):
        print('[ ! ] rockyou.txt not found...')
        exit()
    else:
        print('[ * ] rockyou.txt is ready to break your next CTF hashes !')

    print('[ ~ ] > I\'m ready to gooo !')
    return True

def get_hash_code(txt_code):
    if txt_code.upper() == "MD5":
        return 0
    elif txt_code.upper() == "SHA1":
        return 100
    elif txt_code.upper() == "NTML":
        return 1000


if __name__ == '__main__':
    if check_conf():
        if len(sys.argv) < 3:
            print(f'Usage : {sys.argv[0]} <hash_type> <hash>')
        else:
            hash_type = sys.argv[1]
            txt_hash = sys.argv[2]

            hashcat_process = subprocess.Popen(f"hashcat -a 0 -m {get_hash_code(hash_type)} {txt_hash} rockyou.txt --force", stdout=subprocess.PIPE, shell=True)
            out, err = hashcat_process.communicate()
            print(out.decode())