class Solution:
    def simplifyPath(self, path: str) -> str:
        
        queue = deque([])
        queue.append('/')
        
        path_list = path.split('/')
        recent = ''
        print(path_list)
        
        for i, v in enumerate(path_list):
            if v == '':
                continue
                # if recent != '/':
                #     queue.append('/')
            elif v == '..':
                if len(queue) > 1:
                    queue.pop()
                    queue.pop()
            elif v == '.':
                continue
            else:
                queue.append(v)
                queue.append('/')
                
            if queue:
                recent = queue[-1]
            print(queue)
                
        if len(queue) > 1 and queue[-1] == '/':
            queue.pop()
        
        return ''.join(queue)