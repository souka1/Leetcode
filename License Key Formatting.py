class Solution {
    public String licenseKeyFormatting(String S, int K) {
        
        S=S.toUpperCase();
        S=S.replace("-","");
        
        StringBuilder s=new StringBuilder(S);
        
        for(int i=s.length()-K; i>0; i=i-K){
            s.insert(i,"-");
        }
        return s.toString();
    }
}