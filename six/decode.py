"""
Author: Gabriel Hofer
Date: 01/21/2021
Useful Commands to Remember: 
$ od -t x1 stream.bin | head -n 10

number of bytes in signal.ham --> 9633360
"""


import numpy as np
import sys
import os
import time
from struct import *


""" /// """
def hamming_distance(string1, string2):
	dist_counter = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter

""" Read bytes from binary file and decode codewords """
def decode(b_sz):
	b=f.read(2)                                                   # read two bytes from file 
	cnt=int(0)                                                    # initialize cnt and error to zero
	ret=''
	allzeros=True
	while b:
		s=''                                                        # initialize codeword to empty string
		for j in range(b_sz):                                          # read x IEEE 754 binary16 numbers
			binary16=bin(int.from_bytes(b, 'little'))[2:].zfill(16)   # convert 2 python bytes objects to binary string

			#binary16 = binary16[0:8] + binary16[8:16]

			s+=str(int(binary16[0])^1)                                # xor sign bit and append to codeword
			b=f.read(2) 
		cnt+=1
		ret+=s
		#print(s[len(s)-10:len(s)-1])
		if s[len(s)-1]=='0':
			allzeros=False
		#w.write(pack('B',int(s,2)))
		if cnt>(1<<4): break;
		#if cnt>(1<<18): break;
	return allzeros

#w=open("stream.bin","wb")

#stream = decode(8)
import math

for i in range(10,int(math.sqrt(9633360))+1):
	f=open("../../signal.ham","rb")
	if 9633360%i==0:
		print("i: "+str(i))
		z1=decode(i)
		print("allzeros: "+str(z1))

		print("i: "+str(9633360 // i))
		z2=decode( 9633360 // i)
		print("allzeros: "+str(z2))

		if z1 or z2:
			exit()
	f.close() 
	print()


exit()









""" close files and exit """
f.close() ; w.close()
""" dump hex in terminal """
# os.system(" echo ; hexdump -C stream.bin | head -n 10 ")


