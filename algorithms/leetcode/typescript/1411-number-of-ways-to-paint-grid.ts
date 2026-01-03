function numOfWays(n: number): number {
  let aba = 6;
  let abc = 6;
  let MOD = 1e9 + 7;

  for (let i = 1; i < n; i++) {
    let nextAba = (aba * 3 + abc * 2) % MOD;
    let nextAbc = (aba * 2 + abc * 2) % MOD;

    aba = nextAba;
    abc = nextAbc;
  }

  return (aba + abc) % MOD;
}

// ABA (previous row)
// BAB. BAC  BCB  CAB.  CAC

// ABC (previous row)
// BAB.  BCA.  BCB   CAB

/*ABA           ABC
  6             6
  ABA.  ABC.    ABA.     ABC
  3.    2.      2.       2
  3.    2.      2.       2
 */
