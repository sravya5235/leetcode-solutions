class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> substring = new HashSet<>();
        int left = 0;
        int maxLength = 0;
        for(int right = 0; right < s.length(); right++){
            while(substring.contains(s.charAt(right))){
                substring.remove(s.charAt(left));
                left++;
            }
            substring.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}