list1=[2,4,3,5,7,6]
list2=[3,5,4,1,9,2]
thirdList=[]

for i in list1:
    if(i%2 != 0):
        thirdList.append(i)

for j in list2:
    if(j%2==0):
        thirdList.append(j)

print(thirdList)
