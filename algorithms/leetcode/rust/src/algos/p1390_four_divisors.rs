pub struct Solution;

impl Solution {
  pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
    let mut sum = 0;

    for num in nums {
      let mut divisor_count = 0;
      let mut divisor_sum = 0;

      println!("num {num} root {}", ((num as f64).sqrt()) as i32);
      for i in 1..(((num as f64).sqrt()) as i32 + 1) {
        let divides = (num % i) == 0;

        if divides {
          divisor_count += if i * i == num { 1 } else { 2 };
          divisor_sum += if i * 1 == num { i } else { i + (num / i) };
        }
      }

      if divisor_count == 4 {
        sum += divisor_sum
      }
    }

    sum
  }
}
