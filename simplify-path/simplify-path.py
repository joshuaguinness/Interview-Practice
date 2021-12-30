class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # Add all elements to a queue
        queue = deque([])
        
        # Split at '/'
        path_list = path.split('/')
        
        # Iterate through the list and do actions
        for i, v in enumerate(path_list):
            # Do nothing
            if v == '' or v == '.':
                continue
            # Pop from queue as long as stack exists
            elif v == '..':
                if len(queue) >= 1:
                    queue.pop()
            # Add element to queue
            else:
                queue.append(v)
        
        # Return a '/' + queue with '/' in between each element
        return '/' + '/'.join(queue)