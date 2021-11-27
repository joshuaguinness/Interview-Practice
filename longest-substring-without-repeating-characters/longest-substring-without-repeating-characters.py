class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        final_count = 0
        new_count = 0
        my_dict = {}
        sliding_index = 0
        i = 0

        while i < len(s):

            # Character exists in the dictionary, aka, end of unique substring
            if (s[i] in my_dict.keys()):

                # Reset dictionary to blank
                my_dict = {} 

                # Move the sliding window by updating the current index and the start index of                      the window
                i = sliding_index + 1 
                sliding_index = i

                # Update final count with the higher of current and new, reset the counter
                final_count = max(new_count, final_count)
                new_count = 0

            else:

                # Add character to dictionary to keep track of, add 1 to count and iterator
                my_dict[s[i]] = 1
                new_count += 1
                i += 1

        # Return the max
        return max(final_count, new_count)