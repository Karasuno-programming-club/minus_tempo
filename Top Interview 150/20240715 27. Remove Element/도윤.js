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


/**
 * 시간 복잡도 O(N)
 */
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

var removeElement2 = function(nums, val) {
    let idx = 0;

    for(let i = 0; i < nums.length; i++){
        if(nums[i] !== val){
            nums[idx] = nums[i];
            idx++
        } 
    }
    return idx
  
};

removeElement2([0,1,2,2,3,0,4,2], 2);


/** 1번 방식과 동일 */
var removeElement3 = function(nums, val) {

     let sp = 0;
     let ep = nums.length - 1;
     let cnt = 0;

     while(sp <= ep) {
        
        if(nums[sp] == val) {
            nums[sp] = nums[ep];
            ep--;
            cnt++;
        } else {
            sp++;
        }
     }
    return nums.length - cnt;
};

removeElement3([0,1,2,2,3,0,4,2], 2);