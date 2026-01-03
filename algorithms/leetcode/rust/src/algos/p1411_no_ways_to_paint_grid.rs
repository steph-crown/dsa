pub struct Solution {}

impl Solution {
  pub fn num_of_ways(num: i32) -> i32 {
    const MOD: i64 = 1_000_000_007;
    let mut abc = 6;
    let mut aba = 6;

    for _ in 1..num {
      let next_abc = (abc * 2 + aba * 2) % MOD;
      let next_aba = (abc * 2 + aba * 3) % MOD;

      abc = next_abc;
      aba = next_aba;
    }

    ((aba + abc) % MOD) as i32
  }
}
