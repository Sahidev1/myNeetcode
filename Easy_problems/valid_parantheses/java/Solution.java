package valid_parantheses.java;

public class Solution {

    class Node<T> {
        T data; 
        Node<T> next;

        public Node(T data, Node<T> next){
            this.data = data;
            this.next = next;
        }

        public Node(T data){
            this.data = data;
        }
    }

    class Stack<T> {
        Node<T> top;
        int size;

        public void push(T val){
            Node<T> freshNode = new Node<>(val);
            freshNode.next = top;
            top = freshNode;
            this.size++;
        }

        public T pop(){
            if (top == null) return null;
            T topVal = top.data;
            top = top.next;
            //old top is not referenced, GC will take care of it
            this.size--;
            return topVal;
        }

        public T peek(){
            return top == null?null:top.data;
        }
    }

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] closers = {')',']','}'};
        char[] openers  = {'(','[','{'};

        boolean matchFound = false;
        for (char c : s.toCharArray()) {
            if (c == '(' || c== '[' || c == '{') {
                stack.push(c);
                continue;
            }
    

            for(int i = 0; i < closers.length; i++){
                if(matchCheck(stack.peek(), c, openers[i], closers[i])) {
                    matchFound = true;
                    stack.pop();
                    break;
                }
            }
            if (!matchFound) return false;
            matchFound = false;
        }

        return stack.size == 0;
    }

    private boolean matchCheck(Character opener, char closer, char expOpener, char expCloser){
            if (closer == expCloser){
                if(opener == null) return false;
                if(opener != expOpener) return false;
                else return true;
            }
        return false;
    }
}