function minimumPairRemoval(nums: number[]): number {
  let operations = 0;

  const isSorted = (arr: number[]): boolean => {
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) return false;
    }
    return true;
  };

  while (!isSorted(nums)) {
    let minSum = Infinity;
    let minIndex = -1;

    for (let i = 0; i < nums.length - 1; i++) {
      const currentSum = nums[i] + nums[i + 1];
      if (currentSum < minSum) {
        minSum = currentSum;
        minIndex = i;
      }
    }

    nums.splice(minIndex, 2, minSum);
    operations++;
  }

  return operations;
}
