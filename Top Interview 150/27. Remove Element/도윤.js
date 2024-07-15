/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */

var swap = function (arr, idx1, idx2) {
    const tmp = arr[idx2];
    arr[idx2] = arr[idx1];
    arr[idx1] = tmp;
}

var removeElement = function(nums, val) {
    let endIndex = nums.length - 1; 
    let i = 0; 

    while (i <= endIndex) {
        if (nums[i] === val) {            
            swap(nums, i, endIndex);
            endIndex--; 
        } else {
            i++; 
        }
    }

    return endIndex + 1;
}

// https://en.wikipedia.org/wiki/In-place_algorithm 

removeElement([3,2,2,3], 3)
