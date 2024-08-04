# Inserstion sort - It is a sorting algorithm in which we use one new element 
#                   at a time
# Time complexity  - O(n2)
# Space Complexity - O(1)
a=[2,6,5,9,7,8,3,4,1]
# __
# ____
# ______

def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while key<a[j] and j>=0:   # use 2 nested for loops(instead of while) by analyzing the logic
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a
        
            
res=insertion_sort(a)
print(res)