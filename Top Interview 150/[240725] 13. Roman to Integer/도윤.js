/**
 * @param {string} 
 * @return {number}
 */
var romanToInt = function(s) {
    
    const charArr = s.split("");
    const map = new Map();

    map.set("I", 1);
    map.set("IV", 4);
    map.set("V", 5);
    map.set("IX", 9);
    map.set("X", 10);
    map.set("XL", 40);
    map.set("L", 50);
    map.set("XC", 90);
    map.set("C", 100);
    map.set("CD", 400);
    map.set("D", 500);
    map.set("CM", 900);
    map.set("M", 1000);
    

    let sum = 0;
    let i = 0;

    while (i < charArr.length) {
        const exceptionRoman = map.get(charArr[i] + charArr[i+1]);
        sum += exceptionRoman ? exceptionRoman : map.get(charArr[i]); 
        i += exceptionRoman ? 2 : 1;
    }
    
    return sum;
};  




romanToInt("MCMXCIV")