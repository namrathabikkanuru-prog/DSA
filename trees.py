

#trees :

from collections import deque
# tree node
class tree :
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# build tree from list
def binary_tree(arr): #[1,2,3,4]
      if not arr:
        return None
      
      root = tree(arr[0])
      queue = [root]
      i = 1

      while queue and i < len(arr):
            node = queue.pop(0)
            if i< len(arr) and arr[i] is not None:                                   #1
                node.left = tree(arr[i])                                            
                queue.append(node.left)                                          #2     3
            i += 1                                                              
            if i< len(arr) and arr[i] is not None:                             #4
                node.right = tree(arr[i])
                queue.append(node.right)
            i += 1
                               
      return root

# BFS to find maximum depth

def max_depth(root):
    if  not root:
        return 0
    
    queue = deque([root])
    depth = 0

    while queue:
        for i in range (len(queue)):
            node = queue.popleft()
            if  node.left:
                queue.append(node.left)
            if node.right:
                queue. append(node.right)
        depth += 1            
    return depth
arr = [1,2,3,4]   
root = binary_tree (arr)   
print(max_depth(root))