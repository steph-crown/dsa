pub struct Solution;

impl Solution {
  pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
    nums
      .iter()
      .map(|&num| {
        for i in 0..num {
          if i | (i + 1) == num {
            return i;
          }
        }
        return -1;
      })
      .collect::<Vec<i32>>()
  }
}
