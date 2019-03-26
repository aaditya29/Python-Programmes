#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math,pyperclip

def main():
    myMessage='Cenoonomms tmme oo snnio. s s c'
    myKey=8
    
    plaintext=decryptMessage(myKey,myMessage)
    print(plaintext+'|')
    
    pyperclip.copy(plaintext)

def decryptMessage(key,message):
    #The transpositon decrypt function will simulate the "columns" and
    #"rows" of the grid that the plaintext is written on by using a list
    #of strings. First, we need to calcilate a few values.
    
    #The number of "columns" in our transposition grid:
    numOfColumns=math.ceil(len(message)/key)
    #The number of "rwos" in our grid will need:
    numOfRows=key
    #The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes=(numOfColumns*numOfRows)-len(message)
    
    #Each string in plaintext represents a column in the grid.
    plaintext=['']*numOfColumns
    
    #The col and row variables point to where in the grid the next
    #character in the encrypted message will go.
    col=0
    row=0
    
    for symbol in message:
        plaintext[col]+=symbol
        col+=1#point to next column
        #If there are no more columns OR we're at a shaded box, go back to
        #the first column and the nextrow.
        if(col==numOfColumns)or(col==numOfColumns -1 and row>= numOfRows -
          numOfShadedBoxes):
            col=0
            row+=1
    return''.join(plaintext)
if __name__=='__main__':
    main()