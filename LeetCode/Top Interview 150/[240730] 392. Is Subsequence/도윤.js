/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {

    if(s == "") return true;
    
    let sequencePoint = 0 ;
    let sequence = false;

    for(let i = 0; i < t.length; i++) {

        if (s[sequencePoint] !== t[i]) continue;

        if(sequencePoint === (s.length - 1)) {
            sequence = true;
        } 

        sequencePoint++;
    }

    return sequence
};
const s = "abc", t = "ahbgdc";

console.log(isSubsequence(s,t));






