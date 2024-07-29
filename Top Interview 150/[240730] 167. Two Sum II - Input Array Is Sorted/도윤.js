var twoSum = function(numbers, target) {


    let sp = 0;
    let ep = numbers.length - 1;

    
    while(sp <= ep) {

        const sum = numbers[sp] + numbers[ep];
        
        if(sum == target) return [sp + 1, ep + 1];

        if(target > sum) {
            sp++;    
        } else {
            ep--;   
        }
    }
};
