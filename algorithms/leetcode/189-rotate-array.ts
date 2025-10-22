/**
 Do not return anything, modify nums in-place instead.
 */
//  first solution
function rotate(nums: number[], k: number): void {
  const res = [...nums];

  for (let i = 0; i < res.length; i++) {
    nums[(i + k) % nums.length] = res[i];
  }
}

// [1,2,3,4,5,6,7], 3 ->  [5,6,7,1,2,3,4]
// how?
// reverse array -> [7,6,5,4,3,2,1]
// reverse from index 0 to (3 - 1) and index 3 to (nums - 1)
function rotateSecond(nums: number[], k: number): void {
  k = k % nums.length;

  let l = 0,
    r = nums.length - 1;
  while (l < r) {
    const temp = nums[r];
    nums[r--] = nums[l];
    nums[l++] = temp;
  }

  (l = 0), (r = k - 1);
  while (l < r) {
    const temp = nums[r];
    nums[r--] = nums[l];
    nums[l++] = temp;
  }

  (l = k), (r = nums.length - 1);
  while (l < r) {
    const temp = nums[r];
    nums[r--] = nums[l];
    nums[l++] = temp;
  }
}
