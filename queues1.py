from queue import Queue
my_ordes = Queue()
# Add new orders
my_ordes.put("White coffee")
my_ordes.put("Black coffee")
my_ordes.put("Cuppucino")
my_ordes.put("Lemon tea")
my_ordes.put("caramel")

#serve the next order
print(my_ordes.get())
print(my_ordes.get())
print(my_ordes.get())

#Display all pending orders
print(my_ordes.queue)

#Find how many orders are ahead of a given order

