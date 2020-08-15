class Solution {
    public void helper(int i,char[]x){
        if (i>=x.length/2){
            return;
        }
        helper(i+1,x);
        char a=x[i];
        x[i]=x[x.length-i-1];
        x[x.length-i-1]=a;
           
    }
    public void reverseString(char[] s) {
        
        helper(0,s);
        
     
        
    }
}