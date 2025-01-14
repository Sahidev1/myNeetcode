
import Medium_problems.min_stack.java.MinStack;

class Main {
    public static void main(String[] args) throws Exception {

        MinStack minStack = new MinStack();
        minStack.push(1);
        minStack.push(2);
        minStack.push(0);
        minStack.getMin(); // return 0
        minStack.pop();
        minStack.top(); // return 2
        minStack.getMin(); // return 1
    }
}