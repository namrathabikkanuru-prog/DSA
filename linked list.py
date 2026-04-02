
#Linked lists :
# node class
class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

# linked list class
class LinkedList:
    def __init__(self):
        self.head = None     # initially the head will be none

    def append(self,value): 
        new_node = ListNode(value) 
        if not self.head:
            self.head = new_node 
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node    
                
    def find_middle(self):
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
sample_list = LinkedList()
sample_list.append(1)
sample_list.append(2)
sample_list.append(3)
sample_list.append(4)
sample_list.append(5)
middle = sample_list.find_middle()
print(f"middle node is {middle.value}")  