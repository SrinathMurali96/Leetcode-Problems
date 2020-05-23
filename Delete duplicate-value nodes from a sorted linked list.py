#Delete duplicate-value nodes from a sorted linked list

#Hackerrank

def removeDuplicates(head):
        s = set()
        temp = head
        while head:
            if head.data in s:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                s.add(head.data)
        return temp