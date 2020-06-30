class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL():
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        
        while temp:
            print(temp.data)
            temp = temp.next
        
    def reverselist(self):
        reversed_node = head
        list_to_reverse = reversed_node.next
        reversed_node.next = None
    
        while list_to_reverse:
            temp = reversed_node
            reversed_node = list_to_reverse
            list_to_reverse = list_to_reverse.next
            reversed_node.next = temp
        head = reversed_node
        return head    
    
                
l = LL()
l.head = Node(1)
second = Node(2)
third = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

l.head.next = second
second.next = third
third.next = four
four.next = five
five.next = six

l.printlist()
l.reverselist()
print("After reverse ***")
l.printlist()
