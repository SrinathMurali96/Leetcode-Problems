Copy List with Random Pointer
Basically a doubly linked list. We need create a new LL with same next pointer and previous pointer. (Deep copy)
We do it using recursion

def copyLL(self,head):
    self.visited = {}
    def helper(head):
        if head is None:
            return None
        if head in self.visited:
              return self.visited[head]
        node = Node(head.val,None,None)
        self.visited[head] = node
        node.next = helper(node.next)
        node.random = helper(node.random)
        return node
    return helper(head)

            
