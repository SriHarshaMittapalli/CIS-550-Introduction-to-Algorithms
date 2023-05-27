import math
class MaxHeap:

    def __init__(self): self.heap_list = []
 
    def parent(self, item_index): return (item_index - 1) // 2 # Formula for finding parent index is : ⌊(i-1)/2⌋

    def leftChild(self, item_index): return 2 * item_index + 1 # Formula for finding left child is : 2i+1

    def rightChild(self, item_index): return 2 * item_index + 2 # Formula for finding right child is: 2i+2

    def maxHeapify(self, item_index, heap_size):
        left_child,right_child = self.leftChild(item_index),self.rightChild(item_index)
        largest_index = item_index
        if left_child < heap_size and self.heap_list[left_child][1] > self.heap_list[largest_index][1]: largest_index = left_child
        if right_child < heap_size and self.heap_list[right_child][1] > self.heap_list[largest_index][1]: largest_index = right_child
        if largest_index != item_index:
            self.heap_list[item_index], self.heap_list[largest_index] = self.heap_list[largest_index], self.heap_list[item_index] # Swap the elements
            self.maxHeapify(largest_index,heap_size)

    def insert(self, name, rating): # Insert element and heapify
        self.heap_list.append((name, rating))
        item_index = len(self.heap_list) - 1
        while item_index > 0:
            parent_index = self.parent(item_index)
            parent = self.heap_list[parent_index]
            if rating <= parent[1]: break
            self.heap_list[item_index], self.heap_list[parent_index] = self.heap_list[parent_index], self.heap_list[item_index] # Swap the elements
            item_index = parent_index

    # Print nodes from top to down, left to right
    def Print(self,function_name,heap_list): print(f"\n{function_name.__name__}\n\n{heap_list}\n")

    # Construct a max heap from array
    def maxHeap(self):
        heap_size = len(self.heap_list)
        child_node_start = heap_size // 2 # Child node starts at n // 2
        for item_index in reversed(range(child_node_start)): self.maxHeapify(item_index,heap_size)

    def remove(self, item_index = 0): # Max Heap deletion
        if not self.heap_list: return None
        root, self.heap_list[item_index] = self.heap_list[item_index], self.heap_list[-1] # Swap the elements
        self.heap_list.pop()
        self.maxHeapify(item_index,len(self.heap_list)) # Heapify after removing the root node
        return root

def sort_movies_batch(names, ratings):
    heap = MaxHeap()
    for _, (name, rating) in enumerate(zip(names, ratings)): heap.heap_list.append((name, rating))
    heap.maxHeap()
    names_size = len(names)
    sorted_names = [heap.remove()[0] for _ in range(names_size)]
    """ Uncomment the code below to print the sorted list for incremental version """
    # heap.Print(sort_movies_batch, sorted_names)
    return sorted_names

def sort_movies_incre(names, ratings):
    heap = MaxHeap()
    for _, (name, rating) in enumerate(zip(names, ratings)): heap.insert(name, rating)
    names_size = len(names)
    sorted_names = [heap.remove()[0] for _ in range(names_size)]
    """ Uncomment the code below to print the sorted list for incremental version """
    # heap.Print(sort_movies_incre, sorted_names)
    return sorted_names