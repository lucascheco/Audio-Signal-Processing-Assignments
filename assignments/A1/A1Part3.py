
import numpy as np
def hopSamples(x,M):
    ## Your code here
    arr = np.ndarray(shape = 0, dtype = int)
    for i in range(len(x)):
        if (i % M == 0):
            arr = np.append(arr, x[i])
    return arr

# Other 
def hopSamples2(x,M):
    arr = []
    for i in range(len(x)):
        if (i % M == 0):
            arr.append(x[i])
            
    return arr
    
  
  
