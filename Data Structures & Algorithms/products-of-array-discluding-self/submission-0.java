class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int prodWithout = 1;
        int[] arr = new int[nums.length];
        int count =0;
        for(int i : nums) {
            if(i == 0) {
                count++;
                if(count > 1 ) {
                    prodWithout = 0;
                }
                product = 0;
            } else {
                product = product * i;
                prodWithout = prodWithout * i;
            }
        }
        for(int i = 0; i< nums.length;i++) {
            if(nums[i] == 0) {
                arr[i] = prodWithout;
            } else {
                arr[i] = product / nums[i]; 
            }
            
        }
        return arr;
    }
}  
