use std::collections::HashSet;

pub struct Solution;

impl Solution {
  pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
    let mut seen: HashSet<i32> = HashSet::new();

    for num in nums {
      if !seen.insert(num) {
        return num;
      }
    }

    0
  }
}
