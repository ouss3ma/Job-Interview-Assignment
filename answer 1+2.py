#we suppose that both lists contain only unique values
#if the value does't exist we return -1 

import time
import random

l = random.sample(range(1000), 500)
l_sorted = sorted(l)

####Q1

#find function
def find (l, n):
    out = -1                      
    for i in range(len(l)):
        if l[i] == n:
            out = i
            break
    return (out)


#optimizedfind function
def find_opt (l, n):
    out = -1
    if len(l) % 2 == 0:
        range_loop = int(len(l)/2)
    else:
        range_loop = int(len(l)/2)+1
                         
    for i in range(range_loop):
        if l[i] == n:
            out = i
            break
        elif l[-i-1] ==n:
            out = len(l) - i- 1
            break
    return (out)

####Q2
def sorted_find (l,n):
    left = 0
    right = len(l)-1
    if (l[left] > n) or (l[right] < n):
        return -1
    else:
        while l[left] <= l[right]:
            m = int((left + right) / 2)
            if l[m] < n:
                left = m + 1
            elif l[m] > n:
                right = m - 1
            else:
                return m
    return -1

    
start = time.perf_counter()
print(find(l,300))
end = time.perf_counter()
print (end - start)               
     


start = time.perf_counter()
print(find_opt(l,300))
end = time.perf_counter()
print (end - start)    
    
    

start = time.perf_counter()
print(sorted_find(l_sorted,300))
end = time.perf_counter()
print (end - start)
