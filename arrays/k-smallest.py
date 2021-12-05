'''
Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 4 
Output: 10
'''
a=[7, 10, 4, 3, 20, 15]
k=3
a.sort()
print(a[k-1])