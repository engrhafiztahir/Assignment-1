#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 50 Numpy functions
import numpy as np
# 1
a = np.arange(10)
a


# In[2]:


# 2
b = np.arange(10).reshape(2,5)
b


# In[3]:


# 3
c= np.arange(24).reshape(2,3,4)
c


# In[5]:


# 4
# Multidimension
d = np.array([[1,3],[4,5]])
d


# In[6]:


# 5
# Minimum Dimension
e = np.array([0,1,2,3,4,5,6], ndmin=3)
e


# In[7]:


# 6
# Data type Perameters
f = np.array([1,2,3,4,5,6,7,8,9,10], dtype = complex)
f


# In[8]:


# 7
g = np.array([(1,2,3),(4,5,6)])
g.ndim


# In[10]:


# 8
# Itemsize
h = np.array((1,2,3))
h.itemsize


# In[12]:


# 9
# D-type
h.dtype


# In[13]:


# 10
# Size
h.size 


# In[16]:


# 11
# Shape
c.shape


# In[21]:


# 12
# Silicing
a = np.array([(1,2,3,4),(5,6,7,8)])
print(a[0:,2])


# In[23]:


# 13
# Boolean Function
boolean_array = np.array([1, .5, 0, 'aa', ''], dtype = bool)
print(boolean_array)


# In[35]:


# 14
# Multidimension
i= np.array([(1,4),(3,5),(6,8)])
i[0:2,1]


# In[12]:


# 15
# Linearly Spacing
a = np.linspace(1,2,5)
print(a)


# In[14]:


# 16
# Minimum Values
a = np.array([50,45,57])
a.min()


# In[15]:


# 17
# Maximum Values
a.max()


# In[18]:


# 18
# Values Sum
a = np.array([110,150,255])
a.sum()


# In[19]:


# 19
# Square Root
np.sqrt(a)


# In[20]:


# 20
# Matrix Subtraction
x= np.array([(2,3,4),(1,2,3)])
y = np.array([(5,6,7),(4,5,6)])
x-y


# In[21]:


# 21
# Matrix Addation
x+y


# In[22]:


# Matrix Multiplication
x*y


# In[23]:


# 22
# Matrix Division
x/y


# In[24]:


# 23
# Vertical Stack
np.vstack((x,y))


# In[25]:


# 24
# Horizontal Stack
np.hstack((x,y))


# In[26]:


# 25
# Contiguous Flattened Array
x.ravel()


# In[27]:


# 26
# Odd Number 
arr = np.array([0,1,3,5,7,9,10,12,14,10,13,14,17,19,20])
arr[arr % 2 == 1 ]


# In[28]:


# 27
# Even number
arr[arr % 2 == 0 ]


# In[30]:


# 28
# Zero Array
arrayid = np.zeros(5)
arrayid


# In[31]:


# 29
# 2Dimensional Zero Matrix
c = np.zeros((2,3))
c


# In[38]:


# 30
# Logspace Array
A = np.logspace(4,5,num=15,base= 1000.0, dtype=float)
A


# In[48]:


# 31
# Random Number Generator
np.random.rand(4,2)


# In[60]:


# 32
# Random Number Generator with a range
np.random.randint(2, size= 4)


# In[64]:


# 33
np.random.randint(15, size= (2,2))


# In[65]:


# 34
# Identity Matrix
np.identity(4)


# In[67]:


# Digonal Matrix
np.diag(np.arange(1,5,5))


# In[71]:


# 35
# Numpy Indexing
f = np.array([1,2,3,4,5,6])
f[[1,4]]


# In[73]:


# 36
# Last Value
f[5]


# In[74]:


# 37
# Matrix Joining
Arr1= np.array([[1,2,3],[5,6,7]])
Arr2 = np.array([[2,3,4],[2,4,1]])
Arr1+Arr2


# In[75]:


# 38
# Matrix Stacking Horizontal
np.hstack((Arr1,Arr2))


# In[76]:


# Matrix Stacking Vertical
np.vstack((Arr1,Arr2))


# In[77]:


# 39
# Concatination
np.concatenate((Arr1, Arr2))


# In[81]:


# 40
# Append Value
np.append(Arr1,Arr2, axis = 1)


# In[87]:


# 41
# Trignomatry function Sine
np.sin(Arr1)


# In[89]:


# 42
# Trignomatry function Cosine
np.cos(Arr1)


# In[90]:


# 43
# Trignomatry function Tangent
np.tan(Arr1)


# In[91]:


# 44
# Logarithm function 
np.log(Arr1)


# In[92]:


# 45
# Exponential Function
np.exp(Arr1)


# In[93]:


# 46
# Square root
np.sqrt(Arr1)


# In[95]:


# 47
# Square Function
np.square(Arr1)


# In[102]:


# 48
# Circumference of circle
r=5
circumference=2*3.14*r
circumference


# In[100]:


# 49
# Area of Sphere
area=4*3.14*r*r
area


# In[103]:


# 50
# Area of circle
area=3.14*r*r
area

