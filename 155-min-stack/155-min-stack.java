class MinStack {

  Stack <Integer> stack = new Stack();
  Stack <Integer> min_val = new Stack();
    public void push(int val) {
        stack.push(val);
        if(min_val.isEmpty() || val<=min_val.peek()){
            min_val.push(val);
        }
    }
    
    public void pop() {
        if(stack.peek().equals( min_val.peek())){
            min_val.pop();
        }
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min_val.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */