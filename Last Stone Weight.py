class Solution {
    public int lastStoneWeight(int[] stones) {
        int i=stones.length-1,j= stones.length-2;
        
        
        while(i>0 && j>=0){
             Arrays.sort(stones);
             int x=stones[i], y=stones[j];
             if(x==y){
                 i-=2;
                 j-=2;
             }
            else{
                stones[j]=stones[i]-stones[j];
                i--;
                j--;
            }
        }
        return i<0 ? 0 : stones[i];
        
    }
}