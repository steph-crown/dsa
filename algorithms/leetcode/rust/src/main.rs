use crate::algos::{p1_two_sum, p1411_no_ways_to_paint_grid};

fn main() {
  // problem 1
  // let nums = vec![1, 2, 3, 4];
  // let target = 6;
  // let res = p1_two_sum::Solution::two_sum(nums, target);
  // println!("{:#?}", res);

  // let (mut x, y): (usize, usize) = (2, 5);
  // x = x.max(y);

  // println!("sk{}", x)

  let x = p1411_no_ways_to_paint_grid::Solution::num_of_ways(2);
  println!("Value {x}");
}

pub mod algos;
