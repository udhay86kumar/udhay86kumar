from re import I


#Bubble sort:
"""arr=[2,45,36,38,39,53,32,64,100]
for j in range(len(arr)): 
     for i in range(0,len(arr)-1):
          if arr[i]>arr[i+1]:
             arr[i],arr[i+1]=arr[i+1],arr[i]
for  i in range(len(arr)):
    print(arr[i])"""
#Inserting sort:
arr=[2,45,36,38,39,53,32,64,100]

for i in range(0,len(arr)):
    cur = arr[i]
    for j in range(i-1,-1,-1):
        if arr[j]>cur:
            arr[j+1]=arr[j]
        else:
            arr[j+1]=cur
            break    
for i in range(len(arr)):
    print(arr[i])
