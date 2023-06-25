class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val
    
    def set_data(self, val):
        self.val = val
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
        

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
    
    def find(self, val):
        item = self.head

        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None
    
    def deleteAt(self, idx):

        if idx > self.count - 1:
            return
        
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
              
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

#merge sort
def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_array = dataset[:mid]
        right_array = dataset[mid:]

        mergesort(left_array)
        mergesort(right_array)

        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                dataset[k] = left_array[i]
                i += 1
            else:
                dataset[k] = right_array[j]
                j += 1
            k += 1
        
        while i < len(left_array):
            dataset[k] = left_array[i]
            k += 1
            i += 1
        
        while j < len(right_array):
            dataset[k] = left_array[j]
            k += 1
            j += 1

num_of = int(input("How many numbers did you want to insert: "))
dataset = [int(input("Enter number: ")) for i in range(num_of)]
mergesort(dataset)
print(dataset)


dict