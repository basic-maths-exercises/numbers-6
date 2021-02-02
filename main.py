import numpy as np

def convertToHex( N ) :
  myhex = 5*["0"]
  # Your code goes here
  for i in range(5) : 
      ppp = 16**(4-i)
      vvv = np.floor( N / ppp )
      N = N - vvv*ppp
      if vvv==10 : myhex[i]="A"
      elif vvv==11 : myhex[i]="B"
      elif vvv==12 : myhex[i]="C"
      elif vvv==13 : myhex[i]="D"
      elif vvv==14 : myhex[i]="E"
      elif vvv==15 : myhex[i]="F"
      else : myhex[i] = str(vvv) 
  return myhex
  
for i in range(32) : 
  print( "The number", i, "is", convertToHex(i), "in hex.")
