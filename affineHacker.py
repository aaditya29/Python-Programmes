#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE= False

def main():
    myMessage="""U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG
'<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""

    hackedMessage= hackAffine(myMessage)
    
    if hackedMessage !=None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption')
        
def hackAffine(message):
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    
    #brute-force by looping through each key
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA= affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)):
            continue
        
        decryptedText=affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
            
        if detectEnglish.isEnglish(decryptedText):
            #Check with the user f the decrypted key has been found
            print()
            print('Possible encryption hack:')
            print('Key: %s' %(key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done,or just press Enter to Continue Hacking')
            response= input('>')
            if response.strip().upper().startswith('D'):
                return decryptedText
            return None
#if affineHacker.py is run as module
            if __name__== '__main__':
                main()
            