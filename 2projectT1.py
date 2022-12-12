Num = int(input("Enter the range of Number: "))
i=0
F_val=0
S_val=1
while(i<Num):
    if(i<=1):
        Next=i
    else:
        Next=F_val+S_val
        F_val=S_val
        S_val=Next
    print(Next)
    i=i+1