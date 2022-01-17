

int missingNumber(int* nums, int numsSize){
    
    int missing_value = numsSize;

    // XOR integer n with ever index and value
    // to find the missing number. See solution #3
    // for more details.
    for (int i = 0; i < numsSize; i++){
        
        // XOR = True if exactly one, but not both conditions are true
        missing_value ^= i ^ nums[i];

    }
    return missing_value;
    
}