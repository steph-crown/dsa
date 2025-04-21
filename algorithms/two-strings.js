// Project: HackerRank - Strings - Two Strings. return "YES" if there is a common substring between the two strings, otherwise return "NO"
function twoStrings(s1, s2) {
  const charSet = new Set(s1);

  for (const char of s2) {
    if (charSet.has(char)) {
      return "YES";
    }
  }
  return "NO";
}

console.log(twoStrings("he", "world"));
