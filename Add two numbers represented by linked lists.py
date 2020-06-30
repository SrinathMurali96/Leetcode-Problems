#Add two numbers represented by linked lists

Best Solution:
    
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        sum_val = 0
        dummy = None
        while l1 or l2:
            m,n = 0,0
            if l1:
                m = l1.val
                l1 = l1.next
            if l2:
                n = l2.val
                l2 = l2.next 
            sum_val = m + n + carry
            carry = 1 if sum_val>=10 else 0
            node_val = sum_val % 10
            if dummy is None:
                dummy = ListNode(node_val)
                temp = dummy
            else:
                temp.next = ListNode(node_val)
                temp = temp.next
        if carry:
            temp.next = ListNode(carry)
            temp.next.next = None
        return dummy
            
SECOND SOLUTION :
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class LL():
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        
        while temp:
            print(temp.data)
            temp = temp.next
      
    def sum_lists(self,l1,l2):
        temp1 = l1
        temp2 = l2
        st1 =''
        carry = 0
        while temp1.next:  
                temp1 = temp1.next
        while temp2.next:  
                temp2 = temp2.next
                
        prev_1 = temp1
        prev_2 = temp2
        while prev_1 and prev_2:
            val = prev_1.data + prev_2.data + carry
            if val>=10:
                st1 =  str(val%10) + st1 
                carry = val // 10
            else:
                st1 = str(val) + st1  
                carry = 0
            
            prev_1 = prev_1.prev
            prev_2 = prev_2.prev
            
        if prev_1:
              while prev_1:  
                st1 =  str(prev_1.data +carry) + st1 
                prev_1 = prev_1.prev
         
        if prev_2:
              while prev_2:  
                st1 =  str(prev_2.data +carry) +st1 
                prev_2 = prev_2.prev
        return st1
        
        
#        
l1 = LL()
l1.head = Node(1)
second = Node(5)
third = Node(5)
l1.head.next = second
l1.head.prev = None
second.prev = l1.head
second.next = third
third.prev = second

l2 = LL()
l2.head = Node(4)
second = Node(5)

l2.head.next = second
l2.head.prev = None
second.prev = l2.head



#l1.printlist()
#l2.printlist()

final_sum = l1.sum_lists(l1.head,l2.head)
print("Final_sum is ",final_sum)




