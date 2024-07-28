/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const words = s.split(" ").filter((word) => !!word);
    return words[words.length - 1].length;
};

console.log(lengthOfLastWord("   fly me   to   the moon  "));