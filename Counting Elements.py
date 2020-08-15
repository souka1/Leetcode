class Solution {
    public int countElements(int[] arr) {
        int count=0;
        Set<Integer> set=new HashSet<>();
        for(int a : arr){
            set.add(a);
        }
        for(int i=0;i<arr.length;i++){
            if(set.contains(arr[i]+1)){
                count++;    
            }
        }
        return count;
        
    }
}