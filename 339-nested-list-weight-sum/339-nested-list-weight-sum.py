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
        queue = deque(nestedList)
        level = 1
        
        # Add the level 1 lists/integers to the queue
        length = len(nestedList)
        # for i in range(length):
        #     queue.append(nestedList[i])

        # BFS w/ Queue
        while queue:
            next_length = 0
            for i in range(length):
                new_list = queue.popleft()
                if new_list.isInteger():
                    result += level * new_list.getInteger()
                else:
                    curr_length = len(new_list.getList())
                    next_length += curr_length
                    for j in range(curr_length):
                        queue.append(new_list.getList()[j])
            level += 1
            length = next_length

            
        return result