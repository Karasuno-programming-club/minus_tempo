var threeSum = function(nums) {
    nums.sort((a, b) => a - b);

    let arr = [];

    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue; // i가 이전 값과 같으면 건너뛰기
        }

        let sp = i + 1;
        let ep = nums.length - 1;

        while (sp < ep) {
            let sum = nums[i] + nums[sp] + nums[ep];

            if (sum === 0) {
                arr.push([nums[i], nums[sp], nums[ep]]);

                while (sp < ep && nums[sp] === nums[sp + 1]) {
                    sp++; // sp가 이전 값과 같으면 건너뛰기
                }

                while (sp < ep && nums[ep] === nums[ep - 1]) {
                    ep--; // ep가 이전 값과 같으면 건너뛰기
                }

                sp++;
                ep--;
            } else if (sum > 0) {
                ep--;
            } else {
                sp++;
            }
        }
    }

    return arr;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));

//기본 방향성은 풀었으나 중복제거를 못했음