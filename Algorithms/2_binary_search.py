# Binary search - It is a searching algorithm, but the elements in the list have to be sorted first

# Time complexity - O(log n)
# Space Complexity - O(1)

def binary_search(lis,num):
    l=len(lis)
    low=0
    high=l
    while low<=high:
        mid=(low+high)//2
        if num==lis[mid]:
            return mid
        elif num<lis[mid]:
            high=mid-1
        else:
            low=mid+1
lis=[-1, 0, 3, 4, 9]
num=4
index=binary_search(lis,num)
print('Index is '+str(index))