class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        # Main idea: 
        # If at the end of one cycle, the robot is
        # either at (0, 0), or not facing north
        # then it is bounded by a circle
        
        # This code could have been a lot less,
        # and run faster if I used some nifty modulus
        # operations. See solution for more details
        
        def nextDirection(cur, ins):
            if cur == "north":
                if ins == "L": return "east"
                else: return "west"
            if cur == "east":
                if ins == "L": return "south"
                else: return "north"
            if cur == "south":
                if ins == "L": return "west"
                else: return "east"
            if cur == "west":
                if ins == "L": return "north"
                else: return "south"
        
        curr_direction = "north"
        curr_pos = [0, 0]
        
        for i,v in enumerate(instructions):

            if v == "L" or v == "R":
                curr_direction = nextDirection(curr_direction, v)
                continue
            
            if curr_direction == "north":
                curr_pos[1] += 1
            if curr_direction == "east":
                curr_pos[0] -= 1
            if curr_direction == "south":
                curr_pos[1] -= 1
            if curr_direction =="west":
                curr_pos[0] += 1 
            
        if curr_pos == [0, 0]:
            return True
        
        if curr_direction != "north":
            return True
        
        return False