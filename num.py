'''import numpy as np
a=np.array([1,2,3,4,5])
print(a)
print("Total:",sum(a))
print("Maximum:",max(a))
print("Minimum:",min(a))
print("Average:",a.mean())
'''


'''import numpy as np
a=np.array([1,2,3,4,5])
print("Type:",type(a))
print("Datatype:",a.dtype)'''


'''import numpy as np
try:
 a=np.array([1,2,3,4,5])
 b=np.array([6,7,8,9])
 result=a+b
 print(result)
except:
 print("not valid")
finally:
 print("end")


 import numpy as np
 a=np.arange(1,21)
 print(a)
'''

'''import numpy as np
a=np.arange(1,0,-21)
print(a)

import numpy as np
a=np.arange(2,51,2)
print(a)

a=np.arange(1,51,2)
print(a)

a=np.arange(1,11)
for i in range(1,11):
    print(5*i)

'''    


'''import numpy as np
a=np.array([10,20,30,40,50])
print(a)
print("Total:",sum(a))
print("Maximum:",max(a))
print("Minimum:",min(a))
print("Average:",a.mean())
print("Type:",type(a))
print("Datatype:",a.dtype)
print("multiplication:",a*2)
'''


'''import numpy as np
a=np.zeros(5)
print(a)
a=np.ones(5)
print(a)
a=np.arange(1,11)
print(a)'''

'''
import numpy as np

a=np.array([1,2,3,4,5])
print(a[4])
print(a[-2])'''
'''
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a[1,3])

'''


'''import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
print(a[2,1])


import numpy as np
a=np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
print("Average:",a.mean())

import numpy as np
a=np.array([1,2,3,4,5])
print(a[1:4])
print(a[:4])
print(a[4:])'''

'''
import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([[1,2,3,4,5,6]])
c=np.array([[[1,2,3,4,5,6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)'''


# import numpy as np
# a=np.array([[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]])
# print(a)
# print(a[:-5])

'''
import numpy as np

a=([[[1,2,3,],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]])
print(a[0][4][2])
'''


# import numpy as np
# a=np.array([1,2,3,4,5,6,7])
# print(a)
# print("Total:",sum(a))
# print("Maximum:",max(a))
# print("Minimum:",min(a))
# print("Arange:",a.mean())
# print(a.ndim)
# print(a.shape)


# import numpy as np
# a=np.array([[1,2,3,4,5,6],
#             [7,8,9,10,11]])
# print(a[1,4])
# print(a.ndim)



# import numpy as np
# a=np.array([[[1,2,3,4,5,6,7,8,9]]])
# print(a)
# print(a[0,0,1:4])
# print(a[0,0,:4])
# print(a[0,0,4:])


# import numpy as np 
# a=np.array( [[[1,2,3],[5,6,7],[7,8,9],[10,11,12]]])
# print(a[0][3][2])




# import numpy as np
# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a[2,1:3])


# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print("A dimension:",a.ndim)

# # x=a.reshape(2,6)
# # x=a.reshape(3,4)
# x=a.reshape(4,3)
# print(x)

# print("shape:",x.shape)
# print("X dimension:",x.ndim)



# import numpy as np
# a=np.array([[[[[1,2,3,4],[5,6,7,8],[9,10,11,12]]]]])
# print(a)
# print("A dimension:",a.ndim)
# print("Shape of array:",a.shape)


# x=a.reshape(3,4)
# print(x)    

# import numpy as np
# a=np.array([1,2,3,4,5,6])
# # reshape=a.reshape(2,3)
# # print(reshape)
# new=np.resize(a,(2,4))
# print(new)

# #
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9,10])
# print(a)
# print("arange",a.mean())
# new=np.resize(a,(3,5))
# print(new)
# b=a.reshape(2,4)
# print(b)


# import numpy as np
# b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(b)
# new=np.resize(b,(4,7))
# print(new)
# print("arenge:",b.mean())


# import numpy as np
# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print("Original Array:",a)
# print("Dimension is:",a.ndim)
# new=np.unique(a)
# print("Unique Array:",new)
# new1=np.unique(a).size
# print("Unique Array Count:",new1)
# new2=np.resize(a,(1,3,5))
# print("resize Array:",new2)
# b=np.unique(new2)
# print("unique Array:",b)
# c=np.unique(new2).size
# print("unique array count:",c)
# print("dimension is:",new2.ndim)



# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print("Original Array:",arr)
# slicing=arr[2:6].copy()
# slicing[:]=0
# print(slicing)
# print("original Array:",arr)

# import numpy as np
# a=np.array([[[1,2,3,4,5,6,7,8,9,10]]])
# print("original Array:",a)
# slicing=a[0,0,0:6].copy()
# slicing[:]=0
# print(slicing)
# print("Original Array:",a)





