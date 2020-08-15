class Solution {
    public int maxProfit(int[] prices) {
        
        int max=0;
        for(int i=0;i<prices.length-1;i++){
            int price=prices[i+1]-prices[i];
            if(price>0){
                max+=price;
            }
        }
        return max;
        
    }
}