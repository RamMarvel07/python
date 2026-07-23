sub1=int(input("Enter marks of sub1:"))
sub2=int(input("Enter marks of sub2:"))

sub3=int(input("Enter marks of sub3:"))
per=((sub1+sub2+sub3)/300)*100
print(per)
if(per>=90):
    print("Excellent performance!")
elif(per>=80):
 print("Very Good performance!") 
elif(per>=70):
   print("GOod Performance!")
elif(per>=60):
   print("Average!")
else:
   print("Poor!!")       
