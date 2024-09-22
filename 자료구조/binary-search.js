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