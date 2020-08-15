class MinStack {
    
    List<pair> l;
    int min;
    
    class pair{
        int y;
        int min;
        public pair(int y,int min){
            this.y=y;
            this.min=min;
        }
       
    } 

    /** initialize your data structure here. */
    public MinStack() {
        
        this.l=new ArrayList<>();
        this.min=Integer.MAX_VALUE;
        
    }
    
    public void push(int x) {
        
        if(x<this.min){
            this.min=x;
        }
        l.add(new pair(x,min));
        
    }
    
    public void pop() {
        pair p=l.remove(l.size()-1);
        if(p.min==this.min){
            this.min=l.size()>0 ? l.get(l.size()-1).min : Integer.MAX_VALUE;
        }
        
    }
    
    public int top() {
        return l.get(l.size()-1).y;
        
    }
    
    public int getMin() {
        return this.min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */