# num=int(input('Enter the number'))
num=101
if num==0 or num==1:
    print("Not a prime")
elif num==2 or num==3:
    print("Is a prime")
else:
    flag=False
    for i in range(2,(num//2)+1):
        if num%i==0:
            print('Not a prime')
            flag=True
            break
    if flag is False:
        print('Is a prime')
