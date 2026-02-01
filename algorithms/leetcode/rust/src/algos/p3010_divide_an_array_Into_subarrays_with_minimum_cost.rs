struct Solution;

impl Solution {
  pub fn minimum_cost(nums: Vec<i32>) -> i32 {
    // first number is part
    // pick smallest other two numbers
    let mut iter = nums.iter();
    let min_cost = iter.next().unwrap_or(&0);
    let mut rest: Vec<i32> = iter.copied().collect();
    rest.sort_unstable();

    min_cost + rest[0] + rest[1]
  }
}
