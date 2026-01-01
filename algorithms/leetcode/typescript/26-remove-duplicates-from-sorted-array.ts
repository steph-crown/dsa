function removeDuplicates(nums: number[]): number {
  // pointer starting from 1
  // last unique number start from nums[0]
  // loop to the end, i
  // if nums[i] !== current unique, nums[pointer] = nums[i]
  // pointer++
  // update last unique

  let k = 1;
  let lastUnique = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== lastUnique) {
      nums[k] = nums[i];

      ++k;
      lastUnique = nums[i];
    }
  }

  return k;
}
