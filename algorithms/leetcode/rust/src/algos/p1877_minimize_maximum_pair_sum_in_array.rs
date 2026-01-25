struct Solution;

impl Solution {
  pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
    let mut sorted: Vec<i32> = nums.clone();
    sorted.sort_unstable();
    let sum: i32 = sorted.iter().sum();
    let len = sorted.len();
    let mut max_pair_sum = 0;

    for i in (0..(len / 2)) {
      let pair_sum = sorted[i] + sorted[len - i - 1];
      max_pair_sum = max_pair_sum.max(pair_sum);
    }

    return max_pair_sum;
  }
}
