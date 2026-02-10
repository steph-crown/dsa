pub struct Solution;

impl Solution {
  pub fn is_trionic(nums: Vec<i32>) -> bool {
    let mut relations: Vec<char> = Vec::new();

    for i in 0..(nums.len() - 1) {
      let relation = if nums[i + 1] > nums[i] {
        '>'
      } else if nums[i + 1] < nums[i] {
        '<'
      } else {
        '='
      };

      if relations.len() == 0 || relation != relations[relations.len() - 1] {
        relations.push(relation);
      }
    }

    relations == vec!['>', '<', '>']
  }
}
