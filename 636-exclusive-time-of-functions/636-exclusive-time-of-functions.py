class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # As iterate through the list, add to stack, keep a dictionary of 
        
        stack = []
        function_time = [0]*n
        
        for log in logs:

            process_id, action, time = log.split(':')

            # Push to stack
            if action == 'start':
                stack.append((int(process_id), int(time)))
                
            # Pop from stack
            else:
                prev_id, prev_time = stack.pop()
                time_spent = (int(time) - prev_time + 1)
                function_time[int(process_id)] += time_spent
                
                if stack:
                    next_id, next_time = stack[-1]
                    function_time[int(next_id)] -= time_spent
                    
         
        return function_time                    
    
            
        
        # Decrement time for next process in the stack
                # if len(stack) != 0:
                #     nextProcessId, timeSpentByNextProcess = stack[-1] #
                #     result[int(nextProcessId)] -= timeSpent