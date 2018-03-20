a=[]
num=int(input("Enter number of elements:"))
for i in range(1,num+1):
    c=int(input("Enter element:"))
    a.append(c)
a.sort()
print("Largest element is:",a[num-1])
