package Medium_problems.implement_trie.java;


public class Trie {
    final int ALPHABET_SIZE = 26;
    final char START_INDEX = 'a';
    Trie[] children;
    boolean lastWord;

    public Trie() {
        this.children = new Trie[ALPHABET_SIZE];
        this.lastWord = false;
    }

    private int trieIndex(char c){
        return c - START_INDEX;
    }

    public void insert(String word) {
        Trie root = this;
        int trieI;
        
        for(int i = 0; i < word.length(); i++){
            trieI = trieIndex(word.charAt(i));
            if (root.children[trieI] == null){
                root.children[trieI] = new Trie();
            }

            root = root.children[trieI];
        }

        root.lastWord = true;
    }


    public boolean search(String word) {
        Trie root = this;
        int i = 0;
        int charIndex;

        while(i < word.length()){
            charIndex = this.trieIndex(word.charAt(i++));
            if(root.children[charIndex] == null) return false;
            //System.out.print("char: " + word.charAt(i - 1));
            //System.out.println((root.children[charIndex] != null));
            root = root.children[charIndex];
        }
        return root.lastWord;
    }

    public boolean startsWith(String prefix) {
        Trie root = this;
        int i = 0;
        int charIndex;

        while(i < prefix.length()){
            charIndex = trieIndex(prefix.charAt(i++));
            if(root.children[charIndex] == null) return false;
            root = root.children[charIndex];
        }
        return true;
    }
}




/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */