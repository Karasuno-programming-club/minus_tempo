var reverseWords = function (s) {
  return s
    .split(" ")
    .reverse()
    .filter((v) => !!v)
    .join(" ");
};

// 뭔가 너무 쉬움..
