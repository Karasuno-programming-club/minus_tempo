var isSubsequence = function (s, t) {
  let sIdx = 0;

  for (let i = 0; i < t.length; i++) {
    if (s[sIdx] === t[i]) {
      sIdx++;
    }
  }

  return sIdx === s.length;
};
