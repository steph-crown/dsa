/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  let p1 = m - 1,
    p2 = n - 1,
    writeIndex = nums1.length - 1;

  while (p2 >= 0) {
    if (p1 >= 0 && nums1[p1] >= nums2[p2]) {
      nums1[writeIndex] = nums1[p1];
      --p1;
    } else {
      nums1[writeIndex] = nums2[p2];
      --p2;
    }
    --writeIndex;
  }
}
