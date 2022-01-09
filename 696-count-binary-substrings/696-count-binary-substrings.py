class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        # Iterate through s, and keep track in 
        # a list, all the groups, and number of elements
        # in the group. A new group is added everytime
        # the number changes.
        # Then iterate through the groups and add
        # the minimum of groups[i], groups[i-1] since that
        # is the length of the substring. See solution for
        # more details
        
        # Using groups, O(n) space solution
#         result = 0
#         groups = [1]
        
#         for i in range(1, len(s)):
#             if s[i] != s[i-1]:
#                 groups.append(1)
#             else:
#                 groups[-1] += 1
        
#         for i in range(1, len(groups)):
#             result += min(groups[i], groups[i-1])
            
#         return result

        # Calculating differences on fly, O(1) space solution
        result = 0
        prev = 0
        curr = 1
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                result += min(curr, prev)
                prev = curr
                curr = 1
            else:
                curr += 1
            
        return result + min(prev, curr)
    