class Solution {
    public int maxArea(int[] height) {
        int max=0,s=0,e=height.length-1;
        while(s<e){
            int area=(e-s)*(Math.min(height[s],height[e]));
            max=area > max ? area :max;
            if(height[s]>height[e]){
                e--;
            }
            else{
                s++;
            }
        }
        return max;
        
    }
}