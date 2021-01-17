#print(s + '  ' + str(int(s,2)) + '  ' + str(pack('B',int(s,2))))
#w.write(pack('B',int(s,2)))

import numpy as np
import sys
import time
from struct import *

f = open("../../signal.ham","rb")
w = open("stream.bin","wb")

parity = np.array([ 
  [0,0], 
  [1,1], 
  [1,0], 
  ])

res=np.concatenate((parity,np.identity(2)),axis=0)

print("res: "+str(res))

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

  print(s,end=' ')
  #check = np.transpose(np.array(list(map(lambda x: x%2, res0.dot(str2mat_vert(s)) ))))
  check = np.array(list(map(lambda x: x%2, str2mat_horz(s).dot(res) )))
  print("check2: "+str(check))

  time.sleep(0.05)
  sys.stdout.flush()
  if cnt==100: break;

f.close()
w.close()
#print(s)
exit()

