package Medium_problems.min_stack.java;

public class MinStack{
    class Node{
        int val;
        Node next;

        public Node(int val, Node next){
            this.val = val;
            this.next = next;
        }
    }    

    class Stack{
        Node head;
        int stackSize;

        public Stack(){
            this.stackSize = 0;
        }
        public void push(int val){
            this.head = new Node(val, this.head);
            this.stackSize++;
        }
        public void pop(){
            if(this.head != null) this.head = this.head.next;
            this.stackSize--;
        }
        public int top(){
            return this.head.val;
        }
        public int getSize(){
            return this.stackSize;
        }
    }

    Stack main;
    Stack history;

    public MinStack(){
        this.main = new Stack();
        this.history = new Stack();
    }

    public void push(int val){
        this.main.push(val);
        if(this.history.getSize() <= 0 || this.history.top() > val) this.history.push(val);
        else this.history.push(this.history.top());
    }

    public void pop(){
        this.main.pop();
        this.history.pop();
    }

    public int top(){
        return this.main.top();
    }

    public int getMin(){
        return this.history.top();
    }


}