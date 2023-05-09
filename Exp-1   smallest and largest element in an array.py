#initializing array
arr=[];
temp=0;
noofelements=int(input("enter the elements to be inserted in an array:"));
for i in range(0,noofelements):
    x=i+1 
    value=int(input("please enter the value of element %d:"%x))
    arr.append(value)
print("elements stored in an array:");
for i in range(0,noofelements):
        print(arr[i],end="");
        print();
#smallest element in an array
        temp=arr[0]
        for i in range(1,len(arr)):
            if (temp<arr[i]):
                temp=temp;
            else:
                temp=arr[i];
        print("smallest element in an array:",temp);
        print();
#largest element in an array
        for i in range(1,len(arr)):
            if(temp>arr[i]):
                temp=temp;
            else:
                temp=arr[i];
        print("largest element in an array:",temp);
        print();
