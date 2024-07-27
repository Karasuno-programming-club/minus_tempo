var romanToInt = function(s) {
    const romans = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    };

    const twinRomans = {
        'CM' : 900,
        'CD' : 400,
        'XC' : 90,
        'XL' : 40,
        'IX' : 9,
        'IV' : 4
    }

    let pos = 0;
    let answer = 0;

    while(pos < s.length){
        if(pos <= s.length - 2 && !!twinRomans[s.slice(pos, pos + 2)]){
            answer += twinRomans[s.slice(pos, pos + 2)];
            pos += 2;
        } else {
            answer += romans[s[pos]]
            pos++
        }
    }

    return answer;
};

// time : O(N)
// space : O(1)

// 다른 풀이
var romanToInt = function(s) {
    value = 0;
    for(let i = 0; i < s.length; i+=1){
        symbols[s[i]] < symbols[s[i+1]] ? value -= symbols[s[i]]: value += symbols[s[i]]
    }
    return value
};

// 무조건 왼쪽 값이 오른쪽 값보다 클 수 밖에 없음
// 왼쪽 값이 크다면 그만큼 빼면됨