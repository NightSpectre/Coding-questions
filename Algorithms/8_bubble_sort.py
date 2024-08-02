# Bubble Sort - It is a sorting algorithm in which elements are sorted in ascending or descending 
#               order based on requirement

# For ascending, the first number is compare with second number, if 1st number is larger than second number,
# then the numbers are swapped, we keep on doing this until the last number is largest, This step is continued 
# for next (n-1) numbers, then (n-2) numbers, so on until all the numbers are sorted 

# Time Complexity - O(n2)
# Space complexity - O(1)


def bubble_sort(l):
    j=len(l)-1
    while j!=0:
        for i in range(0,j):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
        j-=1
    return l

l=[2,6,5,9,7,8,3,4,1]
res=bubble_sort(l)
print(res)