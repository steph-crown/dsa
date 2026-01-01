use crate::algos::p1_two_sum;

fn main() {
  // problem 1
  let nums = vec![1, 2, 3, 4];
  let target = 6;
  let res = p1_two_sum::Solution::two_sum(nums, target);
  println!("{:#?}", res);
}

pub mod algos;
