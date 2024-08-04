# num=int(input('Enter the number'))
num=15
if num==1:
    print(0)
elif num==2:
    print(1)
else:
    first=0
    sec=1
    while(num!=2):
        res=first+sec
        first=sec
        sec=res
        num-=1
    print(res)
        