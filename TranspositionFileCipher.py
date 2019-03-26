#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, os,sys, TranspositionEncrypt, TranspositionDecrypt
 
def main():
    inputFilename='frankenstein.txt'
    outputFilename='frankenstein.encrypted.txt'
    myKey=10
    myMode='encrypt'
    
    #If the input file does not exist, then the program terminates early.
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...'%(inputFilename))
        sys.exit()
        
    #If the output file already exist give the user a chance to exit
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit'%
              (outputFilename))
        response=input('>')
        if not response.lower().startswith('c'):
            sys.exit()
            
    
    #Read in the message from the input file
    fileObj=open(inputFilename)
    content=fileObj.read()
    fileObj.close()
    
    print('%sing...' %(myMode.title()))
    
    #Measure how long the encryption/decryption takes.
    startTime=time.time()
    
    if myMode=='encrypt':
        translated= TranspositionEncrypt.encryptMessage(myKey, content)
    elif myMode=='decrypt':
        translated= TranspositionDecrypt.decryptMessage(myKey, content)
    totalTime=round(time.time()-startTime, 2)
    print('%sion time: % seconds' %(myMode.title(),totalTime))
    
    #Write out the translated message to the output file
    outputFileObj=open(outputFilename,'w')
    outFileobj.write(translated)
    outputFileObj.close()
    
    print('Done %sing %s (5s characters).' %(myMode, inputFilename,
          len(content)))
    print('%sed file is %s.' %(myMode.title(), outputFilename))
    
if __name__=='__main__':
    main()