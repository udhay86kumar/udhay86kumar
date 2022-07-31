
Array = [63, 75, 13, 2, 441] # loop through each and every element in the array
for element1 in range(len(Array)):
# To determine the least element in the remaining list
   minimum_idx = element1
for element2 in range(element1+1, len(Array)):
    if Array[minimum_idx] > Array[element2]:
          min_idx = element2
# swap the determined least element with the  previous element in the list
Array[element1], Array[minimum_idx] = Array[minimum_idx], Array[element1] # main code
print ("Array after getting sorted by selection sort")
for i in range(len(Array)):
      print("%d" %Array[i])