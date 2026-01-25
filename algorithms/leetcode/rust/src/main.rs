use crate::algos::{
  p1_two_sum, p1390_four_divisors, p1411_no_ways_to_paint_grid, p1975_max_matrix_sum,
  p1984_minimum_difference_between_highest_n_lowest_of_k_scores,
};

fn main() {
  // problem 1
  // let nums = vec![1, 2, 3, 4];
  // let target = 6;
  // let res = p1_two_sum::Solution::two_sum(nums, target);
  // println!("{:#?}", res);

  // let (mut x, y): (usize, usize) = (2, 5);
  // x = x.max(y);

  // println!("sk{}", x)

  // let x = p1411_no_ways_to_paint_grid::Solution::num_of_ways(2);
  // println!("Value {x}");

  // let x = p1390_four_divisors::Solution::sum_four_divisors(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

  // let x = p1975_max_matrix_sum::Solution::max_matrix_sum(vec![
  //   vec![-1, 0, -1],
  //   vec![-2, 1, 3],
  //   vec![3, 2, 2],
  // ]);
  let x =
    p1984_minimum_difference_between_highest_n_lowest_of_k_scores::Solution::minimum_difference(
      vec![9, 4, 1, 7],
      2,
    );
  println!("answer {x} ");
}

pub mod algos;
