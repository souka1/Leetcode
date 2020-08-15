class Solution {
    public String stringShift(String s, int[][] shift) {
       
        char[] temp = s.toCharArray();
         char[] sh = new char[temp.length];
        int count=0;
        for(int i=0; i<shift.length; i++){
            count+=(shift[i][0]==0 ? -1 : 1) * shift[i][1];
        }
        if (count>0){
            for (int i=0; i<temp.length; i++){
                sh[(i+count)%temp.length]=temp[i];
            }
            return String.valueOf(sh);
        }
        else if(count<0 ){
            for (int i=0; i<temp.length; i++){
                sh[(i+(count%temp.length)+temp.length)%temp.length]=temp[i];
            }
            return String.valueOf(sh);
        }
        else{
            return s;
        }
        
    }
}