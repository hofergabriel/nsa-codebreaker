#print(s + '  ' + str(int(s,2)) + '  ' + str(pack('B',int(s,2))))
#w.write(pack('B',int(s,2)))

import numpy as np
import sys
import time
from struct import *

f=open("../../signal.ham","rb")
w=open("stream.bin","wb")

code = np.array([ 
  [0,0], 
  [1,1], 
  [0,1], 
  ])

parity=np.concatenate((code,np.identity(2)),axis=0)
generator = np.concatenate((np.identity(3),code),axis=1)
R = np.array([
  [1,0,0],
  [0,1,0],
  ])

#print("parity:\n"+str(parity))
#---------------------------------------------------------------------

def str2mat_vert(s):
  ret=np.zeros((3,1))
  for i in range(ret.shape[0]):
    ret[i,0]=int(s[i])
  return ret

def str2mat_horz(s):
  ret=np.zeros((1,3))
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
    for j in range(3):
      # convert 2 python bytes objects to binary string
      binary16=bin(int.from_bytes(b, 'little'))[2:].zfill(16)
      # xor sign bit and append to codeword
      s+=str(int(binary16[15])^1)
      # repeat 
      b=f.read(2)
      cnt+=1

    # multiply codeword array with parity check matrix
    check = np.array(list(map(lambda x: x%2, str2mat_horz(s).dot(p) )))
        #print(check)
        #Pr = R.dot(str2mat_vert(s))
        #print(s+" --> "+str(np.transpose(Pr)))
    
    # count errors
    error+=check[0,0]+check[0,1]
    if cnt>100: break;
  return [check,error]


"""
  generate all possible parity matrices
"""
def bruteforce():
  mn=1000
  for i in range(64):
    bs=bin(i)[2:].zfill(6)
    p=np.zeros((3,2))
    p[0,0]=bs[0]
    p[0,1]=bs[1]
    p[1,0]=bs[2]
    p[1,1]=bs[3]
    p[2,0]=bs[4]
    p[2,1]=bs[5]
    # p[3,0]=bs[6]
    # p[3,1]=bs[7]
    # p[4,0]=bs[8]
    # p[4,1]=bs[9]
    # p=np.concatenate((p,np.identity(2)),axis=0)
    #print(p)
    [ch,err]=decode(p)
    if(err<mn):
      mn=err
    if err<=20:
      print("---------------------------------------\n")
      print("parity: ")
      print(p)
      print("check: ")
      print(ch)
      print("err: "+str(err))
  
  print("mn: "+str(mn))

bruteforce()

  
f.close()
w.close()



