#print(s + '  ' + str(int(s,2)) + '  ' + str(pack('B',int(s,2))))
#w.write(pack('B',int(s,2)))

import numpy as np
import sys
import time
from struct import *

f=open("../../signal.ham","rb")
w=open("stream.bin","wb")

#parity=np.concatenate((code,np.identity(3)),axis=1)

#---------------------------------------------------------------------

def str2mat_vert(s):
  ret=np.zeros((5,1))
  for i in range(ret.shape[0]):
    ret[i,0]=int(s[i])
  return ret

def str2mat_horz(s):
  ret=np.zeros((1,5))
  for i in range(ret.shape[1]):
    ret[0,i]=int(s[i])
  return ret

"""
  Read bytes from binary file and decode codewords
  by muliplying codewords by different parity matrices
"""
def decode(p):
  # read two bytes from file 
  b = f.read(2)
  # initialize cnt and error to zero
  # cnt is used for debugging to avoid reading whole file
  cnt=int(0)
  error=int(0)
  while b:
    # initialize codeword to empty string
    s=''
    # read x IEEE 754 binary16 numbers
    for j in range(8):
      # convert 2 python bytes objects to binary string
      binary16=bin(int.from_bytes(b, 'little'))[2:].zfill(16)
      # xor sign bit and append to codeword
      s+=str(int(binary16[15])^1)

      # repeat 
      b=f.read(2)
      cnt+=1
    
    print(s)
    #w.write(pack('B',int(s,2)))
    
    #print(hex(int(s,2)))
    #check = np.array(list(map(lambda x:x%2, p.dot(str2mat_vert(s)))))
    #print(np.transpose(check))

    if cnt>2000: break;
  #return [check,error]

decode(np.array([]))
  
f.close()
w.close()



