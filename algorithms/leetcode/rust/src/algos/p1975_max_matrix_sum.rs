pub struct Solution;

impl Solution {
  pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
    let mut neg_count: i64 = 0;
    let mut min_abs: i64 = i64::MAX;
    let mut total_abs_sum: i64 = 0;

    for &cell in matrix.iter().flatten() {
      let cell_i64 = cell as i64;
      total_abs_sum += cell_i64.abs();
      min_abs = min_abs.min(cell_i64.abs());

      if cell_i64 < 0 {
        neg_count += 1;
      }
    }

    if neg_count % 2 == 0 {
      total_abs_sum
    } else {
      total_abs_sum - (2 * min_abs)
    }
  }
}
