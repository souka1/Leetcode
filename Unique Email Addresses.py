class Solution {
    public int numUniqueEmails(String[] emails) {
        
        Set<String> s = new HashSet();
        for(String email: emails){
            String first=email.substring(0,email.indexOf('@'));
            String second=email.substring(email.indexOf('@'));
           if(first.contains("+")){
               first=first.substring(0,email.indexOf('+'));
           } 
            
            first=first.replaceAll("\\.","");
            
        
            s.add(first+second);
            }
            
        return s.size();
        
    }
}