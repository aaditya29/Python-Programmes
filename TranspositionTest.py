#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random,sys,TranspositionEncrypt,TranspositionDecrypt

def main():
    random.seed(42)
    
    for i in range(20):
        #Generate random messages to test
        
        #The message will have a random length:
        message='ABCDEFGHIJKLMNOPQRSTUVWXYZ'*random.randint(4,40)
        
        #Convert the message string to a list to shuffle it.
        message=list(message)
        random.shuffle(message)
        message=''.join(mesage)#convert list to string
        
        print('Test #%s: "%s..."'%(i+1,message[:50]))
        
        #Check all possible keys for each message.
        for key in range(1,len(message)):
            encrypted=TranspositionEncrypt.encryptMessage(key, message)
            decrypted=TranspositionDecrypt.decryptMessage(key, encrypted)
            
            #If the decryption doesn't match the original message, display
            #an error message and quit.
            if message !=decrypted:
                print('Mismatch with key %s and message %s.' %(key, message))
                print(decrypted)
                sys.exit()
                
    print('Transposition sipher test passed.')
    
    if __name__=='__main__':
        main()
        