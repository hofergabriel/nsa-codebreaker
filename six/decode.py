"""
Author: Gabriel Hofer
Date: 01/21/2021
Useful Commands to Remember: 
$ od -t x1 stream.bin | head -n 10
$ os.system(" echo ; hexdump -C stream.bin | head -n 10 ")
number of bytes in signal.ham --> 9633360
"""

import numpy as np
import sys
import os
import time
from struct import *
import math
FILESIZE=9633356

""" / """
def hamming_distance(string1, string2):
  dist_counter = 0
  for n in range(len(string1)):
    if string1[n] != string2[n]:
      dist_counter += 1
  return dist_counter

""" Read bytes from binary file and decode codewords """
def decode(bl_sz,f,brk):
  b=f.read(2)                                                   # read two bytes from file 
  cnt=int(0)                                                    # initialize cnt and error to zero
  ret=''
  while b:
    s=''                                                        # initialize codeword to empty string
    for j in range(bl_sz):                                          # read x IEEE 754 binary16 numbers
      binary16=bin(int.from_bytes(b, 'little'))[2:].zfill(16)   # convert 2 python bytes objects to binary string
      s+=str(int(binary16[0])^1)                                # xor sign bit and append to codeword
      b=f.read(2) 
    cnt+=1
    if cnt>brk:
      break;
    ret+=s[0:11]
  return ret

""" / """
def main0():
  f=open("../../signal.ham","rb")
  w=open("stream.bin","wb")
  stream = decode(17,f,1<<40)
  for i in range(len(stream)//8):
    w.write(pack('B',int(stream[8*i:8*i+8],2)))
  f.close() ; w.close()

def main2():
  f=open("../../signal.ham","rb")
  stream = decode(17,f,1<<7)
  for i in range(len(stream)//17):
    print(stream[17*i:17*i+17])
  f.close() ; 

main2()
exit()

def main1():
  f=open("../../signal.ham","rb")
  #w=open("stream.bin","wb")
  stream = decode(17,f,1<<40)
  d={}
  for i in range(len(stream)//8): 
    d[ stream[17*i:17*i+17] ] = 1 if stream[17*i:17*i+17] not in d else 1 + d[ stream[17*i:17*i+17] ]
  desc=sorted(d.items(), key=lambda kv: kv[1], reverse=True)
  for j in range(11):
    print()
    for i in d:
      lookup = '0'*j + '1' + '0'*(10-j)
      if i[0:11] == lookup:
        print(i + ' ' + str(d[i]))

  #w.write(pack('B',int(stream[8*i:8*i+8],2)))
  #f.close() ; w.close()

main1()
exit()

## #print(str(np.multiply(np.identity(8),np.ones((8,8)))))
## I8 = np.identity(4)
## J8 = np.array([
## 	[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
## 	[ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
## 	[ 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
## 	[ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1 ]])
## H = np.concatenate((J8,I8),axis=1)
## print(H)
## vt0 = np.fromstring('0 1 0 1 0 0 1 0 0 1 0 1 0 1 0', dtype=int, sep=' ').reshape(15,1)
## print(np.array(list((map(lambda x: x%2, H.dot(vt0).reshape(1,4))))))
## print("\n")
## vt1 = np.fromstring('0 1 0 0 1 0 1 0 0 0 1 1 1 0 1', dtype=int, sep=' ').reshape(15,1)
## print(np.array(list((map(lambda x: x%2, H.dot(vt1).reshape(1,4))))))
## # look at the codewords with ony one 1-bit!!! -- and see which parity bits are non-zero

## """ / """
## def main2():
## 	f=open("../../signal.ham","rb")
## 	stream = decode(17,f,100)
## 	for i in range(len(stream)//8):
## 		print(stream[17*i:17*i+11])
## 		vt = np.fromstring(stream[17*i:17*i+11], dtype=int, sep='')
## 		
## 		print(stream[17*i+11:17*i+16])
## 
## 	f.close()
## 	exit()

