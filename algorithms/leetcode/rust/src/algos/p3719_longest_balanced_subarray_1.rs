use std::collections::HashSet;

struct Solution;

impl Solution {
  pub fn longest_balanced(nums: Vec<i32>) -> i32 {
    let mut seen: HashSet<i32> = HashSet::new();
    let mut dups = 0;
    let mut odds = 0;
    let mut evens = 0;

    for num in nums {
      if seen.contains(&num) {
        dups += 1;
        continue;
      }

      if num % 2 == 0 {
        evens += 1;
      } else {
        odds += 1;
      }

      seen.insert(num);
    }

    (odds.min(evens) * 2) + dups
  }

  pub fn sjsj() {
    Self::longest_balanced(vec![]);
  }
}
