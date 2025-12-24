
class WordDictionary {
    private static final int LETTERCOUNT = 26;

    private class Trie {
        private Trie[] tries;
        boolean terminator;

        private int trieIndex(char c) {
            return (int) (c - 'a');
        }

        public Trie() {
            this.tries = new Trie[LETTERCOUNT];
            this.terminator = false;
        }

        //O(N)
        private void addWordProc(char[] w, int index) {
            if (index >= w.length) {
                terminator = true;
                return;
            }
            int cindex = trieIndex(w[index]);
            if (tries[cindex] == null)
                tries[cindex] = new Trie();
            tries[cindex].addWordProc(w, index + 1);
        }

        //worst case: O(K + 26M)
        private boolean matchProc(char[] w, int index){
            if (index == w.length) return this.terminator;
            if (index > w.length) return false;
            if(w[index] == '.'){
                boolean found = false;
                int i = 0;
                //worse case: O(26M)
                while(i < LETTERCOUNT && !found){
                    found = tries[i] == null?false:tries[i].matchProc(w, index+1);
                    i++;
                }
                return found;
            }

            int ci = trieIndex(w[index]);
            return ( tries[ci] != null)?tries[ci].matchProc(w, index + 1):false;
        }

        public void addWord(char[] word) {
            addWordProc(word, 0);
        }

        public boolean match(char[] w) {
            return matchProc(w, 0);
        }

    }

    private Trie rootTrie;

    public WordDictionary() {
        this.rootTrie = new Trie();
    }

    public void addWord(String word) {
        this.rootTrie.addWord(word.toCharArray());
    }

    public boolean search(String word) {
        return this.rootTrie.match(word.toCharArray());
    }

    
}


class Prog{
    public static void main(String[] args) {
        WordDictionary dict = new WordDictionary();
        String[] words = {"bye","cool","tank","holy","cow"};
        for (String word : words) {
            dict.addWord(word);
        }
        String[] matches = {"bye", "c.ol", ".ol.y","cow"};
        for (String string : matches) {
            System.out.println("Match " + (dict.search(string)?"found":"not found") + " for word " + string);
        }
    }
}