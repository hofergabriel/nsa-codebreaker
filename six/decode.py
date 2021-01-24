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
w=open("stream.bin","wb")

""" binary string --> vector of boolean (ints) """
def str2mat_vert(s):
  ret=np.zeros((5,1))
  for i in range(ret.shape[0]):
    ret[i,0]=int(s[i])
  return ret

""" binary string --> vector of boolean (ints) """
def str2mat_horz(s):
  ret=np.zeros((1,5))
  for i in range(ret.shape[1]):
    ret[0,i]=int(s[i])
  return ret

""" Read bytes from binary file and decode codewords """
def decode(p):
  b=f.read(2)                                                   # read two bytes from file 
  cnt=int(0)                                                    # initialize cnt and error to zero
  while b:
    s=''                                                        # initialize codeword to empty string
    for j in range(8):                                          # read x IEEE 754 binary16 numbers
      binary16=bin(int.from_bytes(b, 'little'))[2:].zfill(16)   # convert 2 python bytes objects to binary string
      s+=str(int(binary16[0])^1)                                # xor sign bit and append to codeword
      b=f.read(2) 
      cnt+=1
    print(s + '  ' + str(hex(int(s,2))))
    w.write(pack('B',int(s,2)))
    if cnt>256: break;
  return []

""" Call decode function """
decode(np.array([]))
  
""" close files and exit """
f.close()
w.close()

""" dump hex in terminal """
os.system(" echo ; hexdump -C stream.bin | head -n 10 ")


"""
#check = np.array(list(map(lambda x:x%2, p.dot(str2mat_vert(s)))))
#print(np.transpose(check))
#print(hex(int(s,2)))
"""





