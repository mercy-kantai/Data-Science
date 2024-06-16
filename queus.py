


#Method one
# # FIFO Principle
import queue
queu_1 = queue.Queue()
queu_1.put(10)
queu_1.put("Mercy")
queu_1.put(20.3)
queu_1.put("Banana")
#Removing elements from a queue
print(queu_1.get())
print(queu_1.get())
print(type(queu_1))




# #LIFO Principle
import queue
queue_2 = queue.LifoQueue()
queue_2.put("Apple")
queue_2.put("Mango")
queue_2.put("Pineapple")
queue_2.put("Banana")
print(queue_2.get())
print(queue_2.get())
print(queue_2.get())
print(type(queue_2))


# #Priority Queue Method
import queue
queue_3 = queue.PriorityQueue()
queue_3.put((4,"Ferrari"))
queue_3.put((5,"Maserati"))
queue_3.put((2,"Macedes"))
queue_3.put((1, "BMW"))
queue_3.put((3, "Subaru"))
print(queue_3.get())
print(queue_3.get())
print(type(queue_3))







