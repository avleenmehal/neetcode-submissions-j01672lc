class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        for(int i=0;i<n;i++){
            map.put(nums[i],map.getOrDefault(nums[i], 0) + 1);
        }

        List<Integer>[] freq = new List[nums.length + 1];

        for(int i =0; i<freq.length; i ++) {
            freq[i] = new ArrayList<>();
        }

        for(Map.Entry<Integer,Integer> kp : map.entrySet()) {
            freq[kp.getValue()].add(kp.getKey());
        }

        int[] res = new int[k];
        int index =0;

        for(int i =freq.length -1 ;i>0 && index<k;i--) {
            for(int number : freq[i]) {
                res[index++] =number;
                if(index==k) {
                    return res;
                }
            }
        }

        return res;
    }
}
