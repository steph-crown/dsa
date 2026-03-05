use std::collections::HashSet;

pub struct Solution;

impl Solution {
  pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
    let mut cols: HashSet<usize> = HashSet::new();
    let mut rows: HashSet<usize> = HashSet::new();
    let m = mat.len();
    let n = mat[0].len();

    for i in 0..m {
      for j in 0..n {
        if mat[i][j] == 1 {
          if !cols.remove(&j) {
            cols.insert(j);
          }

          if !rows.remove(&i) {
            rows.insert(i);
          }
        }
      }
    }

    3
  }
}
