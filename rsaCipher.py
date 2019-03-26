#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#IMPORTANT: The block size must be less than the key size
#Note: The block size in bits and key size in bytes
DEFAULT_BLOCK_SIZE= 128 #128 bytes
BYTE_SIZE= 256 #One byte has 256 different values

def main():
    #Runs a test that encrypts a message to a file or decrypts a message
    #from a file.
    filename = 'encrypted_file.txt'#the file to write to/read from
    mode= 'encrypt' # set to 'encrypt' or 'decrypt'
    
    if mode == 'encrypt':
        message = '''"Journalists belong in the utter because that is where the
        ruling classes throw their guilty secrets." -Gerald Priestland "The Founding
        Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
        pubKeyFilename = 'al_sweigart_pubkey.txt'
        print('Reading from %s and decrypting...' %(filename))
        encryptedText = encryptAndWriteToFile(filename, pubkeyFilename, message)
        
        print('Encrypted text:')
        print(encryptedText)
    
    elif mode== 'decrypt':
        privKeyFilename= 'al_sweigart_privkey.txt'
        print('Reading from %s and decrypting...' %(filename))
        decryptedText = readFromFileAndDecrypt(filename, priveKeyFilename)
        
        print('Decrypted text.')
        print(decryptedText)
        
def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    #cONVERTS A STRING MESSAGE TO A LIST OF BLOCK INTEGERS. Each integer
    # represents 128 (or whatever blockSize is set to) string characters.
    messageBytes = message.encode('ascii')#convert the string to bytes
    
    blockInts - []
    for i in range(blockStart, min(blockStart + blockSize, (messageBytes))):
        blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
    blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize = DEFAULT_BLOCK_SIZE):
    #Converts a list of block integers to the original message string.
    #The original message length is needed to properly the last
    #block integer.
    message=[]
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i< messageLength:
                #Decode the message string for the 128( or whatever
                # blockSize is set to) characters from this block integer.
                asciinumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt% (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
            message.extend(blockMessage)
        return''.join(message)


def encryptMessage(message, key, blockSize = DEFAULT_BLOCK_SIZE):
    #Converts the message string into a list of block integers, and then
    #encrypts each block integer. Pass the PUBLIC key to encrypt.
    encryptedBlocks = []
    n, e = key
    
    for block in getBlocksFromTest(message, blockSize):
        #ciphertext = plaintext ^ e mod n
        encryptedBlocks.append(pw(block, e, n))
    return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize= DEFAULT_BLOCK_SIZE):
    #Decrypts a list of encrypted block ints into the original message
    #string. The original message length is required to properly decrypt
    #the last block. Be sure to pass the PRIVATE key to decrypt.
    decryptedBlocks = []
    n, e = key
    for block in encryptedBlocks:
        #plaintext = ciphertext ^ d mod n
        decryptedBlocks.append(pw(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
    #Given the filename of a file that contains a public or private key.
    #return the key as a (n, e) or (n, d) tuple value.
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize, n, EorD= content.split(',')
    return (int(keySize), int(n), int(EorD))

def encryptAndWriteToFile(messageFilename, keyFileName, message, blockSize= DEFAULT_BLOCK_SIZE):
    #Using a key from a key file, encrypt the message and save it to a
    #file. Returns the encrypted message string.
    keySize, n, e = readKeyFile(keyFilename)
    
    #Check that key size ie greater than block size
    if keySize< blockSize * 8:
        sys.exit(''''ERROR: Block size is % bits and key size is %s bits.
                 The RSA cipher requires the block size to be equal to or less than the key size.
                 Either increase the block size or use a different keys.''''
                 %(blockSuze * 8, keySize))
        
        
        #Encrypt the message
        encryptedBlocks = encryptedMessage(message, (n, e), blockSize)
        
        #Convert the large int values to one string value.
        for i in range(len(encryptedBlocks)):
            encryptedBlocks[i]= str(encryptedBlocks[i])
        encryptedContent = ','.join(encryptedBlocks)
        
        #Write out the encrypted string to the output file.
        encryptedContent = '%s_%s_%s' %(len(message), blockSize, encryptedContent)
        fo=open(messageFilename, 'w')
        fo.write(encryptedContent)
        #also return the encrypteed string.
        return encryptedContent

def readFromFileAndDecrypt(messageFilename, keyFilename):
mn    Using a key from a key                