# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        result = 0
        # Add all the level 1 lists/integers to the queue
        # Faster to do it like this instead of with a loop
        # since it just ends up being the exact same in the end
        queue = deque(nestedList)
        level = 1
        # Number of items at the first level
        length = len(nestedList)
        
        # Loop method of adding lists/integers to the queue
        # for i in range(length):
        #     queue.append(nestedList[i])

        # BFS w/ Queue
        while queue:
            
            # The numbers of items in the next level
            next_length = 0
            
            # Iterate through the number of items at the current level
            for i in range(length):
                
                # Pop the element from the queue
                element = queue.popleft()
                
                # If its an integer, add the level * integer to the result
                if element.isInteger():
                    result += level * element.getInteger()
                
                # Its a list
                else:
                    
                    # Get the list and its length
                    new_list = element.getList()
                    curr_length = len(new_list)
                    
                    # Add current length to the next_length
                    # which is the number of items in the next level
                    next_length += curr_length
                    
                    # Add each item in the list to the queue
                    for j in range(curr_length):
                        queue.append(new_list[j])
            
            # Increase level by 1 and reassign the number of items
            # to reflect the new number of items in the next level
            level += 1
            length = next_length

        return result