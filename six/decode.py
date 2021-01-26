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
      s+=str(int(binary16[0])^1)                                # xor sign bit and append to codeword
      b=f.read(2) 
      cnt+=1
    ret+=s
    #w.write(pack('B',int(s,2)))
    if cnt>(1<<10): break;
  return ret

""" Call decode function """
stream = decode(np.array([]))
#print(stream)

""" need to try different codeword lengths """
for i in range(4):
  print("block size: "+str(8*(i+1)))
  mxdist=0
  avgdist=0
  cnt=0
  j=0
  print("dist: ",end='')
  while j+16*(i+1)-1<len(stream):
    dist=hamming_distance(stream[j:j+8*(i+1)],stream[j+8*(i+1):j+16*(i+1)])
    if dist>mxdist: mxdist=dist
    j+=8*(i+1)
    print(str(dist),end=' ')
    avgdist+=dist
    cnt+=1
  print()
  print("avgdist: "+str(avgdist/cnt))
  print("mxdist: "+str(mxdist))
  print()





""" close files and exit """
# f.close() ; w.close()
""" dump hex in terminal """
# os.system(" echo ; hexdump -C stream.bin | head -n 10 ")




