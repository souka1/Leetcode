class Solution {
    
    public void twosum(int[] num,int i,List<List<Integer>> res){
        int low=i+1,high=num.length-1;
        while(low<high){
            if(num[low]+num[high]> -num[i] || high<num.length-1 && num[high]==num[high+1]){
                high--;
            }
            else if(num[low]+num[high]< -num[i] || low>i+1 && num[low]==num[low-1]){
                low++;
            }
            else{
                 res.add(Arrays.asList(num[i],num[low],num[high]));
                high--;
                low++;
            }
        }
    }
    public List<List<Integer>> threeSum(int[] nums) {
        
        Arrays.sort(nums);
        List<List<Integer>> res=new ArrayList<>();
        for(int i=0;i<nums.length-1 && nums[i] <=0;i++){
            
            if(i==0 || nums[i]!=nums[i-1]){
               
              
                    twosum(nums,i,res);
                }
                
                
            }
        
        return res;
    }
} 