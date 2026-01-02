pub struct Solution;

impl Solution {
  pub fn max_profit(prices: Vec<i32>) -> i32 {
    let mut smallest = i32::MAX;
    let mut max_p = 0;

    for i in prices {
      smallest = smallest.min(i);
      max_p = max_p.max(i - smallest)
    }

    max_p
  }
}
