class MinHeap:
    def __init__(self):
        # Initialize an empty list that will be used to store the elements of the heap
        self.heap = []   


        # Calculate the index of the parent node for a given child node. 
    def _parent(self, index):
        return (index - 1) // 2


    def _heapify_up(self, index):
        # Calling the _parent method to get the parent index
        parent = self._parent(index)
        #  CHeck if the current node is less than it's parent value
        if index > 0 and self.heap[index] < self.heap[parent]:
        # Swap if the current element is smaller than its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            # Recursively heapify the parent node
            self._heapify_up(parent)

    def insert(self, key):
        # Add the new element to the end of the heap,, key is the new value added
        self.heap.append(key)
       # Call the heapify method to restore the heap property by finding the last element added in the heap 
        self._heapify_up(len(self.heap) - 1)
#    Convert the heap into the string 
    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(20)
    min_heap.insert(5)
    min_heap.insert(6)

    print("Heap after insertions:", min_heap)  # Output: Heap after insertions: [5, 6, 10, 20]









class MaxHeap:
    def __init__(self):
        # Initialize an empty list that will be used to store the elements of the heap
        self.heap = []

    def _parent(self, index):
        # Calculate the index of the parent node for a given child node
        return (index - 1) // 2

    def _heapify_up(self, index):
        # Calling the _parent method to get the parent index
        parent = self._parent(index)
        # Check if the current node is greater than its parent value
        if index > 0 and self.heap[index] > self.heap[parent]:
            # Swap if the current element is greater than its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            # Recursively heapify the parent node
            self._heapify_up(parent)

    def insert(self, key):
        # Add the new element to the end of the heap; key is the new value added
        self.heap.append(key)
        # Call the heapify method to restore the heap property by finding the last element added in the heap
        self._heapify_up(len(self.heap) - 1)

    def __str__(self):
        # Convert the heap into a string
        return str(self.heap)


if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    max_heap.insert(6)
# Call the heapify method to restore the heap property by finding the last element added in the heap
    print("Heap after insertions:", max_heap)
