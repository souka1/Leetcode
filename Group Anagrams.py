class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map < String, List> map=new HashMap<String,List>();
        for(int i=0;i<strs.length;i++){
            char[] c=strs[i].toCharArray();
            Arrays.sort(c);
            String s = String.valueOf(c);
            if(!map.containsKey(s)){
                map.put(s,new ArrayList());
            }
            map.get(s).add(strs[i]);
        }
        return new ArrayList(map.values());
    }
}