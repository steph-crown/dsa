pub struct Solution;

impl Solution {
  pub fn minimum_cost(nums: Vec<i32>, k: i32, dist: i32) -> i32 {
    let first = nums[0]; // Mandatory cost
    let mut min1 = i32::MAX;
    let mut min2 = i32::MAX;

    // Iterate once through the rest of the array
    for &val in nums.iter().skip(1) {
      if val < min1 {
        min2 = min1;
        min1 = val;
      } else if val < min2 {
        min2 = val;
      }
    }

    first + min1 + min2
  }
}
