pub struct Solution;

impl Solution {
  pub fn min_operations(s: String) -> i32 {
    let mut start_0_diff = 0;
    let n = s.len() as i32;

    let chars = s.chars();

    for (i, c) in s.chars().enumerate() {
      let expected = if i % 2 == 0 { '0' } else { '1' };
      if c != expected {
        start_0_diff += 1;
      }
    }

    start_0_diff.min(n - start_0_diff)
  }
}
