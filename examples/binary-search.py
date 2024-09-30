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

# '정렬된 리스트'에서 `값이 특정 범위에 속하는 원소의 개수`를 구할 때
from bisect import bisect_left, bisect_right

def count_by_range(list, left_value, right_value):
    right_index = bisect_right(list, right_value)
    left_index = bisect_left(list, left_value)
    return right_index - left_index

# 직접 구현해보기 - bisect 사용하지 않고 구현
# left bound : target이 등장하는 가장 왼쪽 idx
def left_bound(lst, target):
    start = 0
    end = len(lst) - 1
    while start < end :
        mid = (start + end) // 2
        if lst[mid] >= target:
            end = mid
        else :
            start = mid +1
    return end

# right bound : target보다 큰 수 중 가장 왼쪽 idx
def right_bound(lst, target):
    start = 0
    end = len(lst) - 1
    while start < end :
        mid = (start + end) // 2
        if lst[mid] >= target:
            start = mid + 1
        else : 
            end = mid
    return start
