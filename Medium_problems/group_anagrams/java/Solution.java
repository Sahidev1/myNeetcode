

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();

        String key;
        List<String> tmp;
        for (String string : strs) {
            key = sortedCharSeq(string); //O(nlogn)
            if(map.containsKey(key)){
                map.get(key).add(string);
            } else {
                tmp = new ArrayList<>();
                tmp.add(string);
                map.put(key, tmp);
            }
        } // O(m*NlogN) where N is average string length and m is number of strings
        return new ArrayList<>(map.values());
    }

    // O(nlog(n)), n = string.length
    private String sortedCharSeq(String s){
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }
}
