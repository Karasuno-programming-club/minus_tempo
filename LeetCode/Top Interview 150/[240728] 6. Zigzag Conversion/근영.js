var convert = function (s, numRows) {
  let strings = {};
  let gap = numRows - 2; // 중간에 들어가는 수의 개수
  let std = numRows + gap; // 배수

  if (numRows < 2) return s; // 2개 이하면 지그재그가 될 수 없다

  for (let i = 0; i < numRows; i++) {
    strings[i] = "";
  }

  for (let i = 0; i < s.length; i++) {
    if (typeof strings[i % std] === "string") {
      strings[i % std] += s[i];
    } else {
      strings[std - (i % std)] += s[i];
    }
  }

  let answer = "";

  Object.values(strings).forEach((v) => (answer += v));

  return answer;
};

// 안보고 풀었다 ~~~~~ 뿌듯뿌듯
// time : O(N)
// space : O(N)
