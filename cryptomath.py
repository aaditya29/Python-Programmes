#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def gcd(a,b):
    #Return the gcd of a and b using the Euclid's algorithm.
    while a!=0:
        a,b = b% a,a 
    return b

def findModInverse(a,m):
    #Return the modular inverse of a%m, which is
    #the number % such that a*x%m=1
    
    if gcd(a,m) !=1:
        return None#No taskperformed if a and m are not relatively prime.
    
    u1,u2,u3= 1,0,a
    v1,v2,v3=0,1,m
    while v3!=0:
        q=u3//v3
        v1,v2,v3,u1,u2,u3= (u1-q *v1), (u2 - 1 * v2), (u3- q *v3), v1,v2,v3
    return u1 % m