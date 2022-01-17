

int singleNumber(int* nums, int numsSize){

    // XOR of zero and some other bit will returrn that bit
    // XOR of two identical bits will return 0
    // Therefore, XOR all bits together to find unnique number
    
    int compare = 0;
    for (int i = 0; i < numsSize; i++){
        compare ^= nums[i];
    }
    
    return compare;
}