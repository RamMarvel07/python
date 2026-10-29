n=int(input("enter n:"))
value=1;
for i in range(n):
    if value>n**2:
       break;
    print(value,end=" ")
    value=value*2
