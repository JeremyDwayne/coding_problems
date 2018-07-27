import java.util.HashMap;
import java.util.Map;

/*
 * Problem 1
 * 07/26/2018
 * Given a list of numbers and a number k, return whether any two numbers from the list add up to k. 
 * For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17. 
 * Bonus: Can you do this in one pass?
 */

class Problem001 {
  public static void main(String[] args){
    int[] vals = {10,15,3,7};
    System.out.println(twoSum(vals, 17));
  }

  public static boolean twoSum(int[] nums, int k){
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++){
      int complement = k - nums[i];
      if (map.containsKey(complement)) {
        return true;
      }
      map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No solution");
  }
}
