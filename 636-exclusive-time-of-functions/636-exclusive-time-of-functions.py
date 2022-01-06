class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # Stack for functions
        stack = []
        
        # Result that will contain the time of all functions
        function_time = [0]*n
        
        for log in logs:

            # Split the log
            process_id, action, time = log.split(':')

            # Push to stack
            if action == 'start':
                # Append the process_id and time to the stack
                stack.append((int(process_id), int(time)))
                
            # Pop from stack
            else:
                # Get the info from the stack
                prev_id, prev_time = stack.pop()
                # Calculate the time the function spent executing
                time_spent = (int(time) - prev_time + 1)
                # Add that time to the function_time array
                function_time[int(process_id)] += time_spent
                
                # If still items left on stack, subtract the time_spent
                # from the process still on the stack since two functions cannot
                # execute at the same time
                if stack:
                    next_id, next_time = stack[-1]
                    function_time[int(next_id)] -= time_spent
                    
         
        return function_time