import numpy as np

a = np.array([(1,2,3,4),(3,1,4,2)])

print ("Original array:\n ") 
print(a)
print ("Dimension of array-> " , (a.ndim))
print("\nOutput for RAVEL \n") 

b = a.ravel()
print(b)

b[0]=1000

print(b)

print(a)

print ("Dimension of array->" ,(b.ndim))

print("\nOutput for FLATTEN \n") 

c = a.flatten()

print(c)

c[0]=0

print(c)

print(a)

print ("Dimension of array-> " , (c.ndim))
