/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {

    let prefix = strs[0];

    for (let i = 1; i < strs.length; i++) {
        while(!strs[i].startsWith(prefix) && prefix.length > 0) {
            prefix = prefix.substring(0, prefix.length - 1)
        }

        if(prefix === "") return prefix;
    }

    return prefix;  
};

// O(M * N)
console.log(longestCommonPrefix(["dog","racecar","car"]));


var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return "";

    // 가장 짧은 문자열의 길이를 구합니다.
    let minLen = Math.min(...strs.map(s => s.length));

    // 공통 접두사를 저장할 변수
    let commonPrefix = "";

    for (let i = 0; i < minLen; i++) {
        // 현재 인덱스 i의 문자들을 확인
        let currentChar = strs[0][i];
        
        // 모든 문자열이 동일한 문자를 갖고 있는지 확인
        if (strs.every(s => s[i] === currentChar)) {
            commonPrefix += currentChar;
        } else {
            break;
        }
    }

    return commonPrefix;
};
