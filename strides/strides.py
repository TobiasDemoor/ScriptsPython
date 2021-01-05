# https://towardsdatascience.com/advanced-numpy-master-stride-tricks-with-25-illustrated-exercises-923a9393ab20
#%% imports
from numpy.lib.stride_tricks import as_strided
import numpy as np

#%% ej 1
arr = np.array(range(1,26), np.int8).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(3,), strides=(1,))
print(new)

# %% ej 2
arr = np.array(range(1,26), np.int8).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(8,), strides=(1,))
print(new)

# %% ej 3
arr = np.array(range(1,26), np.int16).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(25,), strides=(2,))
print(new)

# %% ej 4
arr = np.array(range(1,26), np.int8).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(3,), strides=(2,))
print(new)
 
# %% ej 5
arr = np.array(range(1,26), np.int64).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(4,), strides=(40,))
print(new)
 
# %% ej 6
arr = np.array(range(1,26), np.int64).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(5,), strides=(48,))
print(new)
 
# %% ej 7
arr = np.array(range(1,26), np.int64).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(5,), strides=(0,))
print(new)
 
# %% ej 8
arr = np.array(range(1,26), np.int64).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(3,4), strides=(40,8))
print(new)
 
# %% ej 9
arr = np.array(range(1,26), np.int64).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(4,2), strides=(48,8))
print(new)
 
# %% ej 10
arr = np.array(range(1,26), np.int64).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(3,3), strides=(80,16))
print(new)
 
# %% ej 11
arr = np.array(range(1,26), np.int8).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(3,3), strides=(1,5))
print(new)
 
# %% ej 12
arr = np.array(range(1,26), np.int32).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(5,4), strides=(20,0))
print(new)
 
# %% ej 13
arr = np.array(range(1,13), np.int64)
print(arr)
new = as_strided(arr, shape=(4,3), strides=(24,8))
print(new)
 
# %% ej 14
arr = np.array(range(1,11), np.int8)
print(arr)
new = as_strided(arr, shape=(8,3), strides=(1,1))
print(new)
 
# %% ej 15
l = []
for i in range(6):
    n = i *10
    l.append(range(n, n+2))
arr = np.array(l, np.int8)
print(arr)
new = as_strided(arr, shape=(4,6), strides=(2,1))
print(new)
 
# %% ej 16
arr = np.array(range(1,13), np.int8).reshape(3,2,2)
print(arr)
new = as_strided(arr, shape=(3,4), strides=(4,1))
print(new)
 
# %% ej 17
arr = np.array(range(1,26), np.int16).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(2,2,2), strides=(30,10,2))
print(new)
 
# %% ej 18
arr = np.array(range(1,26), np.int8).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(2,2,3), strides=(10, 6, 1))
print(new)
 
# %% ej 19
arr = np.array(range(1,26), np.int16).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(3,2,4), strides=(0, 10, 2))
print(new)
 
# %% ej 20
arr = np.array(range(1,13), np.int32).reshape(3,2,2)
print(arr)
new = as_strided(arr, shape=(3,2,2), strides=(16,4,8))
print(new)
 
# %% ej 21
arr = np.array(range(1,21), np.int64).reshape(4,5)
print(arr)
new = as_strided(arr, shape=(3,2,5), strides=(40,40,8))
print(new)
 
# %% ej 22
arr = np.array(range(1,13), np.int8)
print(arr)
new = as_strided(arr, shape=(2,2,3), strides=(6,3,1))
print(new)
 
# %% ej 23
arr = np.array(range(1,26), np.int8).reshape(5,5)
print(arr)
new = as_strided(arr, shape=(2,2,3,3), strides=(10,2,5,1))
print(new)
 
# %% ej 24
arr = np.array(range(1,13), np.int64).reshape(2,2,3)
print(arr)
new = as_strided(arr, shape=(2,2,2,3), strides=(48,0,24,8))
print(new)
 
# %% 25
arr = np.array(range(1,17), np.int64)
print(arr)
new = as_strided(arr, shape=(2,2,2,2), strides=(64,32,16,8))
print(new)
 

# %%
