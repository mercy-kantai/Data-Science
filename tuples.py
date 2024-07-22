#Accessing items in a tuple
tuple1 = ("Banana","Orange","Mango","Avocado",1,20,9)
print(tuple1[1])
print(tuple1[5])

#adding an item to a tuple
tuple2 = (10,20,30,40)
print(tuple2)
#convert a tuple into list
my_list = list(tuple2)

#Remove items
my_list.pop()
my_list.pop()
#convert back to a list to a tuple
my_list = tuple(my_list)
print(my_list)


# #Removing an element from a tuple

# #Method 1
# tuple3 = ("Bag","Book",False,True,4)
# print(tuple3)
# tuple3 = tuple3[0]
# print(tuple3)

# #Method2
# tuple4 = ("pen",3,"Mercy")
# # convert a tuple in a list
# list_2 = list(tuple4)
# # remove an item
# list_2.remove(3)
# #convert back to a tuple
# list_2 = tuple(list_2)
# print(list_2)

  