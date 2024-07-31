var isPalindrome = function (s) {
  let forward = "";
  let backward = "";
  let lowerS = s.toLowerCase();

  for (let i = 0; i < s.length; i++) {
    let charCode = lowerS.charCodeAt(i);
    if (
      (charCode >= 97 && charCode <= 122) ||
      (charCode >= 48 && charCode <= 57)
    ) {
      forward += lowerS[i];
      backward = lowerS[i] + backward;
    }
  }
  return forward === backward;
};
