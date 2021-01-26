"""
Author: Gabriel Hofer
Date: 01/21/2021
Useful Commands to Remember: 
$ od -t x1 stream.bin | head -n 10
"""

import numpy as np
import sys
import os
import time
from struct import *

f=open("../../signal.ham","rb")
#w=open("stream.bin","wb")

""" /// """
def hamming_distance(string1, string2):
	dist_counter = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter

""" Read bytes from binary file and decode codewords """
def decode(p):
  b=f.read(2)                                                   # read two bytes from file 
  cnt=int(0)                                                    # initialize cnt and error to zero
  ret=''
  while b:
    s=''                                                        # initialize codeword to empty string
    for j in range(8):                                          # read x IEEE 754 binary16 numbers
      binary16=bin(int.from_bytes(b, 'little'))[2:].zfill(16)   # convert 2 python bytes objects to binary string
      s+=str(int(binary16[15])^1)                                # xor sign bit and append to codeword
      b=f.read(2) 
    cnt+=1
    ret+=s
    #w.write(pack('B',int(s,2)))
    if cnt>(1<<8): break;
  return ret

""" Call decode function """
stream = decode(np.array([]))
print(stream)

""" try different codeword lengths && vary codeword size for each block length """
for i in range(8,64,8):
  print("-------------------------------------------------")
  print("blockSize: "+str(i))
  for k in range(3,i+1):
    mndist=1e9
    j=0
    while j+2*i <len(stream):
      dist=hamming_distance(stream[j:j+k],stream[j+i:j+i+k])
      if dist<mndist: mndist=dist
      j+=i
    if mndist>1:
      print("codeword size: "+str(k)+" padding: "+str(i-k)+" mindist: "+str(mndist))

















""" close files and exit """
# f.close() ; w.close()
""" dump hex in terminal """
# os.system(" echo ; hexdump -C stream.bin | head -n 10 ")




