struct Solution;

impl Solution {
  pub fn minimum_abs_difference(arr: Vec<i32>) -> Vec<Vec<i32>> {
    let mut sorted = arr.clone();
    sorted.sort_unstable();

    let windows = sorted.windows(2);

    let min_diff = sorted
      .windows(2)
      .map(|w| w[0].abs_diff(w[1]))
      .min()
      .unwrap_or(0);

    sorted
      .windows(2)
      .filter(|w| w[0].abs_diff(w[1]) == min_diff)
      .map(|w| w.to_vec())
      .collect::<Vec<Vec<i32>>>()
  }
}
