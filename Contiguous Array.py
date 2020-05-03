#Contiguous Array



def findMaxLength(nums) :
           stack = []
           count = 0
           for i in nums:
               if i ==0:
                  stack.append(0)      
               else:
                   if len(stack) != 0:
                       count = count + 2
                       stack.pop()
           return count
                       
        
        
count = findMaxLength([0,0,0,1,1,1,0])
print("The count is ",count )




#[0,1,1,0,1,1,1,0]

