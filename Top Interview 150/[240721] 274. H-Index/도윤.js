/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {

    citations.sort((a,b) => b - a);
    for (let i = 0; i < citations.length; i++) {
        if(citations[i] < i + 1) {
            return i 
        }
    }

   return citations.length
};

console.log(hIndex([100]))

/**
 * 인용 횟수가 3번 이상인 논문이 3개 
 * hInde는 3
 * 시간복잡도 O(N Log N)
 */


var hIndex2 = function(citations) {
    //길이보다 +1의 빈 배열 작성
    // 0 ~ 배열길이만큼 만들어서 카운팅용으로 제작
    let arr = Array(citations.length+1).fill(0);
    
    // Step 1. 인용회수를 배열 내 저장
    for (let item of citations) {
        if (item >= citations.length) {
            ++arr[citations.length];
        }
        else {
            ++arr[item];
        };
    };

    // [3,0,6,1,5] >> [1,1,0,1,0,2]

    // Step 2. 역순 루프
    // 인용값을 이전 값에 계속적으로 더해줘야 함 (5회는 4회를 포함하기 때문)
    for (let i = arr.length-1; i > 0 ; i--) {
        if (i <= arr[i]) {
            return i;
        } else {
            arr[i-1] += arr[i]
        }
    };

    return 0;
};

// 최종 [ 1, 1, 0, 3, 2, 2 ]


// 시간복잡도 O(3N)

hIndex2([3,0,6,1,5])