pub struct Solution;

impl Solution {
  pub fn num_steps(mut s: String) -> i32 {
    let mut steps = 0;
    while s != "1" {
      // even.
      if s.ends_with("0") {
        s.pop();
      } else {
        let mut value = u128::from_str_radix(&s, 2).unwrap();
        value += 1;

        s = format!("{:b}", value);
      }

      steps += 1;
    }

    steps
  }
}
