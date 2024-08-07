/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    const str = s.split(" ").reverse();
    return str.filter((s) => !!s).join(" ");
};

reverseWords( "  hello world  ");
