class Solution {
    
     public String result(String S){
         
        Stack<Character> s=new Stack();
        
        for(char i : S.toCharArray()){
            if(i!='#'){
                s.push(i);
            }
            else if(!s.empty() && i=='#'){
                s.pop();
            }
        }
         return String.valueOf(s);
         
     }
    
    public boolean backspaceCompare(String S, String T) {
        
        return result(S).equals(result(T));
        
    }
}