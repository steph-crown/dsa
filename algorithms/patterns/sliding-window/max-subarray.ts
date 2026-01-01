const maxSubarray = (arr: number[], k: number) => {
  let windowSum = arr.slice(0, k).reduce((num1, num2) => num1 + num2);
  let maxSum = windowSum;

  for (let i = k; i < arr.length; i++) {
    windowSum = windowSum - arr[i - k] + arr[i];
    maxSum = Math.max(windowSum, maxSum);
  }

  return maxSum;
};

console.log(maxSubarray([1, 12, 3, 4, 5, 6], 3));

// [1, 2, 3, 4, 5, 6]; 2
