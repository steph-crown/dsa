use std::collections::HashMap;

pub struct Solution;

// fn main() {
//   let v = vec![1, 2, 3, 4];
//   let b = Solution::two_sum(v, 4);
//   println!("{:#?}", b);
// }

// [3,2,4], 6
impl Solution {
  pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut m: HashMap<i32, usize> = HashMap::new();

    for (i, n) in nums.iter().enumerate() {
      if let Some(&c) = m.get(n) {
        if i == c {
          continue;
        }

        return vec![i as i32, c as i32];
      } else {
        let c = target - *n;
        m.insert(c, i);
      }
    }

    vec![]
  }
}
