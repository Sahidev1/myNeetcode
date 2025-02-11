
import Medium_problems.implement_trie.java.Trie;

class Main {
    public static void main(String[] args) throws Exception {

        Trie prefixTree = new Trie();
        prefixTree.insert("dog");
        System.out.println(prefixTree.search("dog")); // return true
        System.out.println(prefixTree.search("do")); // return false
        System.out.println(prefixTree.startsWith("do")); // return true
        prefixTree.insert("do");
        System.out.println(prefixTree.search("do")); // return true
    }
}