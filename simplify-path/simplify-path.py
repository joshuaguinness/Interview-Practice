class Solution:
    def simplifyPath(self, path: str) -> str:
        
        queue = deque([])
        queue.append('/')
        
        path_list = path.split('/')
        recent = ''
        
        for i, v in enumerate(path_list):
            if v == '':
                continue
            elif v == '.':
                continue
            elif v == '..':
                if len(queue) > 1:
                    queue.pop()
                    queue.pop()
            else:
                queue.append(v)
                queue.append('/')
                
        if len(queue) > 1 and queue[-1] == '/':
            queue.pop()
        
        return ''.join(queue)