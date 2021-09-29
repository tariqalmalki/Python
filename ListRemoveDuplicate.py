##myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] 
###
### put your code here
###
##
##newlist = myList[:]
##
##for i in myList:
##    if i in newlist:
##        del myList[i]
##        
##print("The list with unique elements only:")
##print(myList)



myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
for number in myList:  # Browse all numbers from the source list.
	if number not in newList:  # If the number doesn't appear within the new list...
		newList.append(number)  # ...append it here.
myList = newList[:]  # Make a copy of newlist.
print("The list with unique elements only:")
print(myList)
