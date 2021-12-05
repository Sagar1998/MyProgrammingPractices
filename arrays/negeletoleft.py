'''
Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
'''
a=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
j = 0
for i in range(0, len(a)) :
        if (a[i] < 0) :
            temp = a[i]
            a[i] = a[j]
            a[j]= temp
            j = j + 1
print(a)
