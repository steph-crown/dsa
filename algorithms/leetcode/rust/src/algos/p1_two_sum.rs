use std::collections::HashMap;

pub struct Solution;

impl Solution {
  pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut seen: HashMap<i32, usize> = HashMap::with_capacity(nums.len());

    for (i, &num) in nums.iter().enumerate() {
      let compliment = target - num;

      if let Some(&prev_index) = seen.get(&compliment) {
        return vec![i as i32, prev_index as i32];
      }

      seen.insert(num, i);
    }

    vec![]
  }
}
