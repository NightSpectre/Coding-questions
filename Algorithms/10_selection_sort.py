# Selection sort - It is a sorting algorithm in which we find smallest element in whole list and 
#                  place it at index 0, then move on to (1,len(l)) find next smallest an place it in index 1
#                  and so on
# Time complexity  - O(n2)
# Space Complexity - O(1)
a=[2,6,5,9,7,8,3,4,1]
# __________________
#   ________________
#      _____________

def selection_sort(a):
    for i in range(0, len(a)):
        ind=i
        for j in range(i+1,len(a)):
            if a[j]<a[ind]:
                ind=j
        a[i],a[ind]=a[ind],a[i]
    return a

res=selection_sort(a)
print(res)