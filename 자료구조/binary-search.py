# 재귀 함수
def binary_search(array, target, start, end):
    if start > end :
        return -1
    mid = (start + end) // 2

    # 원하는 값 찾은 경우
    if array[mid] == target:
        return mid
    # 원하는 값이 중간점 값보다 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점 값보다 큰 경우 오른쪽 확인
    else :
        return binary_search(array, target, mid+1, end)
    

# 반복문
def binary_search(array, target, start, end):
    while start <= end :
        mid = (start + end) // 2

        # 원하는 값 찾은 경우
        if array[mid] == target:
            return mid
        # 원하는 값이 중간점 값보다 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else :
            start = mid + 1
    return -1