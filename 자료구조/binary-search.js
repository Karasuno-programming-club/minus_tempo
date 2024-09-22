/** 재귀 함수 */

function binarySearch(arr, target, start, end){
    if(start > end) return -1;
    let mid = parseInt((start + end) / 2)
    // 찾은 경우 중간점 인덱스 반환
    if(arr[mid] == target) return mid
    // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else if(arr[mid] > target) return binarySearch(arr, target, start, mid-1)
    // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else return binarySearch(arr, target, mid+1, end);
}

/** 반복문 */
function binarySearch(arr, target, start, end){
    while(start <= end){
        let mid = parseInt((start + end) / 2);
        // 찾은 경우 중간점 인덱스 반환
        if(arr[mid] == target) return mid;
        // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        else if(arr[mid] > target) end = mid - 1;
        // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else start = mid + 1;
    }
    return -1;
}

/** 정렬된 배열에서 특정 원소의 개수 구하기 */

function lowerBound(arr, target, start, end){
    while(start < end){
        let mid = parseInt((start + end) / 2);
        if(arr[mid] >= target) end = mid; // 최대한 왼쪽으로 이동하기
        else start = mid + 1;
    }
    return end;
}

function upperBound(arr, target, start, end){
    while(start < end){
        let mid = parseInt((start + end) / 2);
        if(arr[mid] > target) end = mid;
        else start = mid+1; // 최대한 오른쪽으로 이동하기
    }
    return end;
}

// 값이 [leftValue, rightValue]인 데이터의 개수를 반환하는 함수
function countByRange(arr, leftValue, rightValue){
    // 유의 : lowerBound와 upperBound는 end 변수의 값을 배열의 길이로 설정
    let rightIndex = upperBound(arr, rightValue, 0, arr.length)
    let leftIndex = lowerBound(arr, leftValue, 0, arr.length);
    return rightIndex - leftIndex;
}

// 활용
let arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
// 값이 4인 데이터 개수 출력
console.log(countByRange(arr, 4, 4))
// 값이 [-1, 3] 범위에 있는 데이터 개수 출력
console.log(countByRange(arr, -1, 3));