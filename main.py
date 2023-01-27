import numpy as np
var1=np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
var2=np.array([(1,3,2),(6,5,4)])
var3=np.array([(1,2,3),(4,5,6)])
#print(var1+var2)
#print(var1.itemsize)
#print(var1.dtype) #data type stored
#print(var1.ndim) #dimension of array
#print(var2.size) #number of elements
#print(var2.shape) #2*3
#var1=var1.reshape(3,2)
#var2=np.linspace(10,50,5) #for an array with random numbers b/w 10 and 50 having 5 elements
#print(var2)
#print(var1[0,0]) #to print first element of first array
#print(var1[0:,1]) #to print first element of each dimension
#print(var1.max())
#print(var1.min())
#print(var1.sum()) --> for sum of elements in all dimensins
#print(var2.ravel()) --> to merge all in same dimension
#print(var2.sum(axis=0)) -->sum of crresponding elements
#print(var2.sum(axis=1)) -->sum of elements in each dimensions
#print(np.sqrt(var1)) #for square root of each element
#print(np.std(var1)) #for standard deviation of each element
#print(np.__version__)
#print(type(var1))  #type which is ndarray
#print(var1.reshape(-1))  #to merge all in same dimension. flatten,ravel,anything can be used for the same
'''
for x in np.nditer(var1):  #nditer for default iteration
    print(x)
for a in var1:
    print(a)
for idx,x in np.ndenumerate(var1):  #ndenumerate for index number
    print(idx,x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')  #search sorted for sorting data

print(x)

var4=np.concatenate((var2,var3)) #add var1 and var2
print(var3)

newvar1=np.array_split(var1,3) #divide var1 in 3 parts
print(newvar1)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0) #INDEX number of odd elements

print(x)

print(np.sort(var2)) #for sorting

var2=np.array([(1,3,2),(6,5,4)])
var3=np.array([(1,2,3),(4,5,6)])
'''
a=np.array([(1,3),(6,4)])
b=np.array([(1,3),(5,6)])

print(a.dot(b)) #for matrix multiplication

r=np.random.random((3,3)) #a 3*3 matrix
print(r)

s=np.random.rand(3,3,3)  #3 times an array of 3*3 can also be (3,3) for same as random
print(s)

t=np.random.randn(3,3,3)  #negative rand
print(t)

p=np.random.randint(1,10)
p=np.random.randint(1,10,size=(3,3))
print(p)

name_list=['Puja','Aditya','Prem','Nitu']
d=np.random.choice(name_list,size=(3,3),p=[0.2,0.1,0.3,0.1,0.3])  #percentages: 20,10,30,10,30
print(d)