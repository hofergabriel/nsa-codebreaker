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
  [1,0], 
  ])

parity=np.concatenate((code,np.identity(2)),axis=0)
generator = np.concatenate((np.identity(3),code),axis=1)
R = np.array([
  [1,0,0,0,0],
  [0,1,0,0,0],
  [0,0,1,0,0],
  ])

print("parity:\n"+str(parity))
print("generator:\n"+str(generator))
#exit()
#---------------------------------------------------------------------

def str2mat_vert(s):
  ret=np.zeros((5,1))
  for i in range(ret.shape[0]):
    ret[i,0]=int(s[i])
  return ret

def str2mat_horz(s):
  ret=np.zeros((1,5))
  for i in range(ret.shape[0]):
    ret[0,i]=int(s[i])
  return ret

b = f.read(2)
cnt=int(0)
while b:
  s=''
  for j in range(5):
    binary16=bin(int.from_bytes(b, 'little'))[2:].zfill(16)
    s+=binary16[15]
    b=f.read(2)
    cnt+=1

  check = np.array(list(map(lambda x: x%2, str2mat_horz(s).dot(parity) )))
  #print("check2: "+str(check))
  print(s,end=' --> ')
  Pr = R.dot(str2mat_vert(s))
  print(np.transpose(Pr))

  time.sleep(0.05)
  sys.stdout.flush()
  if cnt==100: break;

f.close()
w.close()
#print(s)
exit()


