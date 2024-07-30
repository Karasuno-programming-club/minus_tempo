/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    
    const a = s.toLocaleLowerCase().replace(/[^a-z0-9]+/g, "");
    const b = a.split("").reverse().join("");

    return a == b;
};

// console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("race a car"));

//이래봐도 O(N)임