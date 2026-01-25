pub struct Solution;

impl Solution {
  pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
    let mut sorted = nums.clone();
    sorted.sort_unstable();
    let k = k as usize;

    sorted
      .windows(k)
      .map(|w| w[k - 1] - w[0])
      .min()
      .unwrap_or(0)
  }
}
