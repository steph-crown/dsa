function topKFrequent(n: number[], k: number) {
  const m = new Map();

  for (let i of n) {
    const newCount = (m.get(i) || 0) + 1;
    m.set(i, newCount);
  }

  // bucket of frequerncies. each bucket identifies a frequeency
  const bucket: number[][] = new Array(n.length).fill(null).map(() => []);

  m.forEach((freq, num) => {
    bucket[freq].push(Number(num));
  });

  // console.log({ bucket, m });

  const res: number[] = [];

  for (let i = bucket.length - 1; res.length < k; i--) {
    // console.log({ i, ib: bucket[i], bucket, res });
    if (bucket[i].length) {
      const remainingSlots = k - res.length;
      console.log({ remainingSlots });

      if (bucket[i].length > remainingSlots) {
        res.push(...bucket[i].slice(0, remainingSlots));
        break;
      }

      res.push(...bucket[i]);
    }
  }

  return res;
}

console.log(topKFrequent([1, 2, 3, 4, 5, 5, 4], 4));

// edge case
// - k is bigger than number of uniques.
// - there are multiple unique items with same frequency such that it's more than k
