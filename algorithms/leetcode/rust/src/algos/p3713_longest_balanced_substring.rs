use std::collections::HashMap;

struct Solution;

impl Solution {
  pub fn longest_balanced(s: String) -> i32 {
    let mut max_l = 0;
    let n = s.len();
    let mut chars = s.chars().collect::<Vec<char>>();

    for i in 0..n {
      let mut freq: HashMap<char, i32> = HashMap::new();

      for j in i..n {
        let char = chars[j];
        *freq.entry(char).or_insert(0) += 1;

        let mut balanced = true;

        let mut counts = freq.values();
        let prev_count = counts.next().unwrap_or(&0);

        for count in counts {
          if *count != *prev_count {
            balanced = false;
            break;
          }
        }

        if balanced {
          let len = j - i + 1;
          max_l = len.max(max_l);
        }
      }
    }

    max_l as i32
  }
}
