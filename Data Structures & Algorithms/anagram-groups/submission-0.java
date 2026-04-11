class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char tempArr[] = strs[i].toCharArray();
            Arrays.sort(tempArr);
            String sortedStr = new String(tempArr);
            
            if (map.containsKey(sortedStr)) {
                List<String> strArr = map.get(sortedStr);
                strArr.add(strs[i]);
                map.put(sortedStr, strArr);
            } else {
                List<String> strArr = new ArrayList<>();
                strArr.add(strs[i]);
                map.put(sortedStr, strArr);
            }
        }
        
        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            result.add(entry.getValue());
        }
        return result;
    }
}
