myVal = 3
def myFunc(x: int) -> int:
   global myVal
   myVal += x #seiteneffekt
   #print(myVal)
   return x*x
print(myFunc(42.5), myVal)

def myRecursive():