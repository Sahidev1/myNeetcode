package valid_anagram.java;

//Difficulty easy
public class Solution {
    private final int[] letterMap = new int[(122-97)+1];

    private void incrementCount( char letter){
        letterMap[letter - 97]++;
    }

    private void decrementCount(char letter){
        letterMap[letter - 97]--;
    }



    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int len = s.length();
        for(int i = 0; i < len; i++){
            incrementCount(s.charAt(i));
            decrementCount(t.charAt(i));
        }
        for (int i = 0; i < letterMap.length; i++){
            if(letterMap[i] != 0) return false;
        }

        return true;
    }
}
