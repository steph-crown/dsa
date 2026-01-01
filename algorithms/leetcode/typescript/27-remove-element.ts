function removeElement(nums: number[], val: number): number {
  let totalMatch = 0;
  const lastIndex = nums.length - 1;

  // start from the ending
  // track the total matches
  // if val is seen, s, add to total matches and replace with item at index lastIndex - totalMatch
  // this way, all vals are at the end.
  // and after loop, do total length - totalmatch

  for (let i = nums.length - 1; i >= 0; i--) {
    if (nums[i] === val) {
      nums[i] = nums[lastIndex - totalMatch];
      ++totalMatch;
    }
  }

  return nums.length - totalMatch;
}
