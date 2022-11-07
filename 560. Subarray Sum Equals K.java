    class Solution {
    public int subarraySum(int[] nums, int k) {
        int sum = 0;
        int counter = 0;
        Map<Integer, Integer> stateMap = new HashMap<>();
        stateMap.put(0, 1);

        for (int num : nums) {
            sum += num;
            if (stateMap.containsKey(sum - k)) {
                counter += stateMap.get(sum - k);
            }
            stateMap.put(sum, stateMap.getOrDefault(sum, 0) + 1);
        }
        return counter;
    }
}