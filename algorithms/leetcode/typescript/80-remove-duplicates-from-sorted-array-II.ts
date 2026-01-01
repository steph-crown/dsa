function removeDuplicatesII(nums: number[]): number {
  // create `k` to keep track of the uniques of max 2
  // loop through `nums` and check if a number is the same as the one two indexes prior
  // if not the same, set in position k of nums and increase `k`, else, do nothing.

  let k = 0;

  for (const num of nums) {
    if (k < 2 || num !== nums[k - 2]) {
      nums[k++] = num;
    }
  }

  return k;
}
