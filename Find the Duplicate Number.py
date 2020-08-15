class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
      
        
        for(int i=0; i<nums.length-1;i++){
            int result=0;
            
            result=nums[i]^ nums[i+1];
            if(result==0 ){
                return nums[i];
            }
        }
        return -1;
    }
    
}