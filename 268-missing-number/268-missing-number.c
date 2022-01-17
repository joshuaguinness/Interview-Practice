

int missingNumber(int* nums, int numsSize){
    
//     int missing_value = numsSize;

//     // XOR integer n with ever index and value
//     // to find the missing number. See solution #3
//     // for more details.
//     for (int i = 0; i < numsSize; i++){
        
//         // XOR = True if exactly one, but not both conditions are true
//         missing_value ^= i ^ nums[i];

//     }
//     return missing_value;
    
    
    // Gauss Approach
    
    // Gets the sum of numbers 1 -> n
    int expectedSum = numsSize * (numsSize + 1) / 2;
    int actualSum = 0;
    
    // Calculate the actual sum of the numbers in the array
    for (int i = 0; i < numsSize; i++){
        actualSum += nums[i];
    }
    
    // Return the difference which is number missing
    return expectedSum - actualSum;
    
}