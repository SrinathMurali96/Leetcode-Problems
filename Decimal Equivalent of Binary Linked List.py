#Decimal Equivalent of Binary Linked List


#0->0->0->1->1->0->0->1->0

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL():
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        num_list = []
        while temp:
            num_list.append(temp.data)
            temp = temp.next
            
        return num_list
     
    def findVal(self,num_list):
        j = 0
        decimal = 0
       #some random value  num_list = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
        for i in range(len(num_list)-1,-1,-1):
                decimal = decimal + num_list[i] * (2**j)
                j = j+1
        return decimal
l = LL()
l.head = Node(0)
second = Node(0)
third = Node(0)
four = Node(1)
five = Node(1)
six = Node(0)
seven = Node(0)
eight = Node(1)
nine = Node(0)
l.head.next = second
second.next = third
third.next = four
four.next = five
five.next = six
six.next =seven
seven.next = eight
eight.next = nine
num_list = l.printlist()
decimal = l.findVal(num_list)
print("decimal equivalent is ",decimal)